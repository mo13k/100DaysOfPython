import random
#'''

print("Welcome to the Hangman Game!")
Difficulty = (input("Choose how many letters each word should be: "))
while not Difficulty.isdigit():
    Difficulty = (input("Numeric value only: "))

Difficulty = int(Difficulty)

with open('Day007zwords_alpha.txt') as file:#random word generator
    words=file.read().splitlines()
    words = [word for word in words if len(word) == Difficulty]
    solution = random.choice(words)
solution = list(solution)

blank = []
for number in range(Difficulty):
    blank.append('_') #making blank placeholder

hangmanparts = [ # Stage 1: Head and torso
    """
     _____
     |   |
     |   O
     |   |
     |   
    _|_
    """,

    # Stage 2: One arm
    """
     _____
     |   |
     |   O
     |  /|
     |   
    _|_
    """,

    # Stage 3: Two arms
    """
     _____
     |   |
     |   O
     |  /|\\
     |   
    _|_
    """,

    # Stage 4: One leg
    """
     _____
     |   |
     |   O
     |  /|\\
     |  / 
    _|_
    """,

    # Stage 5: Full body
    """
     _____
     |   |
     |   O
     |  /|\\
     |  / \\
    _|_
    """]#hangman illustrations
hangmancurrent = ( """
     _____
     |   |
     |   
     |   
     |   
    _|_
    """)

wrongs = 0
gameover = False
lives = 5
guessed = set()

while gameover == False:
    if blank == solution:#game ending logic
        gameover = True
    elif wrongs == len(hangmanparts)-1:
        gameover = True

    print(f"*******************************************{lives} lives left*******************************************")
    guess = input("Guess a letter: ").lower()
    if guess in guessed:#this way, they arent penalized for repeating letters
        print("You already guessed that letter")
        guessed.add(guess)
    else:
        guessed.add(guess)
        lcounter = 0
        for i in range(len(solution)):
            if solution[i] == guess:
                blank[i] = guess
            elif solution[i] != guess:
                lcounter+=1
        if lcounter == Difficulty:#if their guess didn't match up against every letter in the word, it is a wrong guess
            hangmancurrent = hangmanparts[wrongs]
            wrongs += 1
            lives -= 1

        print(''.join(blank))
        print(hangmancurrent)

if blank == solution:#win/loss statements
    print(f'you won with {lives} lives remaining')
elif wrongs == len(hangmanparts):
    print("you lost")
#'''

