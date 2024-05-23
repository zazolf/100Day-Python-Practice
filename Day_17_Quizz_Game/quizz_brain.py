

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q.{self.question_number}:{current_question.text}. (True/False)?: ")
        self.check_answer(user_choice, current_question.answer)

    def still_have_question(self):
        if self.question_number == 12:
            return False
        else:
            return True

    def check_answer(self, user_choice, correct_answer):
        if user_choice == correct_answer:
            self.score += 1
            print("you got it right!")
        else: 
            print("that's wrong!")
        print(f"the correct answer is {self.question_list[self.question_number].answer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")
