from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

# create a seachform
class SearchForm(FlaskForm):
    keyword = StringField('Search title',validators = [DataRequired()])
    submit = SubmitField('Search')