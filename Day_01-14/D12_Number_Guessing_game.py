#Number Guessing Game
#100 Days of Code ! Day 12

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
game_start = False

#Sets difficulty
while not game_start:
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    print("\n")
    if level == 'easy':
        attempts = 10
        game_start = True
    elif level == 'hard':
        attempts = 5
        game_start = True
    else:
        print("Incorrect entry. Please try Again.\n")
        
print(f"You have {attempts} attempts remaining to guess the number.\n")

#Let user guess the answer
guess = int(input("Make a guess: "))

#Choosing a random number between 1 and 100
answer = random.randint(2, 100)   
game_over = False

#Checks for guesses not between 1 and 100
def invalid_guess(guess, attempts):
    if guess > 99:  
        print("Guess should be between 1 and 100")
        return True
    elif guess < 2:
        print("Guess should be between 1 and 100")
        return True

#Checks for incorrect attempts 
def incorrect_guess(guess, answer, attempts):
    if guess > answer:
        print("Too high")
    else:
        print("Too low")

#Checks for depleted number of attempts
def attempts_over(attempts, answer):
    if attempts < 1:
        print("You've run out of guesses, you Lose")
        print(f"The answer was {answer}")
        return True

def game(game_over, answer, guess, attempts):
    all_guesses = []
    
    while not game_over:
        if answer == guess:
            print(f"You've got it! The answer was {answer}")
            return
        else:
            if invalid_guess(guess, attempts):
                print("Guess again.\n")
                print(f"You have {attempts} attempts remaining to guess the number.")
            elif guess in all_guesses:
                print("You've already guessed that number.Guess a different number.")
                all_guesses.remove(guess)
            else:
                attempts -= 1
                if attempts_over(attempts, answer):
                    return
                incorrect_guess(guess, answer, attempts)
                print("Guess again.\n")
                print(f"You have {attempts} attempts remaining to guess the number.")
                
        #Stores all guesses made for every game round
        all_guesses.append(guess)
        guess = int(input("Make a guess: "))
                    
game(game_over, answer, guess, attempts)
