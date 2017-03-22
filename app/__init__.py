from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_assets import assets, Environment

# import ssl
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# context.load_cert_chain('phongmachannghia.com.crt', 'phongmachannghia.com.key')



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


moment = Moment(app)
moment.init_app(app)

assets = Environment(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views, models
