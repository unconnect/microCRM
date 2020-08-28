from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


crm = Flask(__name__)
crm.config.from_object(Config)
crm.template_folder = crm.config['TEMPLATE_DIR']
db = SQLAlchemy(crm)
migrate = Migrate(crm, db)

from app import routes, models
