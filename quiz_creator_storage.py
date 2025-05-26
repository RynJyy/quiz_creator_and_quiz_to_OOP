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
    def save_question(self, question_data):
        data = self.load_data()
        data.append(question_data)
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(Fore.GREEN + "Quiz question saved successfully!")