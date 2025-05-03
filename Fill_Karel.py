from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    while no_beepers_present():
        fill_karel()
        move_to_next_row()
        
    
def move_to_next_row():
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    if front_is_clear():
        
        move()
        turn_right()
    else:
        turn_right()
        while front_is_clear(): 
            move()
        

def fill_karel():
    
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
