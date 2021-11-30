from myapp import db
from myapp import login
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import current_user


classrooms = db.Table('classrooms',
        db.Column('classrom_id', db.Integer, db.ForeignKey('classroom.id'), primary_key=True),
        db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)
class Chat(db.Model):
        __tablename__ = "chat"
        id = db.Column(db.Integer, primary_key=True)
        classroom_id = db.Column(db.Integer, db.ForeignKey("classroom.id"))
        message = db.Column(db.String(10000), index = True)
        sender = db.Column(db.String(64), index = True)
        
        def __init__(self, sender, message):
                ''' Creates a new chat object
                '''
                self.sender = sender
                self.message = message
                
        
                                 
class Classroom(db.Model):
    '''
        Classroom database structure used for storing classrooms in database
    '''
    __tablename__ = "classroom"
    messages = db.relationship("Chat", back_populates = "classroom")
        
    def __init__(self, name):
        '''
            Parameters:
                name (string): The name of the classroom object, which other users can search for
        '''
        self.name = name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)    


class User(db.Model):
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

        self.username = username
        self.email = email
        self.set_password(password)
        self.public = True

    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = "user"
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    public = db.Column(db.Boolean, index=True)

    classrooms = db.relationship('Classroom', secondary=classrooms, lazy="subquery",
            backref=db.backref('users', lazy=True))

    password_hash = db.Column(db.String(128))
    
    def check_password(self, password):
        '''
            Uses werkzeug_security function check_password_hash to compare password hash to user entered password when logging in

            parameters:
                password (string): password user entered to compare against what is stored in db
        '''
        return check_password_hash(self.password_hash, password)
   
    #necessary properties and methods for User objects, required by flask_login
    is_active = True
    is_anonymous = False
    is_authenticated = True
    
    def get_id(self):
        '''
            Function required by flask_login for users
        '''
        return self.id

    def getPublic(self):
        '''
            Checks if user account is public in database for user search

            returns:
                (boolean): Whether the user is public or not
        '''
        return self.public

    def setPublic(self, public):
        '''
            Sets user account to public/private in settings

            parameters:
                public (boolean): Value of public that user set
        '''
        current_user.public = public
        db.session.commit()

    @staticmethod
    def check_valid_credentials(username, email, password, reenterPassword):
        
        '''
            Checks to make sure that new user credentials are valid
            
            parameters:
                username (string): Checks to make sure username is unique, otherwise throws flash error
                email (string): Checks to make sure email is unique
                password (string): Password of the user
                reenterPassword (string): Checks to make sure password and reenterPassword are equal

        '''

        credentials_valid = True
        error_message = ""

        if User.query.filter_by(username=username).first() is not None:
            credentials_valid = False
            error_message = "Username taken!"

        elif User.query.filter_by(email = email).first() is not None:
            credentials_valid = False
            error_message = "Email taken!"

        elif password != reenterPassword:
            credentials_valid = False
            error_message = "Password and reenter password did not match!"

        return (credentials_valid, error_message)

    def set_password(self, password):
        '''
            Encrypts password and stores their password hash in the database

            parameters:
                password (string): Unencrypted password to be stored in database
        '''
        self.password_hash = generate_password_hash(password)

    
    @login.user_loader
    def load_user(id):

        '''
            Assigns the current user for logged in

            parameters:
                id (int): ID of the user to login

            returns:
                (User): User object queried from database to be logged in
        '''


        return User.query.get(int(id))


