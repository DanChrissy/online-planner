from . import db
from sqlalchemy import Column, ForeignKey  

class UserAccount(db.Model):
    
    __tablename__ = 'user'
    
    accountId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    date_birth = db.Column(db.Date)
    email = db.Column(db.String(80))
    
    def __init__(self, accountId, username, password, first_name, last_name, email, date_birth):
        """This is the constructor for the User class"""
        self.accountId = accountId
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_birth = date_birth
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    def get_id(self):
        try:
            return unicode(self.accountId)  # python 2 support
        except NameError:
            return str(self.accountId)  # python 3 support

    def __repr__(self):
        return "<Account created by {0} {1}>".format(self.first_name,self.last_name)

class UserProfile(db.Model):
    
    __tablename__ = 'profile'
    
    accountId = Column(ForeignKey('user.accountId', onupdate='CASCADE', ondelete='CASCADE'), nullable=False, primary_key = True) 
    gender = db.Column(db.String(6))
    weight = db.Column(db.Integer)
    meal = db.Column(db.String(100))
    
    def __init__(self, accountId, gender, weight, meal):
        
        self.accountId = accountId
        self.gender = gender
        self.weight = weight
        self.meal = meal
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    def get_id(self):
        try:
            return unicode(self.accountId)  # python 2 support
        except NameError:
            return str(self.accountId)  # python 3 support

    def __repr__(self):
        return "<Profile belongs to user with Account Id: {0} >".format(self.accountId)
