import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'singlepage.db')
    TIMEPERIOD = os.environ.get('TIMEPERIOD', 5)
    SERIAL_PORT = os.environ.get('SERIAL_PORT', 'COM3')
