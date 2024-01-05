from flask import Flask
app=Flask(__name__)
@app.route("/")
def firstFlask():
    return "This is my first flask program"
@app.route("/Rochelle")
def secondFlask():
    return "Hi my name is Rochelle"

app.run()