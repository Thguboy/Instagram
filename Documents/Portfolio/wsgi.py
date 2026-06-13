import sys
import os

# PythonAnywhere WSGI entry point.
# Automatically resolves the project directory — works both locally
# and on PythonAnywhere without manual path edits.
project_home = os.path.dirname(os.path.abspath(__file__))
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import the Flask app object. PythonAnywhere expects a variable named `application`.
from app import app as application  # noqa: F401
