#loops
'''
fruits = ['apple', 'banana', 'pear']
for fruit in fruits:
    #makes fruit = each item in the list, and then prints until the end, doesnt actually change the fruits list tho
    print(fruit, end=", ")#end= makes a loop print in the same line
'''
#solution to max of list, sum of list, and range function
'''
####################################################
scores = [1,17,3,4,5,6,7,8]
totalscore = sum(scores)
print(totalscore)

#otherway of doing this
sum = 0
for score in scores:
    sum+= score
print(sum)

#####################################################
highscore = max(scores)
print(highscore)

#otherway of doing this
max = 0
for score in scores:
    if score > max:
        max = score
print(max)
######################################################
#range function (range(start, end+1, step size))
total=0
for number in range(0,101,2):
    total+= number
print(total)
'''
#FizzBuzz Game
'''
You are going to write a program that automatically prints the solution to the FizzBuzz game. 
These are the rules of the FizzBuzz game:
Your program should print each number from 1 to 100 in turn and include number 100.
But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
'''

#Random Password Generator Project
import random
letters = list(map(chr, range(97,123)))
digits = list("0123456789")
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
chars = letters + digits + symbols
password = []
for passchartotal in range(1,13):
    password.append(random.choice(chars))
password = ''.join(password)
print(password)