
import os, sys
import json
import re

sys.path.append(os.path.dirname('/Users/iseong-won/model-assistant-chatgpt/Middleware'))
from Middleware import model_selector

# 사용자이 옵션 관리 객체
class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.user_path = '/Users/iseong-won/model-assistant-chatgpt/userfiles' + f"/{self.user_name}"
  
        self.selected_model = '[DEFAULT]'
        self.file_url = '[DEFAULT]'
        self.model_result = '[DEFAULT]'
        self.present_scene = 0
        
        if os.path.exists(self.user_path+"/user_options.json"):
            self.load_option_json()
    
    def load_option_json(self):
        with open(self.user_path+"/user_options.json", "r") as f:
            options = json.load(f)
        self.selected_model = options["selected_model"]
        self.file_url = options["file_url"]
        self.model_result = options["model_result"]
        self.present_scene = options["present_scene"]
    
    def save_option_json(self):
        with open(self.user_path+"/user_options.json", "w") as f:
           json.dump(self.__dict__, f)
    
    def take_option(self, input):
        scene = self.present_scene
        if scene == 1:
            if "제품 생애 총 판매량" or "1" in input:
                self.selected_model = "1"
                print("USER: saved SCENE1 option" + self.selected_model)
            else:
                print("USER: we are in scene1 but can't find user option")

        elif scene == 2:
            url = self.extract_file_path(input)
            if url:
                self.file_url = url
                print("USER: saved SCENE2 option" + self.file_url)
            else:
                print("USER: we are in scene2 but can't find user option")
        elif scene == 3:
            if self.selected_model == "1":
                model = model_selector.LifeCycle(self.file_url)
                self.model_result = model.predict()
                print("USER: saved SCENE3 option" + str(self.model_result))
        elif scene == 4:
            if self.model_result == '[DEFAULT]':
                if self.selected_model == "1":
                    model = model_selector.LifeCycle(self.file_url)
                    self.model_result = model.predict()
                    print("USER: saved SCENE3 option" + str(self.model_result))
            print("USER: saved SCENE4 option")
        elif scene == 5:
            print("USER: saved SCENE5 option")
    # def set_selected_model(self, model_name):
    #     self.selected_model = model_name
    
    # def set_file_url(self, url):
    #     self.file_url = url
    
    # def set_model_result(self, result):
    #     self.model_result = result
    def extract_file_path(self, chrs):
        p = re.compile(r'(\/[_0-9a-zA-Z-]+)+[_0-9a-zA-Z-]+\.[0-9a-zA-Z]+')
        m = p.search(chrs)
        if m:
            return m.group()
        else:
            return False
