from myapp import db

class User(db.Model):
    '''
        User database structure for storing into database
    '''

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)

    password_hash = db.Column(db.String(128))
