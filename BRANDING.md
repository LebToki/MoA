# Branding Configuration Guide

This guide explains how to customize the branding elements in MoA Chatbot, similar to Chat-with-Ollama.

## Configuration Options

All branding is configured through environment variables in your `.env` file or directly in `config.py`.

### Required Branding Variables

Add these to your `.env` file:

```env
# Developer/Author Information
DEVELOPER_NAME=Your Name
COMPANY_NAME=Your Company Name
COMPANY_URL=https://yourcompany.com

# GitHub Repository Information
GITHUB_USERNAME=your-github-username
GITHUB_REPO=MoA

# Application Branding
APP_NAME=MoA Chatbot
APP_DESCRIPTION=Mixture of Agents

# Logo (optional)
COMPANY_LOGO=your-logo.png
```

### Branding Elements

1. **Sidebar Header**
   - App name and description
   - Company logo (if provided)
   - Developer name credit

2. **GitHub Community Section** (in sidebar)
   - Star on GitHub
   - Fork & Contribute
   - Report Issues
   - Discussions

3. **Footer Credits** (in chat interface)
   - "Made with ❤️ by [Developer] from [Company]"
   - Company link

4. **Empty State** (home page)
   - Footer credits with company branding

## Logo Setup

1. Place your logo file in `static/images/` directory
2. Supported formats: PNG, JPG, SVG, WEBP
3. Recommended size: 200px width (height auto)
4. Set `COMPANY_LOGO` in `.env` to your logo filename

Example:
```env
COMPANY_LOGO=2tinteractive-logo.png.webp
```

## Default Values

If you don't set these variables, the app will use placeholder values:
- `{{DEVELOPER_NAME}}`
- `{{COMPANY_NAME}}`
- `{{COMPANY_URL}}`
- `{{GITHUB_USERNAME}}`

When placeholders are used, the branding sections will be hidden automatically.

## Quick Setup

1. Copy your logo to `static/images/`
2. Edit `.env` file with your branding information
3. Restart the Flask application
4. Your branding will appear throughout the application

## Example .env Configuration

```env
# Branding
DEVELOPER_NAME=Tarek Tarabichi
COMPANY_NAME=2TInteractive
COMPANY_URL=https://2tinteractive.com
GITHUB_USERNAME=LebToki
GITHUB_REPO=MoA
COMPANY_LOGO=2tinteractive-logo.png.webp
APP_NAME=MoA Chatbot
APP_DESCRIPTION=Mixture of Agents
```

