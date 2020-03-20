
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    useremail = db.Column(db.String(100), nullable=False)
    userpassword = db.Column(db.String(100), nullable=False)

class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.String(100), nullable=False)
    reviewcount = db.Column(db.Integer, nullable=False)
    averagescore = db.Column(db.Float, nullable=False)   

class Review(db.Model):
    __tablename__ = "review"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    review = db.Column(db.String(100), nullable=False)
    bokid = db.Column(db.Integer, nullable=False, )
