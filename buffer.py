import os

class TextBuffer:
    def __init__(self, file_path, num_visible_lines, preload_above=2, preload_below=2):
        self.file_path = file_path
        self.num_visible_lines = num_visible_lines
        self.preload_above = preload_above
        self.preload_below = preload_below
        self.buffer = []
        self.current_position = 0  # Line index in file
        self.total_lines = self._count_lines()
        self.load_initial_buffer()

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
