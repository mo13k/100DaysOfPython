#if else conditional
'''
if int(input("how tall are you: ")) >= 120:
    print("you can ride")
else:
    print("leave")
'''

#modulo
'''
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")'''

#nestedconditionals
'''
height = int(input("Enter your height: "))
if height >= 120:
    print("you can ride")
    bill = 0
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("your ticket is $5")
    elif age <= 18:
        bill = 7
        print("your ticket is $7")
    elif 45 <= age <= 55:
        print("everything is fine its free")
    else:
        bill = 12
        print("your ticket is $12")

    photo = input("do you want a photo?\n")
    if photo.startswith("y") and 45 <= age <= 55:
        bill = bill
    elif photo.startswith("y"):
        bill += 3

    print("your total bill is $" + str(bill))

else:
    print("too short")
'''

#treasureisland game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print('Welcome to Treasure Island.\nYour mission is to find the treasure.\n')

crossroad = input("You're at a crossroads. Where do you want to go?\n   Type \"left\" or \"right\" \n")

if crossroad.startswith("l"):
    print("\nYou've come to a lake. There's a boat island is the middle of the lake.")
    boatswim = input("  Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n")

    if boatswim == "wait":
        print("\nThe boat arrives. It takes you to a set of doors.")
        doorchoice = input("  \"red\", \"yellow\" or \"blue\"? \n")

        if doorchoice == "yellow":
            print("\nYou arrive at the treasure.\nYou Win!")

        elif doorchoice == "red":
            print("\nYou were burned by fire.\nGame Over.")
        elif doorchoice == "blue":
            print("\nYou were eaten by beasts.\nGame Over.")
        else:
            print("\nlame.game over.")
    else:
        print("\nYou were attacked by trout.\nGame Over.")

else:
    print("\nYou feel into a hole. \nGame Over.")
