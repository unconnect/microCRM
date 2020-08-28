from flask import Flask
from config import Config

crm = Flask(__name__)
crm.config.from_object(Config)

from app import routes