import html
# html was imported due to it interprets symbols as escaped chars

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
   

    def still_has_questions(self):
        return self.question_number < len(self.question_list) #true else false

    def next_question(self):
        self.current_question = self.question_list[self.question_number] #from Question with text and answer attribute
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q:{self.question_number}: {q_text}" 
        #user_answer = input(f"Q:{self.question_number}: {q_text} (True/False): ")
        self.check_answer(user_answer, self.current_question.answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
