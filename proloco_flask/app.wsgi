#! /usr/bin/python3.9

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/carlo/proloco_flask/proloco_flask/flask_upload_files.py')
from my_flask_app import app as application
application.secret_key = 'proloco'
