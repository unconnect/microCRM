import os


class Config(object):
    """
    Configuration
    """
    # Reads enviromental variable or
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-nerver-guess-this'