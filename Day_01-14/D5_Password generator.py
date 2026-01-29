#Password Generator Project
#100 days of code ! Day 5
import random

#List of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
           'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#List of numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#List of symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

#Declare and Intialize the variable to store list 
random_list = []

#Generate required number of randomized letters
for letter in range(0, nr_letters):
    rand_letter = random.randint(0, len(letters) - 1) #random.choice(letters)
    random_list += letters[rand_letter]

#Generate required number of randomized symbols
for symbol in range(0, nr_symbols):
    rand_symbol = random.randint(0, len(symbols) - 1)
    random_list += symbols[rand_symbol]

#Generate required number of randomized symbols
for number in range(0, nr_numbers):
    rand_number = random.randint(0, len(numbers) - 1)
    random_list += numbers[rand_number]
    
#Shuffle
random.shuffle(random_list)

password = ""
for _list in random_list:
    password += _list
    
print('\n')
print(password)

