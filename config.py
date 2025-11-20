"""
Configuration file for MoA Chatbot branding and settings.
Customize these values to match your branding.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Branding Configuration
# These can be customized per installation
DEVELOPER_NAME = os.environ.get('DEVELOPER_NAME', '{{DEVELOPER_NAME}}')
COMPANY_NAME = os.environ.get('COMPANY_NAME', '{{COMPANY_NAME}}')
COMPANY_URL = os.environ.get('COMPANY_URL', '{{COMPANY_URL}}')
GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME', '{{GITHUB_USERNAME}}')
GITHUB_REPO = os.environ.get('GITHUB_REPO', 'MoA')

# Logo Configuration
# Place your logo file in static/images/ directory
# Supported formats: PNG, JPG, SVG, WEBP
COMPANY_LOGO = os.environ.get('COMPANY_LOGO', '2tinteractive-logo.png.webp')  # Default logo path

# Application Configuration
APP_NAME = os.environ.get('APP_NAME', 'MoA Chatbot')
APP_DESCRIPTION = os.environ.get('APP_DESCRIPTION', 'Mixture of Agents')

