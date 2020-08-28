import os

basedir = os.path.abspath((os.path.dirname(__file__)))


class Config(object):
    """
    Configuration
    """
    # Reads environmental variable when none is given uses static value
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-nerver-guess-this'
    # Sets the template directory
    TEMPLATE_DIR = os.environ.get('TEMPLATE_DIR') or os.path.abspath(
        'app/templates')
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'crm.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
