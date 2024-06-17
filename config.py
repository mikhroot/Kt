import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://username:password@localhost/yourdatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_DIR = '/path/to/logs'
    LOG_EXT = '.log'
