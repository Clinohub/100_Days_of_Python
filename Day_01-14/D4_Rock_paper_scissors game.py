#Rock, paper, scissors game
#100 Days of Code ! Day 4
import random

print("What do you choose?")
my_turn = int(input("Type 0 for rock, 1 for paper or 2 for scissors."))
comp_turn = random.randint(0,2)

if my_turn == 0:
    print("You chose rock.\n")
    if comp_turn == 0:
        print("Computer chose rock.\n")
        print("Draw")
    elif comp_turn == 1:
        print("Computer chose paper.\n")
        print("You lose")
    else:
        print("Computer chose scissor.\n")
        print("You win")

elif my_turn == 1:
    print("You chose paper.\n")
    if comp_turn == 0:
        print("Computer chose rock.\n")
        print("You win")
    elif comp_turn == 1:
        print("Computer chose paper.\n")
        print("Draw")
    else:
        print("Computer chose scissor.\n")
        print("You lose")

elif my_turn == 2:
    print("You chose scissors.\n")
    if comp_turn == 0:
        print("Computer chose rock.\n")
        print("You lose")
    elif comp_turn == 1:
        print("Computer chose paper.\n")
        print("You win")
    else:
        print("Computer chose scissor.\n")
        print("Draw")
        
else:
    print("Invalid. You lose!!")