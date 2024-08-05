import deepl

class api:
    def translate(send_message):
        auth_key = "bc286719-f92a-4768-b951-b9e6c170b727:fx"
        translator = deepl.Translator(auth_key)

        message = send_message
        result = translator.translate_text(message, target_lang="EN-US")
        
        #print(result)
        return result

