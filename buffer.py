import os
import pygame

class TextBuffer:
    def __init__(self, file_path, font, screen_height):
        self.file_path = file_path
        self.font = font
        self.lines = self._load_lines()
        self.scroll_offset = 0
        self.screen_height = screen_height

    def _load_lines(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.readlines()

    def scroll(self, amount):
        self.scroll_offset = max(0, self.scroll_offset + amount)

    def render(self, screen):
        screen.fill((0, 0, 0))
        y = -self.scroll_offset
        fade_start = 30  # Number of pixels for fade effect
        fade_end = self.screen_height - fade_start

        for i, line in enumerate(self.lines):
            alpha = 255
            if y < fade_start:
                alpha = max(0, (y / fade_start) * 255)
            elif y > fade_end:
                alpha = max(0, ((self.screen_height - y) / fade_start) * 255)

            text_surface = self.font.render(line.strip(), True, (255, 255, 255))
            text_surface.set_alpha(alpha)
            screen.blit(text_surface, (50, y))
            y += 40

    def _count_lines(self):
        """Returns total number of lines in the file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return sum(1 for _ in f)
        except FileNotFoundError:
            return 0

    def load_initial_buffer(self):
        """Loads the initial set of lines based on the screen size."""
        self.buffer = self._read_lines(0, self.num_visible_lines + self.preload_below)

    def _read_lines(self, start, count):
        """Reads 'count' lines from file starting at 'start' index."""
        lines = []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    if i >= start:
                        lines.append(line.strip())
                    if len(lines) >= count:
                        break
        except FileNotFoundError:
            pass
        return lines

    def scroll_down(self):
        """Scrolls down by one line, loads more if needed."""
        if self.current_position + self.num_visible_lines < self.total_lines:
            self.current_position += 1
            self.buffer = self._read_lines(
                self.current_position - self.preload_above, 
                self.num_visible_lines + self.preload_below
            )

    def scroll_up(self):
        """Scrolls up by one line, loads more if needed."""
        if self.current_position > 0:
            self.current_position -= 1
            self.buffer = self._read_lines(
                max(0, self.current_position - self.preload_above), 
                self.num_visible_lines + self.preload_below
            )

    def get_visible_lines(self):
        """Returns the currently buffered lines for display."""
        return self.buffer
