import os
import json

class Config:
    CONFIG_FILE = os.path.expanduser("~/.vermithor_config.json")

    @staticmethod
    def load_config():
        if os.path.exists(Config.CONFIG_FILE):
            with open(Config.CONFIG_FILE, "r") as f:
                return json.load(f)
        return {}

    @staticmethod
    def save_config(config):
        with open(Config.CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)

    @staticmethod
    def get_api_key(provider):
        config = Config.load_config()
        return config.get("api_keys", {}).get(provider)

    @staticmethod
    def set_api_key(provider, key):
        config = Config.load_config()
        if "api_keys" not in config:
            config["api_keys"] = {}
        config["api_keys"][provider] = key
        Config.save_config(config)

    @staticmethod
    def get_llm_model(task_type):
        # Default models based on builtin-llm-models skill
        models = {
            "recon": "claude-sonnet-4-6",
            "prioritize": "gpt-5",
            "report": "gpt-5-mini"
        }
        config = Config.load_config()
        return config.get("models", {}).get(task_type, models.get(task_type))
