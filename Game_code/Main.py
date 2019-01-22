import time
from Character import Character
from Slow_text import Typewriter


def main():

    # the way I'm creating messages here is still inefficient
    # just for testing purposes

    intro_message = "Hello Adventurer! Your Journey starts here\n"
    intro_message = Typewriter(intro_message)
    intro_message.text_scroll()

    second_message = "What would your name be?\n"
    second_message = Typewriter(second_message, typing_speed=0.20)
    second_message.text_scroll()

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
