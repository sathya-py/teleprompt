import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
FONT_SIZE = 30
SCROLL_SPEED = 1
BG_COLORS = [(0, 0, 0), (50, 50, 50), (150, 150, 150), (200, 200, 200), (255, 255, 255)]

# Get monitor size and set window size
monitor_info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = monitor_info.current_w, int(monitor_info.current_h * 0.75)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scrolling Text Viewer")

# Load text file
with open("textfile.txt", "r") as file:
    text_lines = file.readlines()

# State variables
scroll_y = SCREEN_HEIGHT
mirrored_horizontally = False
mirrored_vertically = False
bg_index = 0
BG_COLOR = BG_COLORS[bg_index]


def get_font(size):
    """Returns a Pygame font object with the specified size."""
    return pygame.font.Font(None, size)


def calculate_text_color(bg_color):
    """Determines text color based on background brightness."""
    brightness = (0.299 * bg_color[0]) + (0.587 * bg_color[1]) + (0.114 * bg_color[2])
    return (0, 0, 0) if brightness > 128 else (255, 255, 255)


font = get_font(FONT_SIZE)
TEXT_COLOR = calculate_text_color(BG_COLOR)


def render_text():
    """Renders text lines with horizontal and vertical mirroring options."""
    rendered_lines = []
    for line in text_lines:
        line_surface = font.render(line.strip(), True, TEXT_COLOR)
        if mirrored_horizontally:
            line_surface = pygame.transform.flip(line_surface, True, False)
        if mirrored_vertically:
            line_surface = pygame.transform.flip(line_surface, False, True)
        rendered_lines.append(line_surface)
    
    if mirrored_vertically:
        rendered_lines.reverse()
    
    return rendered_lines


def clear_and_reset():
    """Clears the screen and resets position after flipping."""
    global scroll_y
    screen.fill(BG_COLOR)
    scroll_y = SCREEN_HEIGHT if mirrored_vertically else 0


def draw_text(rendered_lines):
    """Draws rendered text lines on screen with proper alignment."""
    y_offset = scroll_y
    for line_surface in rendered_lines:
        x_pos = SCREEN_WIDTH - line_surface.get_width() - 20 if mirrored_horizontally else 20
        screen.blit(line_surface, (x_pos, y_offset))
        y_offset += line_surface.get_height() + 5


def update_scroll():
    """Updates the scrolling position based on mirroring state."""
    global scroll_y
    if mirrored_vertically:
        scroll_y += SCROLL_SPEED
        if scroll_y > SCREEN_HEIGHT:
            scroll_y = -len(text_lines) * (FONT_SIZE + 5)
    else:
        scroll_y -= SCROLL_SPEED
        if scroll_y + len(text_lines) * (FONT_SIZE + 5) < 0:
            scroll_y = SCREEN_HEIGHT


def main():
    """Main loop to handle events, update state, and render content."""
    global mirrored_horizontally, mirrored_vertically, font, BG_COLOR, TEXT_COLOR, bg_index
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    mirrored_horizontally = not mirrored_horizontally
                    clear_and_reset()
                elif event.key == pygame.K_v:
                    mirrored_vertically = not mirrored_vertically
                    clear_and_reset()
                elif event.key == pygame.K_b:
                    bg_index = (bg_index + 1) % len(BG_COLORS)
                    BG_COLOR = BG_COLORS[bg_index]
                    TEXT_COLOR = calculate_text_color(BG_COLOR)

        rendered_lines = render_text()
        draw_text(rendered_lines)
        update_scroll()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
