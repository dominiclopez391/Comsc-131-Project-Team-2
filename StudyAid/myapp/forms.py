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

class DeleteForm(FlaskForm):
    '''
        Form which allows users to delete their account
    '''

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    reenterPassword = PasswordField('Reenter Password', validators=[DataRequired()])

    submit = SubmitField("Submit")
    confirmation = BooleanField('Are you sure')

    
class SearchForm(FlaskForm):
	'''
	Form which allows users to search for other users
	'''
	
	search = StringField("Search for user")
	submit = SubmitField("Submit")


class SearchClassroomsForm(FlaskForm):
    '''
        Form which allows user to search for different classrooms
    '''

    name = StringField('Classroom Name')
    submit = SubmitField('Search')

class CreateClassroomForm(FlaskForm):
    '''
        Form which allows a user to create a new classroom.
    '''

    name = StringField('New Classroom Name')
    submit = SubmitField('Create')

class MessageForm(FlaskForm):
    '''
        Form for users when they message each other
    '''
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField("Submit")
        

