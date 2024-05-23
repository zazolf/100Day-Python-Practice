print("Welcome to the Number Gussing Ggame!")
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
import random
computer_number = random.randint(1,100)

def number_finder(n):
    message = "You've run out of guesses, you lose"
    while n != 0:
        print(f"you have {n} attempts remaining to guess the number")
        guess = int(input("Make a guess:  "))
        if guess > computer_number:
            print("Too high")
            print("Guess again")
            n = n - 1 
        elif guess < computer_number:
            print("Too low")
            print("Guess again")
            n = n - 1 
        elif guess == computer_number:
            message = f"You got it! the answer was {guess}"
            break
    print(message)

if difficulty_level == "easy":
    number_finder(10)
elif difficulty_level == "hard":
    number_finder(5)
    
    