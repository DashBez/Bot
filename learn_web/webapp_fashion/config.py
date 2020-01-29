import os
basedir = os.path.abspath(os.path.dirname(__file__)) 

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, '..', 'webapp_fashion.db')

SECRET_KEY = "aasdfghjkl45678909jhgcvbnm"