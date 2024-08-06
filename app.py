from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from modules.api import api
from env import ENUM


app = Flask(__name__)

interpreter = api()
app.secret_key = ENUM.APP_KEY


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.get_json()
    text = data.get('text')
    
    processed_text = text.upper() 

    

    print(processed_text)
    if (processed_text == "영어") :
        language_result = interpreter.language(processed_text,'01')
    elif (processed_text == "스페인어") :
        language_result = interpreter.language(processed_text,'02')
    elif (processed_text == "한국어") :
        language_result = interpreter.language(processed_text,'03')
    
    sentence_result = processed_text
    


    print(sentence_result)

    result_text = getattr(sentence_result, 'text', str(language_result))

    session['english_result'] = result_text

    print(result_text)

    return jsonify({'result': result_text})

    
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=ENUM.PORT)