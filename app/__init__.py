from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Init Flask App
crm = Flask(__name__)
# Load Config Object from config.py-module
crm.config.from_object(Config)
# Set Template Directory
crm.template_folder = crm.config['TEMPLATE_DIR']
# Init SQLAlchemy Extension
db = SQLAlchemy(crm)
# Init Migrate extension for eventual database migrations
migrate = Migrate(crm, db)

from app import routes, models
