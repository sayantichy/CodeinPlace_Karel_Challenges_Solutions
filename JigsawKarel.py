from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    way_to_pickBeeper()
    place_beeper()
    wayback_to_startingPoint()
    
def way_to_pickBeeper():
    while no_beepers_present():
        move()
    pick_beeper()

def place_beeper():
    move()
    turn_left()
    for i in range(2):
        move()
    put_beeper()

def wayback_to_startingPoint():
    turn_around()
    for i in range(2):
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_around()

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
