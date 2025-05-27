import random

class QuizLogic:
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data  # List of questions
        self.score = 0  # User's score
        self.questions_asked = 0  # Number of questions asked so far
        self.total_questions = len(quiz_data)  # Total questions available
        self.current_question = None  # Current active question

    def next_question(self):
        self.current_question = random.choice(self.quiz_data)  # Pick random question
        return self.current_question

    def check_answer(self, answer):
        correct = self.current_question['correct_answer']  # Get correct answer
        is_correct = answer == correct  # Check if user answer is correct
        if is_correct:
            self.score += 1  # Increment score if correct
        self.questions_asked += 1  # Count question as asked
        return is_correct, correct
    
    def is_finished(self):
        return self.questions_asked >= self.total_questions  # Quiz done if all questions asked
