import random
import art
from art import text2art

with open("Day014zcelebrities.txt", "r", encoding="utf-8") as cfile, open("Day014zfollowers.txt", "r", encoding="utf-8") as ffile:
    names = [line.strip() for line in cfile]
    followers = [int(line.strip()) for line in ffile]

data = [{}]
for name,count in zip(names,followers):
    data.append({"name":name,"followers":count})

def callperson():
    p1 = random.choice(data)
    p2 = random.choice(data)
    while p1 == p2:
        p2 = random.choice(data)
    return p1,p2


def higherlowergame():
    print(text2art("Higher\nLower", font="slant"))
    p1,p2 = callperson()
    print(f"Compare A: {p1["name"]}")
    print(text2art("VS", font="slant"),end="")
    print(f"B: {p2["name"]}")
    guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()
    if guess == "A":
        if p1["followers"] > p2["followers"]:
            print("You're right! You win!")
        else:
            print("You're wrong! You lose!")
    elif guess == "B":
        if p2["followers"] > p1["followers"]:
            print("You're right! You win!")
        else:
            print("You're wrong! You lose!")
    else:
        print("Invalid guess. Please try again.")
higherlowergame()