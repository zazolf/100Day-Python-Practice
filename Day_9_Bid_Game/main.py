bid_dic = {}
def bid_dictionary(name, bid):
    bid_dic[name] = bid
    print(bid_dic) 
import os
def clear():
  
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program!")
repeat = True
while repeat:
    name = input("what is your name?")  
    bid = float(input("what is your bid?"))
    again = input("Are there any other bidders? Type 'Yes' or 'No'")
    if again == "yes":
        clear()
    elif again == "no":
        repeat = False

    bid_dictionary(name, bid)
    highest_bid = 0
    winner = ""
    for item in bid_dic:
        if bid_dic[item] > highest_bid:
            highest_bid = bid_dic[item]
            winner = item


print(f"The winner is {winner} with a bid of {highest_bid}")


