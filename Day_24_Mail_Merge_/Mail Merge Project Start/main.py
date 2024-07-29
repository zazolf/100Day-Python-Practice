#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
#f = open("./Input/Letters/starting_letter.txt", mode="r")
letter = open("C:/Users/zolfa/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r")
sentence_list = letter.readlines()
print(sentence_list)
name = open("C:/Users/zolfa/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt", mode="r")
name_list = name.readlines()


print(name_list)
i=0
for name in name_list: 
    place_holder = ["[name]",'Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph']
    name = name.strip() 
    new_name = sentence_list[0].replace(place_holder[i], name)
    i += 1
    sentence_list[0] = new_name
    new_letter = ''.join(sentence_list)
    #print(new_letter)
    file_name = f"C:/Users/zolfa/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt"
    with open (file_name, mode="w") as file:
        file.write(new_letter)

    

   
    

   
    

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp