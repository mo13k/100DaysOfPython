import random
import art
from art import text2art
#global [variablename] to call a variable that was defined outside of a function, inside of a function and edit it
#prime number checker
def isprime(n):
    counter = 0
    for i in range(1, (n+1)):
        if n % i == 0:
            counter +=1
    print(counter)
    if counter == 2:
        return True
    else:
        return False

print(text2art("NUMBER GUESSING GAME"))
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Invalid difficulty. Please try again.")

num2guess = random.randint(1, 100)
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == num2guess:
        print(f"You got it! The answer was {num2guess}.")
        break
    elif guess > num2guess:
        print("Too high.")
    elif guess < num2guess:
        print("Too low.")
    attempts -= 1
if attempts == 0:
    print("You've run out of guesses. You lose.")









