from flask import Flask, request, redirect, render_template, url_for, session
from modules.api import api
app = Flask(__name__)

translator = api()

@app.route("/rt890piytr")
def home():
    return render_template('index.html')

@app.route("/")
def button():
    message = "테스트"
    tmp = translator.language(message)
    print(tmp)
    return render_template('index.html',tmp = tmp)
    
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=8080)