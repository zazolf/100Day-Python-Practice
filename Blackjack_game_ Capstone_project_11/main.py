
import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_game():

  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'")

  if play == 'y':
    print(logo)
    user_list = []
    for i in range(2):
        user_choice = random.choice(cards)
        user_list.append(user_choice)
    user_current_score = user_list[0] + user_list[1]

    computer_list = []
    for j in range(2):
        computer_choice = random.choice(cards)
        computer_list.append(computer_choice)
    computer_score = computer_list[0] + computer_list[1]

    print(f"your cards: {user_list}), current score: {user_current_score}, computer_first_card: {computer_list[0]}")

    game = True
    while game:
      if user_current_score == 21 and len(user_list) == 2:
        print(" you won with a jackpot!")
      elif computer_score == 21 and len(computer_list) == 2:
        print(" you lost! computer won with a jackpot!")
      elif computer_score > 21:
        print(" you won! computer went over!")
        game = False
      elif user_current_score == 21:
        print(" you won!")
        game = False
      elif user_current_score > 21:
        print("you lost! you went over!")
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
         user_current_score += new_user_item


         
         computer_score += new_comp_item
         print(f"your cards: {user_list}, current score: {user_current_score}, computer_first_card: {computer_list[0]}")

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
