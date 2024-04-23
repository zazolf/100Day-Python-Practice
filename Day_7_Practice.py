#Step 1 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
print(chosen_word)


display = []
for i in range(len(chosen_word)):
        display += '-'
print(display)

lives = 6
while '-' in display and lives != 0:
    guess = input("Guess a letter = ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
      lives -= 1
      print(stages[lives])

    print(display)
if lives == 0:
  print("you lose!")
else:
  print("You win!")
     




   
   

