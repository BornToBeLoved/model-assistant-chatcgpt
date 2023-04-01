import sys
import os


sys.path.append(os.path.dirname('/Users/iseong-won/model-assistant-chatgpt/keys'))
sys.path.append(os.path.dirname('/Users/iseong-won/model-assistant-chatgpt/scenarios'))
sys.path.append(os.path.dirname('/Users/iseong-won/model-assistant-chatgpt/models'))
import openai
import keys.openai_apy_key as key
import scenarios.gpt_system_content as content

import json

import re

# 발급받은 API 키 설정
OPENAI_API_KEY = key.key

# openai API 키 인증
openai.api_key = OPENAI_API_KEY

class Chatbot:
    def __init__(self, username):
        # 모델 - GPT 3.5 Turbo 선택
        self.model = "gpt-3.5-turbo"
        self.username = username
        self.user_path = '/Users/iseong-won/model-assistant-chatgpt/userfiles' + f"/{self.username}"
        self.messages = self.load_message()
        self.present_scene = 0

    # ChatGPT API 호출
    # 메시지(문맥) 설정하기
    def make_first_content(self):
        messages = [
                {"role": "system", "content": content.before_predict}
        ]
        # messages = [
        #         {"role": "system", "content": content.presentation}
        # ]
        return messages
    
    # 유저 메세지 저장소에 저장.
    def save_message(self, data = None):
        if data == None:
            data = self.make_first_content()

        with open(self.user_path+"/messages.json", "w") as f:
            json.dump(data, f)

    # 저장된 메세지 불러오기.
    def load_message(self):
        if not os.path.exists(self.user_path):
            os.mkdir(self.user_path)
            self.save_message()
    
        with open(self.user_path+"/messages.json", "r") as f:
            data = json.load(f)
        return data

    # OPENAI API사용해서 챗봇과 대화하기.
    def talk_with_bot(self, query, debug = False):
        if debug:
            print(query)
        
        self.messages.append({"role": "user", "content": query})

        response = openai.ChatCompletion.create(
            model= self.model,
            messages=self.messages
        )
        # print(response)
        answer =response['choices'][0]['message']['content']

        self.messages.append({"role": "assistant", "content": answer})

        
        self.save_message(data = self.messages)

        if debug:
            print(answer)

        # 현재 scene 탐지하기.
        self.detect_scene(answer)

        return answer
    
    def detect_scene(self, answer):

        p = re.compile(r"\[SCENE[0-9]\]")
        m = p.findall(answer)
        print(m)
        if m:
            num = m[-1][-2]
            self.present_scene = int(num)
            print(f"chatbot: [SCENE{num}] DETECTED") 
        else:
            return 0


'''
USER차원의 변수
'''
# while True:
#     bot1 = Chatbot("1")
#     query = input("입력:")
#     print(bot1.talk_with_bot(query))

# def detect_scene(answer):

#     p = re.compile(r"\[SCENE[0-9]\]")
#     m = p.findall(answer)
#     print(m)
#     if m:
#         num = m[-1][-2]
#         print(f"chatbot: [SCENE{num}] DETECTED") 
#     else:
#         return 0
# detect_scene("[SCENE1]번을 막 하다가 이제 [SCENE2]번이 나오면 머리가 하얀색이 되는거지")