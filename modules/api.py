import deepl

class api:
    def __init__(self):
        self.auth_key = "bc286719-f92a-4768-b951-b9e6c170b727:fx"
        self.translator = deepl.Translator(self.auth_key)
        
    def language(self, message, code):
        self.message = message
        self.code = code
        if self.message:
            if self.code == "01":
                result = self.translator.translate_text(self.message, target_lang="EN-US")
            elif self.code == "02":
                result = self.translator.translate_text(self.message, target_lang="ES")
            elif self.code == "03":
                result = self.translator.translate_text(self.message, target_lang="KO")


        #print(result)
        return result

