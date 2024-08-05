import deepl

class api:
    def __init__(self):
        self.auth_key = "bc286719-f92a-4768-b951-b9e6c170b727:fx"
        self.translator = deepl.Translator(self.auth_key)
        
    def language(self, message):
        self.message = message
        if self.message:
            cause = self.translator.translate_text(self.message, target_lang="ES")
            result = cause
        
        #print(result)
        return result

