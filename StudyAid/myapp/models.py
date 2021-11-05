from myapp import db
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    '''
        User database structure for storing into database
    '''
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)

    password_hash = db.Column(db.String(128))

    @staticmethod
    def check_valid_credentials(username, email, password, reenterPassword):

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
        self.password_hash = generate_password_hash(password)

            


