# This is from acticvity Day 17th but instead of hardcoded question bank, we pulled questions using API. See data.py
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the history quiz.")
print(f"Your final score: {quiz.score}/{quiz.question_number}")
