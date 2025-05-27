# 🧠 Quiz Creator to Quiz App (OOP)

A Python-based, object-oriented quiz system that lets you **create** and **take** quizzes through a modern **Tkinter GUI**. 
Designed with modularity, clarity, and user experience in mind.

---

## 📦 Features

✅ Create multiple-choice quizzes  
✅ Object-Oriented Structure (Separation of Concerns)  
✅ User-friendly GUI with `tkinter`  
✅ Randomized questions  
✅ Immediate feedback on answers  
✅ Score summary at the end  

---
```
quiz_creator_to_OOP/
├── main_quiz_creator.py # Entry point for Quiz Creator
├── main_quiz_app.py # Entry point for Quiz App
├── quiz_questions.json # Shared data file (quiz questions)
├── quiz_creator.py # Handles creator orchestration
├── quiz_creator_questions.py # Manages question structure
├── quiz_creator_storage.py # JSON file I/O
├── quiz_creator_ui.py # UI for quiz creation
├── quiz_app_gui.py # Main Quiz GUI
├── quiz_app_logic.py # Core quiz logic (score, progression)
├── quiz_app_data_loader.py # Loads data from JSON
├── quiz_app_question_display.py # Displays question & meta info
├── quiz_app_answer_buttons.py # Manages answer choices
└── quiz_app_feedback.py # Feedback, next button, final score
```
---

## 🚀 Features

- 🛠️ **Quiz Creator Interface**: Add, edit, and save multiple-choice questions.
- 🎯 **Quiz Taking Interface**: Answer randomized questions and get real-time feedback.
- 🧩 **Modular OOP Design**: Separate logic, UI, and data layers for maintainability.
- 💾 **JSON Persistence**: Questions are saved and loaded from a single `.json` file.
- 🎨 **Modern Tkinter GUI**: Clean, structured interface with consistent design.

---

## ✅ Run the Quiz App
- python main_quiz_app.py
