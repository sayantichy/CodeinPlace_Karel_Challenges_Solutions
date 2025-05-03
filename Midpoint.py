from karel.stanfordkarel import *

# Helper function to turn Karel 180 degrees
def turn_around():
    turn_left()
    turn_left()

def main():
    # Move Karel to the far wall
    while front_is_clear():
        move()
    
    # Place a beeper at the far wall as a boundary marker
    put_beeper()
    turn_around()
    
    # Check if there's at least one cell ahead (more than 1 cell in the world)
    if front_is_clear():
        move()
        # Check if there's more than 2 cells in the world
        if front_is_clear():
            # Complex logic for larger worlds to find the midpoint
            findMid()
            remove_all_beepers()
            middle()
            # Ensure Karel is facing East at the end
            if not_facing_east():
                turn_around()
        else:
            # Handle the 2x1 or 2x2 case (worlds with only 2 cells)
            turn_around()
            # If Karel didn't land on a beeper, adjust placement
            if no_beepers_present():
                move()
                pick_beeper()
                turn_around()
                move()
                put_beeper()
                turn_around()
            else:
                # Karel is already on the beeper (correct middle)
                middle()

# Function to place a beeper at the far right and prepare for mid detection
def placebeeperwall():
    while front_is_clear():
        move()
    put_beeper()
    turn_and_move()

# Repeatedly check and place beepers inward from both sides until mid is found
def findMid():
    placebeeperwall()
    while no_beepers_present():
        is_it_mid()
        find_beeper()

# Remove all helper beepers used to find the mid
def remove_all_beepers():
    pick_beeper_alg()   # Clean one side
    turn_around()
    middle()            # Move to the beeper left at mid
    pick_beeper_alg()   # Clean the other side
    turn_around()

# Move across a line and pick up all beepers found
def pick_beeper_alg():
    while front_is_clear():
        move()
        pick_beeper()

# Move until Karel is on a beeper (used to return to mid)
def middle():
    while no_beepers_present():
        move()

# Check if Karel is at the midpoint by comparing beeper locations
def is_it_mid():
    move()
    if beepers_present():
        turn_and_move()
        put_beeper()

# Move toward the beeper placed from the far side and continue midpoint search
def find_beeper():
    if no_beepers_present():
        while no_beepers_present():
            move()
        turn_and_move()
        put_beeper()
        move()

# Helper function to turn around and move one step
def turn_and_move():
    turn_around()
    move()

if __name__ == '__main__':
    main()
