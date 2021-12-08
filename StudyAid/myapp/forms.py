from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, optional
from flask_login import current_user

class NotesForm(FlaskForm):
    '''
        Form which allows users to create their own notes
    '''
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[optional()])

    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    '''
        Form which allows users to login
    '''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField("Submit")

class QuestionForm(FlaskForm):
	'''
		Form which allows user to post questions in classroom
	'''
	question = StringField('Question', validators=[DataRequired()])
	submit = SubmitField('Submit')

class AnswerForm(FlaskForm):
	'''
		Form which allows user to answer questions in classroom
	'''
	answer = StringField("Answer", validators=[DataRequired()])
	submit = SubmitField('Submit')


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

class ShareNotesForm(FlaskForm):
    user = StringField("User to send to", validators=[DataRequired()])
    note = SelectField("Note")

    submit = SubmitField("Submit")

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
        
class PomodoroTimerForm(FlaskForm):
    study_time = IntegerField('Study Time', validators = [DataRequired()])
    start_button = SubmitField('Start')

