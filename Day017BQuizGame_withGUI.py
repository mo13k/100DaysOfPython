#Quiz Game with GUI
from Day017Bzquestion_model import Question
from Day017Bzquiz_brain import QuizBrain
from Day017Bzui import QuizInterface, QuizSetupGUI

import tkinter as tk
import requests
import os
import html
import random
from tkinter import messagebox

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_questions_gui():
    # Show setup GUI
    setup_gui = QuizSetupGUI()
    setup_gui.window.mainloop()
    
    if setup_gui.quiz_data is None:
        return None, None
    
    amount = setup_gui.quiz_data['amount']
    difficulty = setup_gui.quiz_data['difficulty']
    qtype = setup_gui.quiz_data['type']
    
    url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type={qtype}"
    response = requests.get(url)
    data = response.json()

    if data["response_code"] != 0:
        messagebox.showerror("Error", "Could not fetch questions. Please try again.")
        return None, None

    return data["results"], qtype

def createquestionbank(data):
    question_bank = []
    for question in data:
        questiontext = html.unescape(question["question"])
        correct_answer = html.unescape(question["correct_answer"])
        incorrect_answers = [html.unescape(ans) for ans in question["incorrect_answers"]]

        all_answers = incorrect_answers + [correct_answer]
        random.shuffle(all_answers)

        question_obj = Question(
            qtext=questiontext,
            qanswer=correct_answer,
            options=all_answers if question["type"] == "multiple" else None
        )
        question_bank.append(question_obj)
    return question_bank

if __name__ == "__main__":

    question_data, qtype = get_questions_gui()
    
    if question_data is None:
        exit()
        
    question_list = createquestionbank(question_data)
    quiz = QuizBrain(qlist=question_list, qtype=qtype)
    
    quiz_ui = QuizInterface(quiz)