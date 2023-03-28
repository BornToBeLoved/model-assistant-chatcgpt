import sys
import os
sys.path.append(os.path.dirname('/Users/iseong-won/model-assistant-chatgpt/Middleware'))
from Middleware.chatbot import Chatbot

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def init():
    return render_template('chat.html')



@app.route('/chat', methods=['POST', 'GET'])
def chat():
    print(request)
    try:
        print(request.form['query'])
        if request.method == 'POST':
            data = request.form['query']
            print(data)
        return "THIS IS TEST"
    except Exception as e:
        print(e)
        return "FAILED"

if __name__ == '__main__':
    app.run('0.0.0.0', port=2000, debug = True)