import pygame
import os
import config
import tkinter as tk
from tkinter import colorchooser

# Load settings from config
config = config.load_config()

# Font Cache
_loaded_fonts = {}


def get_font(size=None, font_name=None):
    """Load a font dynamically with caching."""
    if size is None:
        size = config["font"]["font_size"]
    if font_name is None:
        font_name = config["font"]["font_name"] or None  # Use default system font

    font_key = (font_name, size)
    if font_key not in _loaded_fonts:
        if font_name:
            font_path = os.path.join("assets/fonts", font_name)
            if os.path.exists(font_path):
                _loaded_fonts[font_key] = pygame.font.Font(font_path, size)
            else:
                print(f"⚠ Font '{font_name}' not found. Using default.")
                _loaded_fonts[font_key] = pygame.font.Font(None, size)
        else:
            _loaded_fonts[font_key] = pygame.font.Font(None, size)

    return _loaded_fonts[font_key]

def draw_text(text, font, color):
    """Render text with anti-aliasing."""
    return font.render(text, True, color)


# === COLOR UTILITIES === #
def open_color_picker(target):
    """Open color picker for BG/FG selection and update config."""
    root = tk.Tk()
    root.withdraw()
    color = colorchooser.askcolor(title=f"Select {target.upper()} Color")[1]
    if color:
        update_colors(bg_color=color if target == "bg" else None,
                      fg_color=color if target == "fg" else None)
        save_updated_config()

def update_colors(bg_color=None, fg_color=None):
    """Update background and foreground colors in config."""
    if bg_color:
        config["display"]["bg_color"] = bg_color
    if fg_color:
        config["font"]["font_color"] = fg_color

# === FONT UTILITIES === #
def load_font(size=None, font_name=None):
    """Loads a font dynamically from assets/fonts/ (supports TTF and OTF)."""
    size = size or config["font"]["font_size"]
    font_name = font_name or config["font"]["font_name"]
    
    font_dir = os.path.join(os.path.dirname(__file__), "assets", "fonts")
    font_path = None

    # Check both TTF and OTF variants
    for ext in [".ttf", ".otf"]:
        file_path = os.path.join(font_dir, font_name + ext)
        if os.path.exists(file_path):
            font_path = file_path
            break

    if not font_path:
        print(f"⚠ Font '{font_name}' not found. Using default.")
        font_path = None  # Use system default

    # Cache the font for performance
    if (font_path, size) not in _loaded_fonts:
        _loaded_fonts[(font_path, size)] = pygame.font.Font(font_path, size)

    return _loaded_fonts[(font_path, size)]

def change_font_size(delta):
    """Increase or decrease font size within allowed limits (6 - 120)."""
    new_size = max(6, min(120, config["font"]["font_size"] + delta))
    config["font"]["font_size"] = new_size
    save_updated_config()
    return load_font(new_size)

# === TEXT ALIGNMENT UTILITIES === #
def get_text_position(text_surface, screen_width, screen_height, alignment):
    """Determines text position based on alignment settings."""
    text_width, text_height = text_surface.get_size()
    
    positions = {
        "left": (20, screen_height // 2 - text_height // 2),
        "right": (screen_width - text_width - 20, screen_height // 2 - text_height // 2),
        "center": ((screen_width - text_width) // 2, screen_height // 2 - text_height // 2)
    }

    return positions.get(alignment, (20, 20))  # Default fallback

# === MIRRORING UTILITIES === #
def apply_mirroring(text_surface, mirror_horizontal, mirror_vertical):
    """Applies mirroring effects based on the settings."""
    return pygame.transform.flip(text_surface, mirror_horizontal, mirror_vertical) if mirror_horizontal or mirror_vertical else text_surface

# === SCROLLING UTILITIES === #
def adjust_scroll_speed(delta):
    """Adjust scrolling speed within reasonable limits (1-10)."""
    new_speed = max(1, min(10, config["scrolling"]["scroll_speed"] + delta))
    config["scrolling"]["scroll_speed"] = new_speed
    save_updated_config()

# === CONFIG UTILITIES === #
def save_updated_config():
    """Saves any modified settings back to config.json."""
    from config import save_config
    save_config(config)
