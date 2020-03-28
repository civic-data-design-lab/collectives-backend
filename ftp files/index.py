import os
import sys


CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
PROJECT_DIR = os.path.dirname(CURRENT_DIR)

# Add project top-dir to path (since it has no __init__.py)
sys.path.append(PROJECT_DIR)

# Add virtualenv to path
sys.path.append(PROJECT_DIR + '/collectives/lib/python3.8/site-packages/')

# Export the Flask app object from the project as wsgi application object
from run import app as application
