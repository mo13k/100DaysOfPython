#Quiz Game
from question_model import Question
from quiz_brain import QuizBrain
from art import text2art
import requests
import os
import html

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_questions():
    print("Quiz Customization:")
    amount = int(input("Number of questions: "))
    difficulty = (input("Difficulty (easy, medium, hard): ")).lower()
    qtype = (input("Type (multiple or boolean): ")).lower()
    print(f"\nYou will be asked {amount} {qtype} questions on {difficulty} difficulty.")
    clear()

    url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type={qtype}"
    response = requests.get(url)
    data = response.json()

    if data["response_code"] != 0:
        print("Error: Could not fetch questions. Try again.")
        return[]

    return data["results"], qtype


print("Welcome to...")
print(text2art("Mo's Quiz", font="slant"))
data, qtype = get_questions()

questionbank = []
for question in data:
    questiontext = html.unescape(question["question"])
    questionanswer = html.unescape(question["correct_answer"])
    newquestion = Question(qtext = questiontext, qanswer = questionanswer)
    questionbank.append(newquestion)

quiz = QuizBrain(qlist = questionbank, qtype = qtype)
while quiz.still_has_questions():
    quiz.nextquestion()

print(f"Your final score was {quiz.score}/{quiz.questionnum}")
print("Thank you for playing Mo's Quiz!")
