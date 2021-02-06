from question_model import Question
from data import question_data
import quiz_brain

question_bank = []
# print(len(question_data))
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank[1].text)