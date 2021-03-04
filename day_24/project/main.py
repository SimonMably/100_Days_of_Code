with open("Input/Names/invited_names.txt", "r") as file_1:
    names = file_1.readlines()

with open("Input/Letters/starting_letter.txt", "r") as file_2:
    letter_lines = file_2.readlines()

for name in names:
    path = f"Output/ReadyToSend/letter_for_{name.strip()}.txt"
    with open(path, "w") as file_3:
        stripped_name = name.strip()
        replaced_name = letter_lines[0].replace("[name]", stripped_name)
        file_3.write(f"{replaced_name}\n"
                     f"{letter_lines[2]}\n"
                     f"{letter_lines[4]}\n"
                     f"{letter_lines[6]}\n")
