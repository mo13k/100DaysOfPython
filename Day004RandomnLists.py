#random & lists
import random


#modules - each one is responsible for a certain aspect of ur program, great to split really long code into
#multiple modules, or if working in a group
'''choice = random.randint(1,2)
if choice == 1:
    print("heads")
else:
    print("tails")'''

'''list1 = ["heads", "tails"]
print(list1[random.randint(0,(len(list1)-1))])
#list1[1] = "Tails"
#print(list1)
#list1.append("wingchong")
#list1.extend(list1)
#print(list1)
#list1.pop(0)
print(list1)'''

#who will pay the bill game
'''
#1st way easier
friends = ['mo', 'gajan', 'yadu']
print(random.choice(friends))
#2nd way
print(friends[random.randint(0,len(friends)-1)])
'''

#common issue with list is index out of range, hard when u want to call last item in list but dk the list length
#lenfrien = len(friends)-1

#nested lists
'''
fruits = ['apple', 'banana', 'orange']
veggies = ['spinach', 'kale']
dirtydozen = [fruits, veggies]
print(dirtydozen)
'''

#rock paper scissors game
print("Let's play Rock, Paper, Scissors...")

#making computer's choices
rock = str(r'''
              _    ,-,    _
                 ,--, /: :\/': :`\/: :\
                |`;  ' `,'   `.;    `: |
                |    |     |  '  |     |.
                | :  |     | pb  |     ||
                | :. |  :  |  :  |  :  | \
                 \__/: :.. : :.. | :.. |  )
                      `---',\___/,\___/ /'
                           `==._ .. . /'
                                `-::-'
''')
paper = str(r'''
      _.--._  _.--._
,-=.-":;:;:;\':;:;:;"-._
\\\:;:;:;:;:;\:;:;:;:;:;\
 \\\:;:;:;:;:;\:;:;:;:;:;\
  \\\:;:;:;:;:;\:;:;:;:;:;\
   \\\:;:;:;:;:;\:;::;:;:;:\
    \\\;:;::;:;:;\:;:;:;::;:\
     \\\;;:;:_:--:\:_:--:_;:;\    
      \\\_.-"      :      "-._\
       \`_..--""--.;.--""--.._=>
''')
scissors = str(r'''
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
''')

choices = [rock, paper, scissors]
computerchoice = random.randint(0,2)

playerchoice = int(input("Type 0 for rock, 1 for paper, and 2 for scissors: "))
print(f"You chose: {choices[playerchoice]}")
print(f"I chose: {choices[computerchoice]}")

if computerchoice == playerchoice:
    print("Tie Game")

elif computerchoice == 0 and playerchoice == 1:
    print("You win!")
elif computerchoice == 0 and playerchoice == 2:
    print("You lose!")

elif computerchoice == 1 and playerchoice == 0:
    print("You lose!")
elif computerchoice == 1 and playerchoice == 2:
    print("You win!")

elif computerchoice == 2 and playerchoice == 0:
    print("You win!")
elif computerchoice == 2 and playerchoice == 1:
    print("You lose!")