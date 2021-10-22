from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Length, Email,EqualTo,ValidationError
from flaskblog.models import User

# create a registration form inherited from flask form
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators= [DataRequired(),Length(min= 2,max =20)])
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    #function to validate username
    def validate_username(self,username):
        user = User.query.filter_by(username = username.data).first()
        if user: # if there is any user
            raise ValidationError(f'The username {username.data} is already taken, Please try another!')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError(f'The email {email.data} is already taken, Please try another!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators = [DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')