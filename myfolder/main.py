from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for ques in question_data:
    question_text=ques["text"]
    question_answer=ques["answer"]
    new_ques=Question(question_text,question_answer)
    question_bank.append(new_ques)
quiz=QuizBrain(question_bank)

while quiz.still_question():
    quiz.next_ques()
print("YOu have completed the quiz!")    
print(f"Your final score was : {quiz.score}/{quiz.question_number}")