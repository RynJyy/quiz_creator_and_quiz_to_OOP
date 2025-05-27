import json
from colorama import Fore

class QuizStorage:
    def __init__(self, filename='quiz_questions.json'):
        # Initialize with JSON filename
        self.filename = filename

    def load_data(self):
        # Load quiz data from JSON file
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_question(self, question_data):
        # Append new question and save to file
        data = self.load_data()
        data.append(question_data)
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(Fore.GREEN + "Quiz question saved successfully!")
