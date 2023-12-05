PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("Input/Letters/starting_letter.txt") as start_letter_file:
    starting_letter = start_letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = starting_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

# just hit run once with the folders intact, and you'll get several files generated.
