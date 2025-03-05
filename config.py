import json
import os

CONFIG_FILE = "config.json"

# Default configuration settings
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
    },
    "shortcuts": {
        "increase_font_size": "K_PLUS",
        "decrease_font_size": "K_MINUS",
        "toggle_horizontal_mirror": "K_h",
        "toggle_vertical_mirror": "K_v",
        "toggle_bg_color": "K_b"
    }
}

def create_default_config():
    """Create a new config.json file with default settings if it doesn't exist."""
    with open(CONFIG_FILE, "w") as file:
        json.dump(DEFAULT_CONFIG, file, indent=4)
    print(f"Config file '{CONFIG_FILE}' created with default settings.")

def load_config():
    """Load configuration from the JSON file. If it doesn't exist, create one first."""
    if not os.path.exists(CONFIG_FILE):
        create_default_config()
    
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

def save_config(config_data):
    """Save the given configuration data into the JSON file."""
    with open(CONFIG_FILE, "w") as file:
        json.dump(config_data, file, indent=4)

def update_config(section, key, value):
    """Update a specific configuration value and save the changes."""
    config = load_config()
    if section in config and key in config[section]:
        config[section][key] = value
        save_config(config)
        print(f"Updated '{key}' in '{section}' to {value}")

# Ensure the config file exists on first run
if not os.path.exists(CONFIG_FILE):
    create_default_config()

# Load config at the start
config = load_config()
