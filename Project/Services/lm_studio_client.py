from openai import OpenAI

class LMStudioClient:
        def __init__(self, model_name: str):

            self.client = OpenAI(base_url = "http://127.0.0.1:1234/v1", api_key = "not-needed")
            self.model = model_name


        def set_model(self, model_name: str):
            self.model = model_name


        def generate(self, messages):

            try:

                resp = self.client.chat.completions.create(
                    model = self.model,
                    messages = messages
                )
                
                return resp.choices[0].message.content.strip()
            
            except Exception as e:
                return f"[Model Error] {e}"