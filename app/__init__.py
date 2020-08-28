from flask import Flask
from config import Config


crm = Flask(__name__)
crm.config.from_object(Config)

template_dir = crm.config['TEMPLATE_DIR']
crm.template_folder = template_dir

from app import routes