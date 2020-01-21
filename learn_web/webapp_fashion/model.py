from flask_sqlalchemy import SQLAlchemy
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
    Counter = db.Column(db.Integer, nullable=False)
    
    

    def __repr__(self):
        return '<INFO {} {}>'.format(self.Marka)

"""
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)
"""