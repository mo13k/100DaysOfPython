
class QuizBrain:

    def __init__(self, qlist, qtype):
        self.questionnum = 0
        self.questionlist = qlist
        self.score = 0 
        self.qtype = qtype
    
    def nextquestion(self):
        currentquestion = self.questionlist[self.questionnum]
        self.questionnum += 1
        print(f"Q.{self.questionnum}: {currentquestion.text}")

        if currentquestion.options:
            for i, option in enumerate(currentquestion.options, 1):
                print(f"{i}: {option}")

            useranswer = input("Enter the number of your answer: ")
        else:
            useranswer = input("True/False: ")
        
        self.check_answer(useranswer, currentquestion.answer)
    
    def still_has_questions(self):
        return self.questionnum < len(self.questionlist)
    
    def check_answer(self, useranswer, correctanswer):
        if useranswer.lower() == correctanswer.lower():
            self.score += 1
            print(f"Correct! \nYour score is {self.score}/{self.questionnum}")
        else:
            print(f"Incorrect! The correct answer was {correctanswer}.\nYour score is {self.score}/{self.questionnum}")

        print("\n")
