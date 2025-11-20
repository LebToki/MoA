#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MoA Chatbot Self-Update Script
Run this script to check for and apply updates from the git repository
"""
import sys
import os

# Fix Windows console encoding for Unicode characters
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        # Python < 3.7
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

from update_checker import UpdateChecker, check_updates, update_application

def main():
    """Main entry point for the update script"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="MoA Chatbot Self-Update Utility",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python update.py --check          Check for available updates
  python update.py --update         Pull and apply updates
  python update.py --info           Show detailed update information
        """
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check for available updates"
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Pull and apply updates from git repository"
    )
    parser.add_argument(
        "--info",
        action="store_true",
        help="Show detailed update information"
    )
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Automatically update if updates are available"
    )
    
    args = parser.parse_args()
    
    # If no arguments, show help
    if not any([args.check, args.update, args.info, args.auto]):
        parser.print_help()
        return 0
    
    checker = UpdateChecker()
    
    try:
        if args.info:
            # Show detailed information
            info = checker.get_update_info()
            print("\n" + "="*50)
            print("MoA Chatbot - Update Information")
            print("="*50)
            print(f"Current Version:     {info['current_version']}")
            print(f"Remote Version:      {info['remote_version'] or 'unknown'}")
            print(f"Current Branch:      {info['current_branch'] or 'unknown'}")
            print(f"Current Commit:      {info['current_commit'] or 'unknown'}")
            print(f"Latest Commit:       {info['latest_commit'] or 'unknown'}")
            print(f"Has Updates:         {'Yes' if info['has_updates'] else 'No'}")
            print(f"Is Git Repository:   {'Yes' if info['is_git_repo'] else 'No'}")
            print("="*50 + "\n")
            
            if not info['is_git_repo']:
                print("[WARNING] This does not appear to be a git repository.")
                print("  Self-update requires a git repository.")
                return 1
            
            if info['has_updates']:
                print("[!] Updates are available. Run with --update to apply them.")
            else:
                print("[OK] You are up to date!")
            
            return 0
        
        elif args.check:
            # Check for updates
            has_updates, current, latest = checker.check_for_updates()
            
            if current is None:
                print("[ERROR] Could not determine current commit.")
                print("  This may not be a git repository.")
                return 1
            
            print(f"\nCurrent commit: {current[:8]}")
            
            if latest:
                print(f"Latest commit:  {latest[:8]}")
            
            if has_updates:
                print("\n[!] Updates are available!")
                print("  Run 'python update.py --update' to apply them.")
                return 0
            else:
                print("\n[OK] You are up to date!")
                return 0
        
        elif args.auto:
            # Auto-update if available
            has_updates, current, latest = checker.check_for_updates()
            
            if not has_updates:
                print("[OK] You are already up to date!")
                return 0
            
            print(f"\nUpdates available (current: {current[:8] if current else 'unknown'}, latest: {latest[:8] if latest else 'unknown'})")
            print("Applying updates...")
            
            success, message = checker.pull_updates()
            if success:
                print(f"\n[OK] {message}")
                print("\n[!] Note: You may need to restart the application for changes to take effect.")
                return 0
            else:
                print(f"\n[ERROR] {message}")
                return 1
        
        elif args.update:
            # Pull updates
            print("Checking for updates...")
            has_updates, current, latest = checker.check_for_updates()
            
            if not has_updates:
                print("[OK] You are already up to date!")
                return 0
            
            print(f"\nUpdates available:")
            print(f"  Current: {current[:8] if current else 'unknown'}")
            print(f"  Latest:  {latest[:8] if latest else 'unknown'}")
            print("\nPulling updates...")
            
            success, message = checker.pull_updates()
            if success:
                print(f"\n[OK] {message}")
                print("\n[!] Note: You may need to restart the application for changes to take effect.")
                return 0
            else:
                print(f"\n[ERROR] {message}")
                return 1
    
    except KeyboardInterrupt:
        print("\n\nUpdate cancelled by user.")
        return 1
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        if '--debug' in sys.argv:
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

