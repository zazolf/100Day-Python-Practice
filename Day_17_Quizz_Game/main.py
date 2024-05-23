from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for dic in question_data:
    question_bank.append(Question(dic["text"], dic["answer"]))


quiz = QuizBrain(question_bank)
while quiz.still_have_question():
    quiz.next_question()
    

print("you've completed the quiz!")
print(f"your final score was {quiz.score}/{quiz.question_number}")
