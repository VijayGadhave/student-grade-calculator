# conftest.py
# Adds the project root to Python path so pytest can find grades.py
# Required for CI/CD — do not delete this file

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
