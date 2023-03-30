import sys
import os
import shutil
sys.path.append(os.path.dirname('/Users/iseong-won/model-assistant-chatgpt/Middleware'))
from Middleware.chatbot import Chatbot

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def init():
    try:
        # 접속할때 마다 대화 히스토리 지우기.
        shutil.rmtree('/Users/iseong-won/model-assistant-chatgpt/userfiles/blue')
    except:
        pass
    return render_template('chat.html')



@app.route('/chat', methods=['POST', 'GET'])
def chat():
    print(request)
    try:
        print(request.form['query'])
        if request.method == 'POST':
            data = request.form['query']
            userName = request.form['name']
            print(data)
    except Exception as e:
        print(e)
        return "DATA_RECIEVE_FAILED\n: 데이터를 주고받는 과정에서 오류가 발생했습니다. "
    try:
        bot1 = Chatbot(userName)
        return bot1.talk_with_bot(data)
    except:
        return "CHATBOT_CONTACT_FAILED\n: 챗봇과 대화하는 과정에서 오류가 발생했습니다. "

if __name__ == '__main__':
    app.run('0.0.0.0', port=2000, debug = True)