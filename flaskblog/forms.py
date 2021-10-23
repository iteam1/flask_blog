from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed # filefield for upload file, file allowed for avlidate file
from wtforms import StringField, PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Length, Email,EqualTo,ValidationError
from flaskblog.models import User
from flask_login import current_user # for account udate class


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

# create a update account form
class UpdateAccountForm(FlaskForm):
    username = StringField('Username',validators= [Length(min= 2,max =20)])
    email = StringField('Email', validators = [Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    #function to validate username
    def validate_username(self,username):
        if username.data != current_user.username: # if there is change in username
            user = User.query.filter_by(username = username.data).first()
            if user: # if there is any user
                raise ValidationError(f'The username {username.data} is already taken, Please try another!')

    def validate_email(self,email):
        if email.data != current_user.email: # if there is change in email
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError(f'The email {email.data} is already taken, Please try another!')