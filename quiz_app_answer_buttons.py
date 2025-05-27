import tkinter as tk

class AnswerButtons:
    def __init__(self, window, on_answer):
        self.buttons = []
        for i in range(4):
            btn = tk.Button(window, text="", width=30, height=2, font=("Helvetica", 12), fg="black", bg="white", relief="ridge")
            btn.pack(pady=8)
            self.buttons.append(btn)
        self.on_answer = on_answer

    def set_answers(self, answers, correct_callback):
        for i, option in enumerate(['a', 'b', 'c', 'd']):
            self.buttons[i].config(
                text=answers[i],
                command=lambda opt=option: self.on_answer(opt),
                bg="white",
                activebackground="#d9d9d9"
            )