# Contributing to Agents Course

Thank you for your interest in contributing to the Agents Course! This document provides guidelines for contributing to this educational repository.

## How to Contribute

### For Students

As a student working through the course:

1. **Complete the Labs**: Work through each module's exercises
2. **Share Your Solutions**: After completing a module, consider sharing your approach
3. **Report Issues**: If you find bugs or unclear instructions, open an issue
4. **Suggest Improvements**: Ideas for new labs or better explanations are welcome

### For Instructors/Contributors

1. **Fork the Repository**
   ```bash
   git fork https://github.com/Drmcoelho/Agents.git
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow the existing code style
   - Add tests for new features
   - Update documentation as needed

4. **Test Your Changes**
   ```bash
   make test
   make lint
   ```

5. **Submit a Pull Request**

## Adding New Labs

When adding a new lab:

1. Create the lab file in the appropriate module's `labs/` directory
2. Add corresponding tests in `tests/`
3. Create a solution in `solutions/`
4. Update the module's `gabarito.json` with hints
5. Update the module's README

### Lab Template

```python
"""
Lab X: Title
Brief description of what students will learn.
"""

class LabExercise:
    """Lab exercise class."""
    
    def exercise_1_name(self, param: Type) -> ReturnType:
        """
        Exercise 1: Description
        
        TODO: Implement this method to:
        1. Step one
        2. Step two
        3. Step three
        
        Args:
            param: Description
            
        Returns:
            Description
        """
        # YOUR CODE HERE
        pass
```

## Adding New Modules

To add a new module:

1. Create directory structure:
   ```
   module_name/
   ├── labs/
   ├── tests/
   ├── solutions/
   ├── README.md
   ├── gabarito.json
   └── __init__.py
   ```

2. Update the Makefile to include the new module
3. Add CI tests in `.github/workflows/ci.yml`
4. Update the main README

## Code Style

- **Python**: Follow PEP 8, use Black for formatting
- **Line Length**: 88 characters (Black default)
- **Docstrings**: Use Google-style docstrings
- **Type Hints**: Include type hints where helpful

## Testing

- Write tests for all new functionality
- Use pytest for testing
- Aim for high test coverage
- Mock external API calls in tests

## Documentation

- Keep README files up to date
- Add docstrings to all functions and classes
- Include usage examples where helpful
- Update the main README for significant changes

## Gabarito (Answer Key) System

When adding solutions:

1. Create solution files in the `solutions/` directory
2. Add entries to `gabarito.json`:
   ```json
   {
     "exercise_name": {
       "description": "Brief description",
       "hints": [
         "Hint 1",
         "Hint 2",
         "Hint 3"
       ],
       "solution_file": "solution_filename.py",
       "target_file": "labs/lab_filename.py"
     }
   }
   ```

## Commit Messages

Use clear, descriptive commit messages:

- `feat: Add new lab for X`
- `fix: Correct issue in Y`
- `docs: Update README for Z`
- `test: Add tests for W`
- `refactor: Improve code structure in V`

## Pull Request Process

1. Ensure all tests pass
2. Update documentation
3. Describe your changes clearly in the PR description
4. Link any related issues
5. Wait for review and address feedback

## Questions?

- Open an issue for questions about contributing
- Check existing issues and PRs first
- Be respectful and constructive in all interactions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
