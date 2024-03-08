from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import login
import signup

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'mykey'
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login")
def user_login():
    return login.login()

@app.route("/signup")
def user_signup():
    return signup.signup()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


