from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates")


def signup():
    return render_template("signup.html")
