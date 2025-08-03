#type conversion
'''print("123"+"456")
print(int("123")+int("456"))
int("hello")doesnt work cus how would u change to numbers
print("number of letters in your name: "+ str(len(input("enter your name: "))))
Operators: -, +, *, /, //, **
print(int(3*(3+3/3-3)))'''

#BMI Calculator
'''height = 1.85
weight = 66
bmi = weight / (height**2)
print(bmi)
print(round(bmi, 5))
'''
#fstring lesson
'''
score = 0
score += 1
score -= 1
height = 1.85
iswinning = True
print(f"your score is {score}, your heigh is {height}, and you're winning is {iswinning}
'''

#Tip Calculator
print("Welcome to the tip calculator!\n")
bill = float(input("Enter your bill amount: $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people will split the bill? "))
print(f"Each person should pay: ${round(bill*(1+tip/100)/people,2)}")
