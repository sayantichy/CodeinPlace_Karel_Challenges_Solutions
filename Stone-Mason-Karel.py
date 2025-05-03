from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    bottom_to_top()
    turn_right()
    for i in range (4):
        move()
    top_to_bottom()
    turn_left()
    for i in range (4):
        move()
    bottom_to_top()
    turn_right()
    for i in range (4):
        move()
    top_to_bottom()
    turn_left()

    

def bottom_to_top():
    turn_left()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()

def top_to_bottom():
    turn_right()
    for i in range(4):
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

if __name__ == '__main__':
    main()
