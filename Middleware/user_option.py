import os
class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.user_path = '/Users/iseong-won/model-assistant-chatgpt/userfiles' + f"/{self.user_name}"
        if os.path.exists(self.user_path):
            self.selected_model = '[DEFAULT]'
            self.file_url = '[DEFAULT]'
            self.model_result = '[DEFAULT]' 
        else:   
            self.selected_model = '[DEFAULT]'
            self.file_url = '[DEFAULT]'
            self.model_result = '[DEFAULT]'
    
    def set_selected_model(self, model_name):
        self.selected_model = model_name
    
    def set_file_url(self, url):
        self.file_url = url
    
    def set_model_result(self, result):
        self.model_result = result