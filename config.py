import os


class Config(object):
    """
    Configuration
    """
    # Reads environmental variable when none is given uses static value
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-nerver-guess-this'
    TEMPLATE_DIR = os.environ.get('TEMPLATE_DIR') or os.path.abspath(
        'app/templates')