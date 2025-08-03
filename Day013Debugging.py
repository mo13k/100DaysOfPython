#this wont work if i put a string in the input so i can test like this to figure out the error
'''age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.")
age = ''
try:
    age = int(input("How old are you?"))
except ValueError:
    input("Please enter a valid age (number).")
    age = int(input("How old are you?"))
    
print(f"You can drive at age {age}.")'''

import random

def mutate(alist):
    blist= []
    newitem = 0
    for item in alist:
        newitem = item*2
        newitem+= random.randint(1,3)
        newitem = newitem + item
        blist.append(newitem)
    print(blist)

mutate([1,2,3,4,5])