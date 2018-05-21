from flask import Flask
from config import Config
import serial
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_wtf.csrf import CSRFProtect
from flask_restful import Resource, Api
#from flask_restful_swagger import swagger


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, name='RGB', template_mode='bootstrap3')
api = Api(app)
csrf = CSRFProtect(app)
#api = swagger.docs(Api(app), apiVersion='0.1')
#ser  = None
try:
    ser = serial.Serial(app.config.get('SERIAL_PORT'), 9600, write_timeout=3)
except Exception as e:
    print(e)
    ser = None


from app import routes, models, modelviews, api_routes
