# CLAUDE.md — Student Grade Calculator

## Project Overview
A Python library for calculating student grades, GPA,
and academic performance summaries.
Used by a fictional online learning platform.

## Coding Standards
- Use Python 3.10+
- Follow PEP 8 style guidelines
- snake_case for all names
- Docstrings on every function
- Type hints on all parameters and return values
- f-strings for all string formatting
- Raise ValueError with a clear message for invalid inputs
- No global variables

## Testing Standards
- Use pytest for all tests
- Test file: tests/test_grades.py
- Run with: PYTHONPATH=. pytest tests/ -v
- Every function must have at least one happy path test
  and at least one error test using pytest.raises()
- When adding a new function, always add it to the
  import statement at the top of test_grades.py

## CI/CD Rules (enforced by GitHub Actions)
- All PRs are automatically reviewed by Claude Code
- Claude Code will flag:
    BLOCKING: missing type hints on any function
    BLOCKING: missing docstring on any function
    BLOCKING: no tests for a new function
    BLOCKING: function longer than 20 lines
    WARNING:  magic numbers without named constants
    WARNING:  more than 3 parameters on a function

## Project Structure
```
student-grade-calculator/
├── CLAUDE.md
├── conftest.py            ← pytest path fix (do not delete)
├── grades.py              ← Core grading logic
├── tests/
│   └── test_grades.py
└── .github/
    └── workflows/
        └── claude_review.yml
```

## Off-Limits
- Do NOT modify CLAUDE.md
- Do NOT modify claude_review.yml without team approval
