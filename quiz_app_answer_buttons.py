import tkinter as tk

class AnswerButtons:
    def __init__(self, window, on_answer):
        self.buttons = []
        for i in range(4):
            btn = tk.Button(window, text="", width=30, height=2, font=("Helvetica", 12), fg="black", bg="white", relief="ridge")
            btn.pack(pady=8)
            self.buttons.append(btn)
        self.on_answer = on_answer