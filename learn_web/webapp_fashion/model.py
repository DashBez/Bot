from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Marka = db.Column(db.String, nullable=False)
    Size = db.Column(db.Integer, nullable=False)
    Condition = db.Column(db.String, nullable=False)
    Description = db.Column(db.String, nullable=False)
    Price = db.Column(db.String, nullable=False)
    Seller = db.Column(db.String, nullable=False)
    Image = db.Column(db.String, nullable=False)
    
    

    def __repr__(self):
        return '<INFO {} {}>'.format(self.Marka)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

