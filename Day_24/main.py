# File Handling
# 100 Days of Code ! Day 24

with open("./Input/Letters/starting_letter.txt", mode="r") as template:
    template_letter = template.readlines()

with open("./Input/Names/invited_names.txt", "r") as invited_names:
    name_list = invited_names.readlines()

for names in name_list:
    letter_list = []
    name = names.strip('\n')
    letter_list.append(template_letter[0].replace("[name]", name))
    letter_list.extend(template_letter[1::])

    filename = f"./Output/ReadyToSend/letter_for_{name}.txt"
    with open(filename, "w") as letter:
        for lines in letter_list:
            letter.write(lines)