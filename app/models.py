from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    currency = db.Column(db.String(25))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))   
    wallet = db.relationship('Wallet',backref='users',lazy='dynamic') 
    transaction = db.relationship('Transaction',backref='users',lazy='dynamic') 
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'
    
class Wallet(db.Model):
    __tablename__= "wallets"
    id = db.Column(db.Integer,primary_key = True)
    total = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='SET NULL'),nullable = True)
    transaction = db.relationship('Transaction',backref='wallets',lazy='dynamic') 
    
 
    def __repr__(self):
        return f'Wallet{self.id}'
    
class Transaction(db.Model):
    __tablename__="transactions"
    id = db.Column(db.Integer,primary_key = True)
    type = db.Column(db.String(255))
    amount = db.Column(db.Float)
    time=db.Column(db.DateTime(),default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='SET NULL'),nullable = True)
    wallet_id = db.Column(db.Integer, db.ForeignKey('wallets.id',ondelete='SET NULL'),nullable = True)
    
    def __repr__(self):
        return f'Transaction{self.type}'
    
