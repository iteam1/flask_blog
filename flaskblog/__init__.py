from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# create app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a745e902cf3b161c90630fc2ae745351'

# setup mail server
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "xxx"
app.config['MAIL_PASSWORD'] = "xxx"
mail = Mail(app)

# connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# bcrypt for hash password
bcrypt = Bcrypt(app)

# create a login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login' # if route required to login by @login_required, show 'login' page
login_manager.login_message_category = 'info'

# import all routes
from flaskblog import routes