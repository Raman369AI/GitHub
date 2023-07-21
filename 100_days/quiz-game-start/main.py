import data
import question_model
from quiz_brain import Quiz

question_bank = []
answers = []
length = len(data.question_data)
for i in range(0, length):
    question_text = data.question_data[i]["text"]
    question_answer = data.question_data[i]["answer"]
    question_bank.append(question_model.Question(question_text, question_answer))
# initialising a quiz object
quiz = Quiz(question_bank)
while quiz.is_ended():
    quiz.next_question()
