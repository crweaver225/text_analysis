from flask import Flask
from flask import request
from flask import render_template, redirect
from text_analytics import *
import string
import math

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/compare_texts", methods=['POST', 'GET'])
def compare_texts():
    
    if request.method == 'POST':
        text1 = request.form['Text1']
        text2 = request.form['Text2']
        if text1 is None and text2 is None:
            return render_template('index.html',
                analytics = "Cant compare empty fields",
                txt1 = '',
                txt2 = ''
            )
        elif text1 == '' and text2 == '':
            return render_template('index.html',
                analytics = "Cant compare empty fields",
                txt1 = '',
                txt2 = ''
            )
        else:
            exclude = set(string.punctuation)

            text1 = ''.join(pf for pf in text1 if pf not in exclude).lower()
            text2 = ''.join(pf for pf in text2 if pf not in exclude).lower()
        
            vocab_to_int = establish_vocab(text1, text2)
        
            tokenized_string = tokenize_string(vocab_to_int, text1)
            tokenized_string2 = tokenize_string(vocab_to_int, text2)

            final = cosine_simularity(tokenized_string, tokenized_string2)

            return render_template('index.html',
                analytics = "Text simularity score: {}".format(round(final, 3)),
                txt1 = request.form['Text1'],
                txt2 = request.form['Text2']
            )
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)


