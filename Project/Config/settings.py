import json
from pathlib import Path

SETTINGS_FILE = Path(__file__).parent / "settings.json"

def load_settings():

    if SETTINGS_FILE.exists():
        return json.loads(SETTINGS_FILE.read_text())
    
    return {}
    
def save_settings(settings: dict):
    SETTINGS_FILE.write_text(json.dumps(settings, indent=2))