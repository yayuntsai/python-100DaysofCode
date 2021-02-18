with open("./Input/Names/invited_name.txt") as name_list:
    names = name_list.readlines()
    #names.strip()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    placeholder = '[name]'
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(placeholder, stripped_name)
        with open(f"./Output/ReadToSend/letter_of_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)