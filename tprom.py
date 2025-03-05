import pygame
import sys
from config import config
from utils import get_font, draw_text
from file_manager import file_manager
from buffer import TextBuffer
from toolbar import Toolbar

# Initialize pygame
pygame.init()

# Load user configuration
SCREEN_WIDTH, SCREEN_HEIGHT = config.get_screen_size()
BG_COLOR = config.get_bg_color()
FG_COLOR = config.get_fg_color()
FONT_SIZE = config.get_font_size()
SCROLL_SPEED = config.get_scroll_speed()

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("T.Prompt")

# Initialize modules
toolbar = Toolbar(screen)
buffer = TextBuffer(file_manager.current_file, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE)

def update_display():
    """Renders text on the screen"""
    screen.fill(BG_COLOR)  # Background color
    lines_to_render = buffer.get_visible_lines()

    y_offset = 50  # Start position for text
    for line in lines_to_render:
        rendered_text = draw_text(line, get_font(FONT_SIZE), FG_COLOR)
        screen.blit(rendered_text, (50, y_offset))
        y_offset += FONT_SIZE + 5

    toolbar.draw()  # Draw the toolbar on top
    pygame.display.flip()

def handle_keyboard_events(event):
    """Handles keyboard shortcuts for font size, scrolling, and alignment"""
    global FONT_SIZE, BG_COLOR, FG_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            buffer.scroll_up()
        elif event.key == pygame.K_DOWN:
            buffer.scroll_down()
        elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
            FONT_SIZE = min(FONT_SIZE + 2, 120)
            config.set_font_size(FONT_SIZE)
        elif event.key == pygame.K_MINUS:
            FONT_SIZE = max(FONT_SIZE - 2, 6)
            config.set_font_size(FONT_SIZE)
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

def main():
    """Main loop for the teleprompter"""
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(BG_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
                config.set_screen_size((SCREEN_WIDTH, SCREEN_HEIGHT))
            else:
                handle_keyboard_events(event)

        update_display()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
