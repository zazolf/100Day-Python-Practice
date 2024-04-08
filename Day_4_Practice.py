#rock-paper-scissors-practice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
mylist = [rock, paper, scissors]
selection = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors.\n"))
if selection >= 3 or selection < 0:
    print("select a number between 1 and 3")
else:
    print(mylist[selection])


import random
compsel = random.randint(0,2)
print(f"computer chose: {mylist[compsel]}")


if selection == 0 and compsel == 2:
    print("you won")
elif selection == 1 and compsel == 0:
    print("you won")
elif selection == 2 and compsel == 1:
    print("you won")
elif selection == compsel:
    print("draw, try again")
else: 
    print("you lost")
