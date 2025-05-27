import json
from tkinter import messagebox

class QuizDataLoader:
    def __init__(self, filename='quiz_questions.json'):
        # Set the JSON file path
        self.filename = filename

    def load_data(self):
        # Load quiz data from JSON file
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Show error if file not found and return empty list
            messagebox.showerror("Error", "No questions found.")
            return []
