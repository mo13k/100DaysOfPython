#basic function with input
'''name = input("what is your name? ")
def greet(name):
    print("hello "+name)
    print("nice to meet you")
    print("goodbye")
    return(name)

greet(name)'''
#time left in life in weeks
'''age = int(input("age in years: "))

def life_in_weeks(age):
    age *= 52
    timeleft = 4680 - age
    return timeleft
    
print(f"You have {life_in_weeks(age)} weeks left.")'''
#function with two parameters - positional & keyword arguments
'''def greetw(name,location):
    print(f"Hello {name}, your location is {location}")

greetw("Muhammad","Vaughan") #positional argument
greetw(name = "muhammad",location  ="Vaughan") #keyword argument'''
#love calculator
'''def calculate_love_score(name1, name2):
    names = list(name1)+list(name2)
    true = ['t','r','u','e']
    love = ["l","o","v","e"]
    score1 = 0
    score2 = 0
    for i in range(len(names)):
        for j in range(len(true)):
            if names[i] == true[j]:
                score1 +=1
    for i in range(len(names)):
        for j in range(len(love)):
            if names[i] == love[j]:
                score2 += 1
    score = str(score1) + str(score2)
    return(score)
name1 = input("enter your name: ")
name2 = input("enter your partner's name: ")
print(f"your love score is {calculate_love_score(name1, name2)}")'''

#Caesar Cipher - the main thing here
def ciphermap(startchoice, shift):

    alphabet =  'abcdefghijklmnopqrstuvwxyz'
    alphabetshift = {}

    for i in range(len(alphabet)):
        alphabetshift[alphabet[i]] = alphabet[(i + shift) % 26]

    if startchoice.lower() == "decode":
        flipped = {}
        for k in alphabetshift:
            flipped[alphabetshift[k]] = k
        alphabetshift = flipped

    return alphabetshift

def applycipher(message, alphabetshift):
    final = ""
    for letter in message:
        if letter in alphabetshift:
            final += alphabetshift[letter]
        else:
            final += letter
    return final

print('''           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             ''')
playagain = input("Press enter to begin.")

#gameloop
while playagain == "":
    message = input("\nenter your message: ").lower()
    shift = int(input("enter your shift number: "))
    startchoice = input("\nType \'encode\' to encrypt, Type \'decode\' to decrypt: ")
    alphabetshift = ciphermap(startchoice, shift)
    print(f"your result: {applycipher(message, alphabetshift)}")

    playagain = input("\nPress enter to play again. Otherwise, press any key and enter to exit.")

