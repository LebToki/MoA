# Contributing to MoA Chatbot

Thank you for your interest in contributing to MoA Chatbot! We welcome contributions from the community and appreciate your efforts to improve this project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How to Contribute

### Reporting Issues

**We use GitHub Issues (not Discussions) for all community interactions** to ensure maximum visibility and benefit for the entire community.

When reporting issues:

1. **Check existing issues** - Make sure the issue hasn't already been reported
2. **Use clear titles** - Descriptive titles help others find and understand issues
3. **Provide details** - Include:
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Screenshots if applicable
   - Error messages or logs

### Feature Requests

Have an idea for a new feature? Open a GitHub Issue with:
- Clear description of the feature
- Use case and benefits
- Potential implementation approach (if you have ideas)

### Submitting Pull Requests

1. **Fork the repository**
2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**:
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation if needed
   - **IMPORTANT**: Preserve branding attributions (see License section below)

4. **Test your changes**:
   - Test on Windows if possible
   - Verify no breaking changes
   - Check browser compatibility

5. **Commit your changes**:
   ```bash
   git commit -m "Description of your changes"
   ```

6. **Push and create Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Submit Pull Request** with:
   - Clear description of changes
   - Reference related issues
   - Screenshots if UI changes

## License and Branding Requirements

**IMPORTANT**: This project uses a custom license that requires preserving branding attributions.

### What You MUST Do:

✅ **Retain Branding**: Keep attributions to Tarek Tarabichi and 2TInteractive in:
- README files
- Documentation
- User interfaces (footer, about sections)
- Code comments where appropriate

✅ **Add Your Attribution**: You can add your own branding alongside the required attributions

### What You CANNOT Do:

❌ Remove or obscure the original branding
❌ Modify copyright notices
❌ Remove attribution to Tarek Tarabichi or 2TInteractive

### Example of Proper Attribution:

```markdown
Made with ❤️ by Tarek Tarabichi from 2TInteractive

[Your additional attribution here]
```

## Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and single-purpose

### Testing

- Test your changes thoroughly
- Test on Windows (if possible) - this is a Windows-friendly project
- Verify UI changes in multiple browsers
- Check for console errors

### Documentation

- Update README.md if adding new features
- Add comments for complex logic
- Update CHANGELOG.md for significant changes
- Keep inline documentation up to date

## Technical Notes

### API Compatibility

This project is based on **Groq's API**, not the original Together API. When contributing:
- Ensure compatibility with Groq's specifications
- Test API integrations thoroughly
- Follow Groq's rate limits and best practices

### Windows Compatibility

This project prioritizes Windows compatibility:
- Test on Windows if possible
- Use cross-platform paths (`os.path.join`)
- Consider Windows-specific issues (path separators, etc.)

## Questions?

- **Issues**: Open a GitHub Issue for questions, bugs, or feature requests
- **License Questions**: Contact https://2tinteractive.com
- **Commercial Licensing**: For commercial use inquiries, visit https://2tinteractive.com

## Recognition

Contributors will be:
- Listed in the project's contributors (if desired)
- Credited in release notes for significant contributions
- Appreciated by the entire community!

Thank you for contributing to MoA Chatbot and helping make it better for everyone! 🎉

---

**Remember**: All community interactions should go through GitHub Issues to ensure the whole community benefits from the discussions and solutions.
