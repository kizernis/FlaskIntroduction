import os, sys

# edit your username below
sys.path.append("/home/akizernis/flask/FlaskIntroduction");

sys.path.insert(0, os.path.dirname(__file__))
from app import app as application

# make the secret code a little better
application.secret_key = 'secret241'