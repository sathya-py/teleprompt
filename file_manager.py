import os
import tkinter as tk
from tkinter import filedialog
import config

class FileManager:
    def __init__(self, directory="."):
        """Initialize file manager with default or specified directory."""
        self.directory = directory
        self.file_list = []
        self.current_file = None
        self.load_files()

    def load_files(self):
        """Load .prom and .txt files from the directory."""
        self.file_list = [
            f for f in os.listdir(self.directory)
            if f.endswith(".prom") or f.endswith(".txt")
        ]

    def get_file_list(self):
        """Return the list of available files."""
        return self.file_list
    
    def get_file_name(self):
        """Return the name of the currently opened file."""
        return os.path.basename(self.current_file) if self.current_file else "No File Loaded"


    def open_file_dialog(self):
        """Open file dialog to select a file."""
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(
            title="Open Teleprompter File",
            filetypes=[("Prompt Files", "*.prom"), ("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            self.current_file = file_path
            config.set_last_opened_file(file_path)  # Save to config
        return file_path



    def read_file_lines(self, start=0, num_lines=10):
        """
        Read a chunk of lines from the file.
        This supports lazy loading (buffering).

        :param start: The line number to start from.
        :param num_lines: Number of lines to read.
        :return: List of lines.
        """
        if not self.current_file or not os.path.exists(self.current_file):
            return []

        with open(self.current_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return lines[start: start + num_lines]  # Lazy loading chunk

# Create a global instance
file_manager = FileManager()
