"""
Configuration file for MoA Chatbot branding and settings.

IMPORTANT: This software is licensed with branding protection.
The original branding (Tarek Tarabichi and 2TInteractive) MUST be retained
as required by the license. You may add your own branding alongside it.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# REQUIRED BRANDING - Cannot be removed per license
# These are always displayed and required by the license
REQUIRED_DEVELOPER_NAME = 'Tarek Tarabichi'
REQUIRED_COMPANY_NAME = '2TInteractive'
REQUIRED_COMPANY_URL = 'https://2tinteractive.com'
REQUIRED_GITHUB_USERNAME = 'LebToki'
REQUIRED_GITHUB_REPO = 'MoA'

# OPTIONAL CUSTOM BRANDING - Can be added alongside required branding
# Set these in .env to add your own branding (will appear alongside required branding)
CUSTOM_DEVELOPER_NAME = os.environ.get('CUSTOM_DEVELOPER_NAME', '')
CUSTOM_COMPANY_NAME = os.environ.get('CUSTOM_COMPANY_NAME', '')
CUSTOM_COMPANY_URL = os.environ.get('CUSTOM_COMPANY_URL', '')
CUSTOM_COMPANY_LOGO = os.environ.get('CUSTOM_COMPANY_LOGO', '')

# Legacy support - map to required branding
# These are kept for backward compatibility but always use required values
DEVELOPER_NAME = REQUIRED_DEVELOPER_NAME
COMPANY_NAME = REQUIRED_COMPANY_NAME
COMPANY_URL = REQUIRED_COMPANY_URL
GITHUB_USERNAME = REQUIRED_GITHUB_USERNAME
GITHUB_REPO = os.environ.get('GITHUB_REPO', REQUIRED_GITHUB_REPO)

# Logo Configuration
# Default logo is 2TInteractive logo (required branding)
# You can add your own logo via CUSTOM_COMPANY_LOGO
COMPANY_LOGO = os.environ.get('COMPANY_LOGO', '2tinteractive-logo.png.webp')

# Application Configuration
APP_NAME = os.environ.get('APP_NAME', 'MoA Chatbot')
APP_DESCRIPTION = os.environ.get('APP_DESCRIPTION', 'Mixture of Agents')

