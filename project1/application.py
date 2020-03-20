import os
import csv
import json

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests

app = Flask(__name__)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://zyqwlztajytvod:78db12e0d8ca64d8845c773b7a2dc37a801aefddd8f05ee0907b9b3a769cb615@ec2-3-229-210-93.compute-1.amazonaws.com:5432/d9t1b56ooec3um")
db = scoped_session(sessionmaker(bind=engine))




@app.route("/")
def index():
    return render_template("login.html")

ISBN = []
TITLE = []
AUTHOR = []
YEAR = []
@app.route("/Dashboard", methods=["Post","Get"])
def login():

    password = request.form.get("password")
    email = request.form.get("email")
    print(password)
    print(email)
    
    if(password is not None and email is not None):
        user = db.execute('SELECT * FROM "user" WHERE userpassword = :userpassword AND useremail = :useremail',{"userpassword":password,"useremail":email}).fetchone()
        print(user)
        if(user is not None):
            b = open("books.csv")
            reader = csv.reader(b)
            for isbn,title,author,year in reader:
                ISBN.append(isbn)
                TITLE.append(title)
                AUTHOR.append(author)
                YEAR.append(year)
            return render_template("Dashboard.html", ISBN=ISBN, TITLE=TITLE, AUTHOR=AUTHOR, YEAR=YEAR)
        else:
           return render_template("signup.html")       

    else:
        return render_template("login.html")


@app.route("/Signup", methods=["Post"])
def signup():
    name=request.form.get("name")
    email=request.form.get("email")
    password=request.form.get("password")
    user = db.execute('SELECT * FROM "user" WHERE useremail = :useremail',{"useremail":email}).fetchone()
    if(user is None):
        data=db.execute('SELECT id FROM "user" ORDER BY id DESC LIMIT 1').fetchone()
        db.commit()
        if(data is not None):
            db.execute('INSERT INTO "user" (id,username,useremail,userpassword) VALUES (:id,:name,:email,:password)',{"id":data[0]+1,"name":name,"email":email,"password":password})
            db.commit()
        else:
            db.execute('INSERT INTO "user" (id,username,useremail,userpassword) VALUES (:id,:name,:email,:password)',{"id":1,"name":name,"email":email,"password":password})
            db.commit()                
        b = open("books.csv")
        reader = csv.reader(b)
        for isbn,title,author,year in reader:
            ISBN.append(isbn)
            TITLE.append(title)
            AUTHOR.append(author)
            YEAR.append(year)
        return render_template("Dashboard.html", ISBN=ISBN, TITLE=TITLE, AUTHOR=AUTHOR, YEAR=YEAR)                    
    else:
        return "Email Already exists try with other one"    


@app.route("/Search",methods=["Post"])
def search():
    isbn = request.form.get("isbn")
    title = request.form.get("title")
    author = request.form.get("author")
    print("??????????")
    print(isbn)
    print(title)
    print(author)
    BOOKS = []
    books = db.execute('SELECT * FROM "book" WHERE isbn = :isbn OR title = :title OR author = :author',{"isbn": isbn, "title": title, "author": author}).fetchall()
    print(books)
    if(books is not None):
        for book in books:
            getbook = f"{book.title}"
            BOOKS.append(getbook)
            print(f"{book.title}")
        print(BOOKS)    
        return render_template("books.html",Books=BOOKS)    
    else:
        return "No Book found"


@app.route("/Detail/<bookname>")
def detail(bookname):
    print(bookname)
    data = db.execute('SELECT * FROM "book" WHERE title = :title',{"title": bookname}).fetchone()
    if(data is not None):
        return render_template("Detail.html",booktitle=data.title, bookid=data.id, author=data.author, year=data.year, isbn=data.isbn, reviewscount=data.reviewcount,averagescore=data.averagescore)
    else:
        return "No Data Found"    