import os


class Config(object):
    """
    Configuration
    """
    # Reads environmental variable when none is given uses static value
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-nerver-guess-this'
