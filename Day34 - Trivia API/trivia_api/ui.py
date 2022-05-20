
from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = '#375362'
TRUE = '#2E8B57'
FALSE = '#8B0000'


class QuizInterface:
    

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR )
        self.score_label.grid(row =0, column = 1)

        #interface
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="hello", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50) #columnspan requires position 150, 125 ablove


        # #button
        self.true_button = Button(text="✔",fg=TRUE, borderwidth=0, font=('Arial', 50, 'normal'), command=self.true_ans)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(text="✘",fg=FALSE,borderwidth=0, font=('Arial', 50, 'normal'), command=self.false_ans)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text= f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        
    def true_ans(self):
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right)
        
    def false_ans(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)
        
    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="seagreen4")
        else:
            self.canvas.config(bg="indian red")
    
        
        self.window.after(1000, self.get_next_question)
        