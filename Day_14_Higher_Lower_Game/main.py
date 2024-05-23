from art import logo
print(logo)
from game_info import data
import random
        
def guess_generation():
    item = random.choice(data)
    follower = item['follower_count']
    message = (f"Compare: {item['name']}, a {item['description']}, from {item['country']}")
    return follower, message

score = 0
follower_A, message_A = guess_generation()
follower_B, message_B = guess_generation()
    
from art import vs
right_answer = True
while right_answer:
    if follower_A == follower_B:
        follower_B = guess_generation()   
    print(message_A)
    print(vs)
    print(message_B)
    answer = input("who has the most follower? Type 'A' or 'B'").lower()

    A = follower_A
    B = follower_B

    if answer == 'A' and A>B:
        follower_B, message_B = guess_generation()
        score += 1
        print(f"You're right! your current score:{score}")
    elif answer == 'B' and B>A:
        follower_A, message_A = guess_generation()
        score += 1
        print(f"You're right! your current score:{score}")
    else:
        print(f"Sorry! that's wrong. Final Score: {score}")
        right_answer = False
    