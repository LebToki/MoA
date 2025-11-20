"""
Self-update utility for MoA Chatbot
Checks for updates from git repository and can pull/apply them
"""
import os
import subprocess
import sys
import requests
from pathlib import Path
from loguru import logger
from typing import Optional, Tuple

# Get the repository root directory
REPO_ROOT = Path(__file__).parent.absolute()

# Version from pyproject.toml or fallback
CURRENT_VERSION = "2.0.2"
try:
    # Try Python 3.11+ tomllib first
    try:
        import tomllib
        with open(REPO_ROOT / "pyproject.toml", "rb") as f:
            pyproject = tomllib.load(f)
            CURRENT_VERSION = pyproject.get("project", {}).get("version", CURRENT_VERSION)
    except ImportError:
        # Fallback to tomli for older Python versions
        try:
            import tomli as tomllib
            with open(REPO_ROOT / "pyproject.toml", "rb") as f:
                pyproject = tomllib.load(f)
                CURRENT_VERSION = pyproject.get("project", {}).get("version", CURRENT_VERSION)
        except ImportError:
            # Fallback: try to parse manually
            import re
            with open(REPO_ROOT / "pyproject.toml", "r", encoding="utf-8") as f:
                content = f.read()
                match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', content)
                if match:
                    CURRENT_VERSION = match.group(1)
except Exception:
    pass  # Use default version


class UpdateChecker:
    """Handles checking and applying updates from git repository"""
    
    def __init__(self, repo_path: Optional[str] = None, remote_url: Optional[str] = None):
        """
        Initialize the update checker
        
        Args:
            repo_path: Path to git repository (defaults to current directory)
            remote_url: Remote repository URL (defaults to origin)
        """
        self.repo_path = Path(repo_path) if repo_path else REPO_ROOT
        self.remote_url = remote_url
        
    def _run_git_command(self, command: list, check: bool = False) -> Tuple[bool, str]:
        """
        Run a git command and return success status and output
        
        Args:
            command: List of command parts (e.g., ['git', 'pull'])
            check: If True, raise exception on failure
            
        Returns:
            Tuple of (success: bool, output: str)
        """
        try:
            result = subprocess.run(
                command,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=check
            )
            return result.returncode == 0, result.stdout.strip() + result.stderr.strip()
        except subprocess.CalledProcessError as e:
            if check:
                raise
            return False, str(e)
        except Exception as e:
            return False, str(e)
    
    def get_current_branch(self) -> Optional[str]:
        """Get the current git branch"""
        success, output = self._run_git_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        return output if success else None
    
    def get_current_commit(self) -> Optional[str]:
        """Get the current git commit hash"""
        success, output = self._run_git_command(['git', 'rev-parse', 'HEAD'])
        return output if success else None
    
    def get_remote_url(self) -> Optional[str]:
        """Get the remote repository URL"""
        success, output = self._run_git_command(['git', 'remote', 'get-url', 'origin'])
        return output if success else self.remote_url
    
    def fetch_updates(self) -> bool:
        """Fetch latest changes from remote without merging"""
        logger.info("Fetching updates from remote repository...")
        success, output = self._run_git_command(['git', 'fetch', 'origin'])
        if success:
            logger.info("Successfully fetched updates from remote")
        else:
            logger.error(f"Failed to fetch updates: {output}")
        return success
    
    def check_for_updates(self) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Check if there are updates available
        
        Returns:
            Tuple of (has_updates: bool, current_commit: str, latest_commit: str)
        """
        # Get current commit
        current_commit = self.get_current_commit()
        if not current_commit:
            logger.warning("Could not determine current commit. Not a git repository?")
            return False, None, None
        
        # Fetch latest changes
        if not self.fetch_updates():
            return False, current_commit, None
        
        # Get latest commit from remote
        branch = self.get_current_branch() or "main"
        success, latest_commit = self._run_git_command(
            ['git', 'rev-parse', f'origin/{branch}']
        )
        
        if not success:
            logger.warning("Could not determine latest commit from remote")
            return False, current_commit, None
        
        has_updates = current_commit != latest_commit
        return has_updates, current_commit, latest_commit
    
    def get_version_from_github(self) -> Optional[str]:
        """
        Get the latest version from GitHub releases or pyproject.toml
        
        Returns:
            Version string or None
        """
        remote_url = self.get_remote_url()
        if not remote_url:
            return None
        
        # Try to extract GitHub repo info
        # Format: https://github.com/owner/repo.git or git@github.com:owner/repo.git
        try:
            if 'github.com' in remote_url:
                # Extract owner/repo
                if remote_url.startswith('https://'):
                    parts = remote_url.replace('.git', '').split('/')
                    owner = parts[-2]
                    repo = parts[-1]
                elif remote_url.startswith('git@'):
                    parts = remote_url.replace('.git', '').split(':')
                    owner_repo = parts[-1].split('/')
                    owner = owner_repo[0]
                    repo = owner_repo[1]
                else:
                    return None
                
                # Try to get latest release from GitHub API
                api_url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
                try:
                    response = requests.get(api_url, timeout=5)
                    if response.status_code == 200:
                        release_data = response.json()
                        return release_data.get('tag_name', '').lstrip('v')
                except Exception as e:
                    logger.debug(f"Could not fetch from GitHub API: {e}")
        except Exception as e:
            logger.debug(f"Could not parse remote URL: {e}")
        
        return None
    
    def pull_updates(self, branch: Optional[str] = None) -> Tuple[bool, str]:
        """
        Pull updates from remote repository
        
        Args:
            branch: Branch to pull from (defaults to current branch)
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        if branch is None:
            branch = self.get_current_branch() or "main"
        
        logger.info(f"Pulling updates from origin/{branch}...")
        
        # First fetch
        if not self.fetch_updates():
            return False, "Failed to fetch updates"
        
        # Then pull
        success, output = self._run_git_command(['git', 'pull', 'origin', branch])
        
        if success:
            logger.info(f"Successfully pulled updates: {output}")
            return True, f"Successfully updated to latest version. Output: {output}"
        else:
            logger.error(f"Failed to pull updates: {output}")
            return False, f"Failed to pull updates: {output}"
    
    def get_update_info(self) -> dict:
        """
        Get comprehensive update information
        
        Returns:
            Dictionary with update information
        """
        has_updates, current_commit, latest_commit = self.check_for_updates()
        current_branch = self.get_current_branch()
        remote_version = self.get_version_from_github()
        
        return {
            "current_version": CURRENT_VERSION,
            "remote_version": remote_version,
            "has_updates": has_updates,
            "current_branch": current_branch,
            "current_commit": current_commit[:8] if current_commit else None,
            "latest_commit": latest_commit[:8] if latest_commit else None,
            "is_git_repo": current_commit is not None,
        }


def check_updates() -> dict:
    """Convenience function to check for updates"""
    checker = UpdateChecker()
    return checker.get_update_info()


def update_application() -> Tuple[bool, str]:
    """Convenience function to update the application"""
    checker = UpdateChecker()
    return checker.pull_updates()


if __name__ == "__main__":
    # CLI interface for testing
    import argparse
    
    parser = argparse.ArgumentParser(description="MoA Chatbot Update Checker")
    parser.add_argument("--check", action="store_true", help="Check for updates")
    parser.add_argument("--update", action="store_true", help="Pull and apply updates")
    parser.add_argument("--info", action="store_true", help="Show update information")
    
    args = parser.parse_args()
    
    checker = UpdateChecker()
    
    if args.check:
        has_updates, current, latest = checker.check_for_updates()
        if has_updates:
            print(f"✓ Updates available!")
            print(f"  Current: {current[:8] if current else 'unknown'}")
            print(f"  Latest:  {latest[:8] if latest else 'unknown'}")
        else:
            print("✓ You are up to date!")
    
    elif args.update:
        success, message = checker.pull_updates()
        if success:
            print(f"✓ {message}")
            print("\nNote: You may need to restart the application for changes to take effect.")
        else:
            print(f"✗ {message}")
    
    elif args.info:
        info = checker.get_update_info()
        print("Update Information:")
        print(f"  Current Version: {info['current_version']}")
        print(f"  Remote Version:  {info['remote_version'] or 'unknown'}")
        print(f"  Current Branch:  {info['current_branch']}")
        print(f"  Current Commit:  {info['current_commit']}")
        print(f"  Latest Commit:   {info['latest_commit']}")
        print(f"  Has Updates:     {info['has_updates']}")
        print(f"  Is Git Repo:     {info['is_git_repo']}")
    
    else:
        parser.print_help()

