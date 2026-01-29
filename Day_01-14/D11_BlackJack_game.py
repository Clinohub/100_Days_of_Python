#BlackJack game
#100 Days of Code ! Day 11

import random

def blackjack(player_cards, computer_cards, player_cards_total, computer_cards_total):
    """Identify blackjack"""
    print(f"Your hand: {player_cards}")
    print(f"Computer hand: {computer_cards}")
    
    if player_cards_total == 21 and computer_cards_total == 21:
        print("Draw")
    elif player_cards_total == 21:
        print("Blackjack: You Win")
    else:
        print("Blackjack: You Lose")

def ace_reavaluation(hand, total_deck_value):
    """
    Converts ace when busted and stops when less or equal to > 21

    Parameters
    ----------
    hand : int
        CARDS IN HAND.
    total_deck_value : int
        SUM OF ALL CARDS IN HAND.

    Returns
    -------
    int
        UPDATED HAND, UPDATED TOTAL_DECK_VALUE.
    """

    while total_deck_value > 21 and 11 in hand:
        ace_index = hand.index(11)
        hand[ace_index] = 1
        total_deck_value -= 10
           
    return hand , total_deck_value

def victory(user_chosen_cards, computer_chosen_cards):
    """Compare and prints the score of the game"""
    print("\n")
    print(f"Your final hand: {user_chosen_cards}")
    print(f"Computer's final hand: {computer_chosen_cards}")
    
    if sum(user_chosen_cards) > 21:
        print("Bust: You lose")
    elif sum(computer_chosen_cards) > 21:
        print("Computer Bust: You Win")
    elif sum(user_chosen_cards) == sum(computer_chosen_cards):
        print("Draw")
    elif sum(user_chosen_cards) > sum(computer_chosen_cards):
        print("You Win")
    else:
        print("You lose")

def game():
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    player_cards = []
    computer_cards = []  
    
    for i in range (2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        
    player_cards_total = sum(player_cards)
    computer_cards_total = sum(computer_cards)
    
    if player_cards_total == 21 or computer_cards_total == 21:
        blackjack(player_cards, computer_cards, player_cards_total, computer_cards_total)
        start_game()
        return
    
    print(f"Your cards are: {player_cards}")
    print(f"Computer cards are: ?,{computer_cards[1]}")
        
    hit = input("Do you want to get another card? Type = 'h' to hit or 's' to stand: ")
    if hit == 'h':
        player_cards.append(random.choice(cards))
        player_cards_total = sum(player_cards)
    ace_reavaluation(player_cards, player_cards_total)
    
    ace_reavaluation(computer_cards, computer_cards_total)
    while computer_cards_total < 17:
        computer_cards.append(random.choice(cards))
        computer_cards_total = sum(computer_cards)
        ace_reavaluation(computer_cards, computer_cards_total)
    
    victory(player_cards, computer_cards)
    start_game()
    
def start_game():
    """Initiates the game"""
    play_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': " )
    if play_game == 'y':
        print("\n")
        game()
    else:
        print("Exit")
        
start_game()



