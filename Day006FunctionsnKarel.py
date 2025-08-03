#make your own function

def myfunct():
    #write actions here that ur function will do
    print('goatshit')

#while loops
#to clear the hurdles i did:
'''
def hurdle():
    move()
    turnleft()
    move()
    turnright()
    move()
    turnright()
    move()
    turnleft()
for step in range(1,7)#to clear 6 hurdles
    hurdle()
'''
#instead i could do:
'''
hurdles=6
while hurdles>0:
    hurdle()
    hurdles-=1
    
'''


#To solve any hurdles problem from reeborgs world
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
    
while not at_goal():
    while wall_in_front():
        hurdle()
    move()
'''
#To Solve maze problem reeborgs world
def turn_right():
    turn_left()
    turn_left()
    turn_left()
'''
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not right_is_clear and front_is_clear():
        move()
    else:
        turn_left()'''
#could fail if starts in a 2x2 square where
#right is always clear, so goes in an endless
#square

while front_is_clear():#this loop ensures you move to a place with a wall
    move()
turn_left()#if you move into a place where you get back into a 2x2 square, turning left ensures you have a wall on your right so u leave the first right_is_clear condition
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not right_is_clear and front_is_clear():
        move()
    else:
        turn_left()
