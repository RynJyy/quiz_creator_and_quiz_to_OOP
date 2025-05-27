import random

class QuizLogic:
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data
        self.score = 0
        self.questions_asked = 0
        self.total_questions = len(quiz_data)
        self.current_question = None

    def next_question(self):
        self.current_question = random.choice(self.quiz_data)
        return self.current_question

    def check_answer(self, answer):
        correct = self.current_question['correct_answer']
        is_correct = answer == correct
        if is_correct:
            self.score += 1
        self.questions_asked += 1
        return is_correct, correct
    
    def is_finished(self):
        return self.questions_asked >= self.total_questions