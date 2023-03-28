import sys
import os
sys.path.append(os.path.dirname('/Users/iseong-won/model-assistant-chatgpt/Middleware'))
from Middleware.chatbot import Chatbot

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def init():
    return render_template('chat.html')



@app.route('/preprocessing', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        data = request.json
        print(data)
    return "THIS IS TEST"

if __name__ == '__main__':
    app.run('0.0.0.0', port=2000, debug = True)