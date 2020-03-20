import csv
import os
import requests

from flask import Flask, render_template, request
from modal import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "8pV2dRbipRugYtFReyCnw", "isbns": isbn})
        if(res.status_code == 200):
            res_text = res.json()
            for book in res_text["books"]:
                id=int(book["id"])
                review_count=int(book["reviews_count"])
                average_score=float(book["average_rating"])
                db.execute('INSERT INTO "book" (id, title, author,year,isbn,reviewcount,averagescore) VALUES (:id, :title, :author, :year, :isbn, :review_count, :average_score)',
                            {"id": id, "title": title, "author": author, "year": int(year), "isbn": isbn, "review_count": review_count, "average_score": average_score})
                db.commit()
        
    

if __name__ == "__main__":
    with app.app_context():
        main()
