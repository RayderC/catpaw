from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates")


def login():
    return render_template("login.html")
