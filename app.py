from flask import Flask, request, redirect, render_template, url_for, session
from modules.api import api
app = Flask(__name__)

@app.route("/rt890piytr")
def home():
    return render_template('index.html')

@app.route("/")
def button():
    tmp = api.translate("안녕하세요!")
    print(tmp)
    return render_template('index.html',tmp = tmp)
    
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=8080)