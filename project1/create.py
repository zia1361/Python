from modal import *
from flask import Flask, render_template, request
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://zyqwlztajytvod:78db12e0d8ca64d8845c773b7a2dc37a801aefddd8f05ee0907b9b3a769cb615@ec2-3-229-210-93.compute-1.amazonaws.com:5432/d9t1b56ooec3um"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()
    

if __name__ == "__main__":
    with app.app_context():
        main()