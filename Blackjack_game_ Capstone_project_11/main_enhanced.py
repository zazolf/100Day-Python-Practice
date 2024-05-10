
import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")

def score_calculate(my_list):
  if sum(my_list) == 21 and len(my_list) == 2:
    return 0
  if 11 in my_list and sum(my_list) > 21:
    my_list.remove(11)
    my_list.append(1)
  return sum(my_list)

def compare(user_current_score, computer_score):
    if user_current_score == 0:
      return " you won with a jackpot!"

    elif computer_score == 0:
      return " you lost! computer won with a jackpot!"

    elif user_current_score > 21 and computer_score > 21:
      return "You went over. You lose 😤"
        
    elif user_current_score > 21:
      return " you lost! you went over!"
        
    elif computer_score > 21:
      return " you won! computer went over!"
        
    elif user_current_score == 21:
      return " you won!"
        
    elif computer_score == 21:
      return "you lost!"

    elif user_score == computer_score:
      return "Draw"   
    

def start_game():
  
  is_game_over = False
  print(logo)
  user_list = []
  computer_list = []
  for i in range(2):
      user_list.append(random.choice(cards))
      computer_list.append(random.choice(cards))
  

  while not is_game_over:
     user_current_score = score_calculate(user_list)
     computer_score = score_calculate(computer_list)
     print(f"your cards: {user_list}, current score: {user_current_score}, computer_first_card: {computer_list[0]}")
     
     if user_current_score == 0 or computer_score == 0 or user_current_score > 21:
       is_game_over = True
     else:
       repeat = input("Type 'y' to get another card, type 'n' to pass: ")
       if repeat == "y":
         user_list.append(random.choice(cards))
       else:
        is_game_over = True

     while computer_score != 0 and computer_score < 17:
      computer_list.append(random.choice(cards))
      computer_score = score_calculate(computer_list)

     print(f"your final hand: {user_list}, final score: {user_current_score}")
     print(f"computer's final hand: {computer_list}, final score: {computer_score}")
     print(compare(user_current_score, computer_score))
        
while play == "y":
  start_game()
  play = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")

