from hangman_art import stages, logo
print(logo)
import hangman_words
import random
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)


display = []
for i in range(len(chosen_word)):
        display += '-'
print(display)

lives = 7
while '-' in display and lives != 0:
    guess = input("Guess a letter = ").lower()
    if guess in display:
        print("you have already guessed this letter, try another one!")
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
      lives -= 1
      print(stages[lives])
      print(f"you guessed {guess}, that's not in the word. you lose a life")

    print(display)
if lives == 0:
  print("you lose!")
else:
  print("You win!")
   