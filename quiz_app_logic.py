import random

class QuizLogic:
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data
        self.score = 0
        self.questions_asked = 0
        self.total_questions = len(quiz_data)
        self.current_question = None

    