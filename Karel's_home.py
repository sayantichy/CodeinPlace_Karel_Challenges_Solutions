from karel.stanfordkarel import *
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    startingPoint_to_beeperPoint()
    pick_beeper()
    beeperPoint_to_StartingPoint()
    
def startingPoint_to_beeperPoint():
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()

def beeperPoint_to_StartingPoint():
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
