import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "display": {
        "screen_width": 800,
        "screen_height": 600,
        "window_mode": "windowed",
        "bg_color": [0, 0, 0],
        "fg_color": [255, 255, 255]
    },
    "font": {
        "font_size": 30,
        "font_name": None,
        "font_color": [255, 255, 255],
        "text_alignment": "left",
        "text_orientation": "normal"
    },
    "scrolling": {
        "scroll_speed": 1,
        "scroll_direction": "up"
    },
    "toolbar": {
        "toolbar_visible": True,
        "toolbar_position": "top"
    }
}

class ConfigWatcher(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_modified(self, event):
        if event.src_path.endswith(CONFIG_FILE):
            self.callback()

def create_default_config():
    with open(CONFIG_FILE, "w") as file:
        json.dump(DEFAULT_CONFIG, file, indent=4)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        create_default_config()
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

def start_config_watcher(callback):
    event_handler = ConfigWatcher(callback)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer_thread = threading.Thread(target=observer.start, daemon=True)
    observer_thread.start()

config = load_config()
start_config_watcher(lambda: print("Config updated! Reload settings dynamically."))
