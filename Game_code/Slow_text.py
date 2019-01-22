import sys
import time

# This is a very interesting line of code that creates a text text text scroll
# Typewriter effect for the output of the text
# The user may easily change the speed of the output


class Typewriter:
    def __init__(self, message, typing_speed=0.05):
        self.message = message
        self.typing_speed = typing_speed

    def text_scroll(self):
        for character in self.message:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(self.typing_speed)
