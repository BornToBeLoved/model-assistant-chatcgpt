import sys
import os
sys.path.append(os.path.dirname('/Users/iseong-won/model-assistant-chatgpt/keys'))
sys.path.append(os.path.dirname('/Users/iseong-won/model-assistant-chatgpt/scenarios'))
sys.path.append(os.path.dirname('/Users/iseong-won/model-assistant-chatgpt/models'))

import openai
import keys.openai_apy_key as key
import scenarios.gpt_system_content as content

# 발급받은 API 키 설정
OPENAI_API_KEY = key.key

# openai API 키 인증
openai.api_key = OPENAI_API_KEY

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-3.5-turbo"

# ChatGPT API 호출
# 메시지(문맥) 설정하기
def make_first_content(text):
    messages = [
            {"role": "system", "content": text}
    ]
    return messages

def talk_with_bot( query, messages = None, debug = False):
    if debug:
        print(query)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    answer = response['choices'][0]['message']['content']
    
    if debug:
        print(answer)
    return answer

messages = make_first_content(content.content)

while True: 
    query = input()
    if query =='quit':
        break
    messages.append({"role": "user", "content": query})

    answer = talk_with_bot(query, messages, debug=True)
    messages.append({"role": "assistant", "content": answer})