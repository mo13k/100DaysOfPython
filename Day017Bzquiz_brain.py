
class QuizBrain:

    def __init__(self, qlist, qtype):
        self.questionnum = 0
        self.questionlist = qlist
        self.score = 0 
        self.qtype = qtype
    
    def next_question(self):
        current_question = self.questionlist[self.questionnum]
        return current_question.text, current_question.options
    
    def still_has_questions(self):
        return self.questionnum < len(self.questionlist)
    
    def check_answer(self, useranswer):
        current_question = self.questionlist[self.questionnum]
        correctanswer = current_question.answer
        iscorrect = useranswer.strip().lower() == correctanswer.strip().lower()
        if iscorrect:
            self.score += 1
        self.questionnum += 1
        return iscorrect, correctanswer