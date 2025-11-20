# Branding Configuration Guide

## Important: License Requirements

This software is licensed with **branding protection**. The original branding attributions to **Tarek Tarabichi** and **2TInteractive** **MUST be retained** as required by the license. You may add your own branding alongside the required branding, but you cannot remove or replace it.

## Required Branding (Always Displayed)

The following branding is **always displayed** and **cannot be removed**:

- **Developer**: Tarek Tarabichi
- **Company**: 2TInteractive
- **Company URL**: https://2tinteractive.com
- **GitHub**: LebToki/MoA

This branding appears in:
- Sidebar header
- Footer
- Meta tags
- GitHub community links

## Adding Your Own Branding

You can add your own branding **alongside** the required branding by setting these environment variables in your `.env` file:

```env
# Custom Branding (Optional - Added alongside required branding)
CUSTOM_DEVELOPER_NAME=Your Name
CUSTOM_COMPANY_NAME=Your Company Name
CUSTOM_COMPANY_URL=https://yourcompany.com
CUSTOM_COMPANY_LOGO=your-logo.png
```

### How It Works

When you set custom branding:
- **Required branding** (Tarek Tarabichi / 2TInteractive) is always shown first
- **Your custom branding** appears below/alongside it
- Both are displayed together, separated by a divider

### Example Display

**Sidebar:**
```
[2TInteractive Logo]
by Tarek Tarabichi

---
[Your Company Logo]
by Your Name
```

**Footer:**
```
Made with ❤️ by Tarek Tarabichi from 2TInteractive | Your Name from Your Company
```

## Application Configuration

You can customize the application name and description:

```env
APP_NAME=MoA Chatbot
APP_DESCRIPTION=Mixture of Agents
```

## Logo Setup

### Required Logo (2TInteractive)
- Default logo: `static/images/2tinteractive-logo.png.webp`
- This is always displayed

### Custom Logo (Optional)
- Place your logo in: `static/images/`
- Supported formats: PNG, JPG, SVG, WEBP
- Set `CUSTOM_COMPANY_LOGO=your-logo.png` in `.env`

## OG Banner

For social media sharing, add your OG banner:
- Location: `static/images/og_banner.png`
- Recommended size: 1200x630 pixels
- Format: PNG or JPG

**Note**: The OG banner can be customized, but meta tags will still include required branding information.

## License Compliance

When using this software:

✅ **You CAN:**
- Add your own branding alongside required branding
- Customize app name and description
- Add your own logo
- Use in commercial projects
- Modify the code

❌ **You CANNOT:**
- Remove Tarek Tarabichi attribution
- Remove 2TInteractive attribution
- Hide or obscure the required branding
- Replace the required branding with your own

## Examples

### Example 1: Personal Use
```env
CUSTOM_DEVELOPER_NAME=John Doe
CUSTOM_COMPANY_NAME=My Startup
CUSTOM_COMPANY_URL=https://mystartup.com
```

**Result**: Shows "by Tarek Tarabichi from 2TInteractive" AND "by John Doe from My Startup"

### Example 2: Company Use
```env
CUSTOM_COMPANY_NAME=Acme Corp
CUSTOM_COMPANY_URL=https://acmecorp.com
CUSTOM_COMPANY_LOGO=acme-logo.png
```

**Result**: Shows 2TInteractive logo and branding, plus Acme Corp logo and branding

### Example 3: No Custom Branding
If you don't set any custom branding variables, only the required branding is shown.

## Questions?

For questions about branding or licensing:
- Visit: https://2tinteractive.com
- Open an issue: https://github.com/LebToki/MoA/issues

---

**Remember**: The license requires preserving the original branding. This ensures proper attribution while allowing you to add your own branding alongside it.
