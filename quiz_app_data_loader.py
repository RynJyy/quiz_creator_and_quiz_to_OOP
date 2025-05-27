import json
from tkinter import messagebox

class QuizDataLoader:
    def __init__(self, filename='quiz_questions.json'):
        self.filename = filename

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No questions found.")
            return []