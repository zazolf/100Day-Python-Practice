alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount): 
    new_word = "" 
    for letter in plain_text:
        new_letter_index = alphabet.index(letter) + shift_amount
        letter = alphabet[new_letter_index]
        new_word += letter
    print(f"The encoded text is {new_word}")

def decode(plain_text, shift_amount):
    new_word= ""
    for letter in plain_text:
        new_letter_index = alphabet.index(letter) - shift_amount
        letter = alphabet[new_letter_index]
        new_word += letter
    print(f"The decoded text is {new_word}")

if direction == 'encode':
  encrypt(text, shift)
elif direction == 'decode':
  decode(text, shift)
  
