import pygame
import tkinter as tk
from tkinter import filedialog, colorchooser
import config
import file_manager

# Toolbar Dimensions
ICON_SIZE = 24
PADDING = 10
TOOLBAR_HEIGHT = 40
TOOLBAR_BG = (30, 30, 30)

# Colors
TOOLBAR_BG = (30, 30, 30)  # Dark Grey
TEXT_COLOR = (255, 255, 255)  # White
BUTTON_COLOR = (50, 50, 50)  # Button Background
HOVER_COLOR = (80, 80, 80)  # Hover Effect
BORDER_COLOR = (100, 100, 100)  # Separator Line

# Button Configurations
buttons = [
    {"label": "aA", "action": "toggle_font"},
    {"label": "f", "action": "change_font"},
    {"label": "◄", "action": "align_left"},
    {"label": "►", "action": "align_right"},
    {"label": "▲", "action": "align_top"},
    {"label": "▼", "action": "align_bottom"},
    {"label": "BG", "action": "change_bg"},
    {"label": "FG", "action": "change_fg"},
    {"label": "▪", "action": "minimize"},
    {"label": "■", "action": "maximize"},
    {"label": "X", "action": "close"},
]


class Toolbar:
    def __init__(self, screen, width):
        """Initialize the toolbar with button positions and actions."""
        self.screen = screen
        self.width = width
        self.height = TOOLBAR_HEIGHT
        self.dragging = False
        self.offset_x, self.offset_y = 0, 0
        self.font = pygame.font.Font(None, 20)
        self.active_file = "Promptfile"
        self.buttons_rects = []  # ✅ Initialize button rectangles
        self.create_buttons()  # ✅ Ensure this runs after other initializations
        self.title_rect = pygame.Rect(PADDING, 8, width // 3, ICON_SIZE)  # Clickable title area

    def create_buttons(self):
        """Calculate button positions and store their rects."""
        x_offset = self.width - PADDING  # ✅ Initialize x_offset before using it
        self.buttons_rects = []

        for btn in reversed(buttons):  # Right-aligned buttons
            btn_surface = self.font.render(btn["label"], True, TEXT_COLOR)
            btn_width, btn_height = btn_surface.get_size()
            btn_rect = pygame.Rect(x_offset - btn_width - PADDING, 8, btn_width + 8, ICON_SIZE)
            x_offset -= (btn_width + PADDING + 10)  # ✅ Ensure x_offset is updated
            self.buttons_rects.append((btn_rect, btn["action"]))



    def update_file_name(self, file_name):
        """Update the displayed filename in the toolbar."""
        self.active_file = file_name or "No File Loaded"

    def draw(self):
        """Render the toolbar and its elements."""
        pygame.draw.rect(self.screen, TOOLBAR_BG, (0, 0, self.width, self.height))
        pygame.draw.line(self.screen, BORDER_COLOR, (0, self.height), (self.width, self.height), 2)

        # Draw Application Title (Clickable)
        title_surface = self.font.render(f"T.Prompt - {self.active_file}", True, TEXT_COLOR)
        self.screen.blit(title_surface, (PADDING, 10))

        # Draw Buttons
        for btn_rect, action in self.buttons_rects:
            pygame.draw.rect(self.screen, BUTTON_COLOR, btn_rect, border_radius=5)
            label_surface = self.font.render(action[0], True, TEXT_COLOR)
            self.screen.blit(label_surface, (btn_rect.x + 5, btn_rect.y + 5))
        
        for btn in reversed(buttons):  # Right-aligned buttons
            btn_surface = self.font.render(btn["label"], True, TEXT_COLOR)
            btn_width, btn_height = btn_surface.get_size()
            btn_rect = pygame.Rect(x_offset - btn_width - PADDING, 8, btn_width + 8, ICON_SIZE)
            x_offset -= (btn_width + PADDING + 10)
            self.buttons_rects.append((btn_rect, btn["action"]))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 0 <= event.pos[1] <= self.height:
                self.dragging = True
                self.offset_x, self.offset_y = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
            x, y = pygame.mouse.get_pos()
            pygame.display.get_window_surface().get_abs_parent().move(x - self.offset_x, y - self.offset_y)
            

    def execute_action(self, action):
        """Perform the respective toolbar action."""
        if action == "toggle_font":
            config.toggle_font_size()
        elif action == "change_font":
            config.next_font()
        elif action == "align_left":
            config.set_alignment("left")
        elif action == "align_right":
            config.set_alignment("right")
        elif action == "align_top":
            config.set_alignment("top")
        elif action == "align_bottom":
            config.set_alignment("bottom")
        elif action == "change_bg":
            self.open_color_picker("bg")
        elif action == "change_fg":
            self.open_color_picker("fg")
        elif action == "minimize":
            pygame.display.iconify()
        elif action == "maximize":
            pygame.display.toggle_fullscreen()
        elif action == "close":
            pygame.quit()
            exit()

    def open_file_dialog(self):
        """Open file dialog to select a file."""
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        file_path = filedialog.askopenfilename(
            title="Open Teleprompter File",
            filetypes=[("Prompt Files", "*.prom"), ("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        
        if file_path:
            self.update_file_name(file_path.split("/")[-1])
            file_manager.load_file(file_path)  # Pass file to manager

    def open_color_picker(self, target):
        """Open color picker for BG/FG selection."""
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        color = colorchooser.askcolor(title=f"Select {target.upper()} Color")[1]  # Get hex color
        if color:
            if target == "bg":
                config.set_background_color(color)
            elif target == "fg":
                config.set_foreground_color(color)


