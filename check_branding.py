"""Quick script to verify branding configuration"""
from app import app
import config

print("=" * 50)
print("MoA Chatbot - Branding Configuration Check")
print("=" * 50)
print()
print("Current Branding Values:")
print(f"  Developer Name: {config.DEVELOPER_NAME}")
print(f"  Company Name:   {config.COMPANY_NAME}")
print(f"  Company URL:    {config.COMPANY_URL}")
print(f"  GitHub:         {config.GITHUB_USERNAME}/{config.GITHUB_REPO}")
print(f"  App Name:       {config.APP_NAME}")
print(f"  App Description: {config.APP_DESCRIPTION}")
print(f"  Company Logo:   {config.COMPANY_LOGO}")
print()
print("Template Variables (available in all templates):")
with app.app_context():
    from flask import render_template_string
    template_vars = {
        'developer_name': config.DEVELOPER_NAME,
        'company_name': config.COMPANY_NAME,
        'company_url': config.COMPANY_URL,
        'github_username': config.GITHUB_USERNAME,
        'github_repo': config.GITHUB_REPO,
        'company_logo': config.COMPANY_LOGO,
        'app_name': config.APP_NAME,
        'app_description': config.APP_DESCRIPTION
    }
    for key, value in template_vars.items():
        print(f"  {key}: {value}")
print()
print("=" * 50)
print("Branding Status:")
if config.COMPANY_NAME != '{{COMPANY_NAME}}':
    print("✓ Company branding configured")
else:
    print("⚠ Company branding not configured (using placeholder)")
    
if config.DEVELOPER_NAME != '{{DEVELOPER_NAME}}':
    print("✓ Developer name configured")
else:
    print("⚠ Developer name not configured (using placeholder)")
    
if config.GITHUB_USERNAME != '{{GITHUB_USERNAME}}':
    print("✓ GitHub information configured")
else:
    print("⚠ GitHub information not configured (using placeholder)")
print("=" * 50)
print()
print("Server: http://127.0.0.1:5000/")
print("Please refresh your browser (Ctrl+F5) to see the branding!")

