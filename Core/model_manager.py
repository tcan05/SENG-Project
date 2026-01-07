from Config.settings import load_settings, save_settings

class ModelManager:
    def __init__(self):
        self.settings = load_settings()


    def get_active_model(self):
        return self.settings.get("active_model", "llama-3.1-storm-8b")


    def set_active_model(self, model_name: str):
        self.settings["active_model"] = model_name
        save_settings(self.settings)