import pygame
import sys
from config import config
from utils import get_font, draw_text
from file_manager import file_manager
from buffer import TextBuffer
from toolbar import Toolbar

pygame.init()

# Load configuration
SCREEN_WIDTH, SCREEN_HEIGHT = config["display"]["screen_width"], config["display"]["screen_height"]
BG_COLOR = tuple(config["display"]["bg_color"])
FG_COLOR = tuple(config["display"]["fg_color"])
FONT_SIZE = config["font"]["font_size"]
SCROLL_SPEED = config["scrolling"]["scroll_speed"]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("T.Prompt")

toolbar = Toolbar(screen, SCREEN_WIDTH)
file_path = file_manager.current_file or "textfile.prom"  # Fallback file

buffer = TextBuffer(file_path, get_font(FONT_SIZE), SCREEN_HEIGHT)

def update_display():
    screen.fill(BG_COLOR)
    buffer.render(screen)
    toolbar.draw()
    pygame.display.flip()

def handle_events(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            buffer.scroll(-SCROLL_SPEED)
        elif event.key == pygame.K_DOWN:
            buffer.scroll(SCROLL_SPEED)
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

def main():
    clock = pygame.time.Clock()
    running = True
    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handle_events(event)

        update_display()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
