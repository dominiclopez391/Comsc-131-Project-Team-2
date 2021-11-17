from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_login import current_user

class LoginForm(FlaskForm):
    '''
        Form which allows users to login
    '''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    '''
        Form which allows users to register for a new account
    '''

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    reenterPassword = PasswordField('Reenter Password', validators=[DataRequired()])

    submit = SubmitField("Submit")

class OptionsForm(FlaskForm):
    '''
	Form which allows user to change accounts settings
    '''
    public = BooleanField('Public')
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
	
	search = StringField("Search for user")
	submit = SubmitField("Submit")






        

