
import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def score_calculate(my_list):
  if sum(my_list) == 21 and len(my_list) == 2:
    return 0
  elif 11 in my_list and sum(my_list) > 21:
    my_list.remove(11)
    my_list.append(1)
  return sum(my_list)


def start_game():

  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
  print(logo)

  if play == 'y':
    user_list = []
    for i in range(2):
        user_list.append(random.choice(cards))
    user_current_score = score_calculate(user_list)

    computer_list = []
    for j in range(2):
        computer_list.append(random.choice(cards))
    computer_score = score_calculate(computer_list)

    print(f"your cards: {user_list}, current score: {user_current_score}, computer_first_card: {computer_list[0]}")

    game = True
    while game:
      if user_current_score == 21 and len(user_list) == 2:
        print(" you won with a jackpot!")
      elif computer_score == 21 and len(computer_list) == 2:
        print(" you lost! computer won with a jackpot!")
      elif user_current_score > 21 and computer_score > 21:
        print( "you lost! both went over!")
        game = False
      elif user_current_score > 21:
        print(" you lost! you went over!")
        game = False
      elif computer_score > 21:
        print(" you won! computer went over!")
        game = False
      elif user_current_score == 21:
        print(" you won!")
        game = False
      elif computer_score == 21:
        print("you lost!")
        game = False
      else: 
        repeat = input("Type 'y' to get another card, type 'n' to pass: ")
        new_comp_item = random.choice(cards)
        computer_list.append(new_comp_item)
       

        if repeat == 'y':
         new_user_item = random.choice(cards)
         user_list.append(new_user_item)
         user_current_score = score_calculate(user_list)
         computer_score = score_calculate(computer_list)

         print(f"your cards: {user_list}, current score: {user_current_score}, computer first card: {computer_list[0]}")


        elif repeat == 'n':
          print(f"your final hand: {user_list}, final score: {user_current_score}")
          print(f"computer's final hand: {computer_list}, final score: {computer_score}")
          if user_current_score > computer_score:
            print("you won!")
          elif user_current_score == computer_score:
            print("draw")
          else:
            print("you lost!")
          start_game()

start_game()
