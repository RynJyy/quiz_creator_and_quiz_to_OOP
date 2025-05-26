import json
from colorama import Fore

class QuizStorage:
    def __init__(self, filename='quiz_questions.json'):
        self.filename = filename

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []