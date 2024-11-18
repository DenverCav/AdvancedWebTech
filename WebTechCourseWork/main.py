from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/GeneralInfo") #Forgot to actually say that the way to reach this page is with this / ... This is stuff I can't afford to forget.
def GeneralInfo():
    return render_template('GeneralInfo.html')

@app.route("/Notes")
def Notes():
    return render_template('Notes.html')