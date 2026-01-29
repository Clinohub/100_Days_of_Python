#Love Calculator
#100 Days of Code ! Day 3

# Don't change the code below
print("Welcome to Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

#Write your code below this line
name_case = name1.lower() + name2.lower()
t = name_case.count('t')
r = name_case.count('r')
u = name_case.count('u')

l = name_case.count('l')
o = name_case.count('o')
v = name_case.count('v')

e = name_case.count('e')

love_score = ((t+r+u+e)*10 + (l+o+v+e))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and menthos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")