from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flasgger import Swagger
from flaskblog.config import Config

# create a extension mail server for multi app
mail = Mail()

# create a extension database for multi app
db = SQLAlchemy()

# create a extension bcrypt for hash password for multi app 
bcrypt = Bcrypt()

# create a login manager extension for multi app 
login_manager = LoginManager()
login_manager.login_view = 'users.login' # if route required to login by @login_required, show 'login' page
login_manager.login_message_category = 'info'

#define a template Info Object
template = {
    "swagger":"2.0",
    "info":{
        "title":"FlaskBlog Backend",
        "description":"FlaskBlog API documments",
        "contact":{
            "name": "LocChuong",
            "url": "http://www.swagger.io/support",
            "email": "locchuong123@gmail.com"
        },
        "version":"0.0.1",
        "schemes":['http','https']
    }
}

# create a login manager extension for multi app 
swagger = Swagger(template = template)

def create_app(config = Config):
    # create app
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)   
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    swagger.init_app(app)

    # import all routes
    from flaskblog.users.routes import users # users blueprint instance
    from flaskblog.posts.routes import posts # posts blueprint instance
    from flaskblog.main.routes import main # main blueprint instance
    from flaskblog.errors.handlers import errors # handle errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

