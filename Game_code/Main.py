import time
from Character import Character
from Slow_text import Typewriter


def print_out(string, speed=0.05):
    message_object = Typewriter(string, speed)
    message_object.text_scroll()


def main():

    # the way I'm creating messages here is still inefficient
    # just for testing purposes

    # update: created a function print_out for text printing

    print_out("Hello Adventurer! Your Journey starts here\n")
    print_out("What would your name be?\n", 0.2)
    name = str(input())

    character_1 = Character(100, name)

    character_1.damage(45)
    time.sleep(0.5)

    character_1.heal(1000)
    time.sleep(0.5)

    character_1.damage(45)
    time.sleep(0.5)

    character_1.damage(45)
    time.sleep(0.5)

    character_1.damage(45)
    time.sleep(0.5)


main()
