import random
import art 
from art import text2art
import os

def clear():
    os.system("cls" if os.name == "nt" else 'clear')

def hit(hand, cards, end):
    hit = input("Type 'h' to hit, or 's' to stay.")
    if hit == 'h':
        hand.append(random.choice(list(cards.keys())))
        print(f"Your cards: {', '.join(hand)}, your score: {score(hand, cards)}")
        return False
    elif hit == 's':
        return True


def score(hand, cards):
    score = sum(cards[card] for card in hand)
    # Adjust for Aces if score > 21
    ace_count = hand.count("A") 
    while score > 21 and ace_count:
        score -= 10  # Convert an Ace from 11 to 1
        ace_count -= 1
    return score
    

def playblackjack():

    clear()
    print(text2art("BLACKJACK"))
    cards = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }
    #GENERATE PLAYERS STARTING HAND OF 2 CARDS AND CALC SCORE, THEN GENERATE DEALERS STARTING HAND OF 2 CARDS AND CALC SCORE.
    phand = [random.choice(list(cards.keys())), random.choice(list(cards.keys()))]
    print(f"Your cards: {', '.join(phand)}, your score: {score(phand, cards)}")
    dhand = [random.choice(list(cards.keys())), random.choice(list(cards.keys()))]
    print(f"Dealer's first card: {dhand[0]}")
    
    #PLAYER HIT OR STAY
    end = False
    while not end and score(phand, cards) < 21:
        if score(phand, cards) < 21:
            end = True
        end = hit(phand, cards, end)
    while score(dhand, cards) < 17:
        dhand.append(random.choice(list(cards.keys())))
    print(f"Your final hand: {', '.join(phand)}, your final score: {score(phand, cards)}")
    print(f"Dealer's hand: {', '.join(dhand)}, dealer's score: {score(dhand, cards)}")
    if score(phand, cards) > 21:
        print("You busted! You lose.")
    elif score(dhand, cards) > 21:
        print("Dealer busted! You win!")
    elif score(phand, cards) > score(dhand, cards):
        print("You win!")
    elif score(phand, cards) < score(dhand, cards):
        print("You lose.")
    else:
        print("It's a draw.")

playagain = input("Press enter to continue to Black Jack. Otherwise, press any key and enter to exit.")
while playagain == '':
    playblackjack()
    playagain = input("Press enter to continue to Black Jack. Otherwise, press any key and enter to exit.")







