from art import logo
print(logo)
from game_info import data
import random


def list_creator():
    items = []
    for i in range(2):
        computer_guess = random.choice(data)
        items.append(computer_guess)
    return items
        

def guess_generation():
    from art import vs
    items = list_creator()
    A_dic = items[0]
    B_dic = items[1]
    A_follower = A_dic['follower_count']
    B_follower = B_dic['follower_count']
    message = f"Compare A: {A_dic['name']}, a {A_dic['description']}, from {A_dic['country']}\n{vs}\nCompare B: {B_dic['name']}, a {B_dic['description']}, from {B_dic['country']}"
    return A_follower, B_follower, message

score = 0
right_answer = True
while right_answer:
    A_follower, B_follower, message = guess_generation()
    print(message)
    answer = input("who has the most follower? Type 'A' or 'B'")
    A = A_follower
    B = B_follower
    if answer == 'A' and A>B:
        score += 1
        print(f"You're right! your current score:{score}")
    elif answer == 'B' and B>A:
        score += 1
        print(f"You're right! your current score:{score}")
    else:
        print(f"Sorry! that's wrong. Final Score: {score}")
        right_answer = False
    

#print(f"Compare A: {computer_guess['name']}, a {computer_guess['description']}, from {computer_guess['country']}")
# maybe define a function that compare the two results with each other
# the random number should take an item from the list and retive it's name, description and contry + print it
# there should be a while loop that takes data from game_info while the user answer is true.
# keep track of the score
# once the answer is false, get out of the loop and print the message and score