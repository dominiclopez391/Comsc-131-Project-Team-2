### class Note(db.Model):
	'''
	Note database structure for storing notes in database
	'''
	
	def __init__(self, title, body): 
	
	'''
		Parameters:
			title (string): Title of note
			body (string): Body of note
		timestamp (string): Current time
	'''

### class Chat(db.Model):

	'''
	Chat database structure for adding comments to database
	'''

	def __init__(self, sender, message)

	'''
		Parameters:
			sender (string): Username of the user that sent this message
			message (string): Message the user sent to the classroom chat
	'''

### class Questions(db.Model):

	'''
	Database structure used for storing questiosn in classroom in database
	'''

	def __init__(self, question):
	
	'''
		Parameters:
			question (string): Inputted question for classroom

	def answerQuestion(self, answer):

	'''
		Parameters: 
			answer (string): Inputted answer for question in classroom
	'''

	id: Creates id column in database

	question: Creates question column in database

	answer: Creates answer column in database

	asker: Creates asker column in database

	answerer: Creates answerer column in database

### class Classroom(db.Model):


	'''
        Classroom database structure used for storing classrooms in database
	'''


	def __init__(self, name)


	'''
            Parameters:
                name (string): The name of the classroom object, which other users can search for        
	'''


	id: Creates id column in database


	name: creates name column in database


### class User(db.Model):


	'''
        User database structure for storing into database
	'''


	def __init__(self, username, email, password):


	'''
            Parameters:
                Username (string): Username of the user, stored as a column in db
                Password (string): Password of the user, unencrypted, stored as a column
                email (string): Email of the user, stored as a column
	'''


	id: Creates id column in database


	username: Creates username column in database


	email: Creates email column in database


	public: Creates public column in database


	classrooms: Many to many relationship between Classroom database and User database


	password_hash: Creates password_hash column in database


	def check_password(self, password):


	'''
            Uses werkzeug_security function check_password_hash to compare password hash to user entered password when logging in

            parameters:
                password (string): password user entered to compare against what is stored in db
	'''


	Necessary properties and methods for User objects, required by flask_login


		is_active = True


		is_anonymous = False


		is_authenticated = True


	def get_id(self):


	'''
            Function required by flask_login for users
	'''



	def getPublic(self):


	'''
            Checks if user account is public in database for user search

            returns:
                (boolean): Whether the user is public or not
	'''


	def setPublic(self, public):


	'''
            Sets user account to public/private in settings

            parameters:
                public (boolean): Value of public that user set
	'''


		
	def check_valid_credentials(username, email, password, reenterPassword):


	'''
            Checks to make sure that new user credentials are valid

            parameters:
                username (string): Checks to make sure username is unique, otherwise throws flash error
                email (string): Checks to make sure email is unique
                password (string): Password of the user
                reenterPassword (string): Checks to make sure password and reenterPassword are equal

	'''


	def set_password(self, password):


        '''
            Encrypts password and stores their password hash in the database

            parameters:
                password (string): Unencrypted password to be stored in database
        '''


	def load_user(id):


        '''
            Assigns the current user for logged in

            parameters:
                id (int): ID of the user to login

            returns:
                (User): User object queried from database to be logged in
        '''
