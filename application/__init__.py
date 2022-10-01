import os
from flask import Flask, render_template

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

@app.route("/")
def home():
    return render_template("home.html")