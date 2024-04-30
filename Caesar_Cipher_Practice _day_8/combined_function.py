alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)


def Caesar(plain_text, shift_amount, direction): 
    new_word ="" 
    if direction == 'decode':
        shift_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_word += alphabet[new_position]
        else: 
            new_word += letter
            
    print(f"The {direction}d text is {new_word}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    Caesar(text, shift, direction) 
    result = input(" type 'yes' if you want to go again. Otherwise, type 'no'")
    if result == "no":
        should_continue = False
print("goodbye")
           


