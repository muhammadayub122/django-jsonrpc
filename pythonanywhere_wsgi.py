# PythonAnywhere WSGI configuration
import os
import sys

# Add your project directory to the sys.path
project_home = '/home/yourusername/yourprojectname'  # Replace with your actual path
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable to tell django where to find your settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Import django
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()