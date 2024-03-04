import sys
import random
import time

try:
    import bext
except ImportError:
    print("This program requires the bext module")
    print("You can install it by following instructions at this website")
    print("https://pypi.org/project/Bext/")
    sys.exit()

# setting up  the width and height constants 
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a newline automatically, so reduce the width by one:
WIDTH -= 1

NUMBER_OF_LOGOS = 10 # you could change it how you want 
PAUSE_AMOUNT = 0.1  # you could change it how you want 

COLORS = ["red", "green", "magenta", "purple"]

UP_RIGHT = "ur"
UP_LEFT = "ul"
DOWN_RIGHT = "dr"
DOWN_LEFT = "dl"
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# key names for logo dictionaries:
COLOR = "color"
X = "x"
Y = "y"
DIR = "direction"


def main():
    bext.clear()
    # generating some logos 
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # if x is odd, it will hit the corner 
            logos[-1][X] -= 1 
    
    cornerBounces = 0 # how many times a logo hits a corner 
    while True:
        for logo in logos:
            # erasing the logo's current location
            bext.goto(logo[X], logo[Y])
            print("   ", end="") # (!)try to comment this line 

            originalDirection = logo[DIR]
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1 
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1 
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1 
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1 
            # see if the logo bounces off the left edge:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the right edge:
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # See if the logo bounces off the top edge:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the bottom edge:
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                # Change color when the logo bounces:
                logo[COLOR] = random.choice(COLORS)

            # Move the logo. (X moves by 2 because the terminal characters are twice as tall as they are wide.)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # Display number of corner bounces:
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end='')

        for logo in logos:
            # Draw the logos at their new location:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)
        sys.stdout.flush() # Required for bext-using programs.
        time.sleep(PAUSE_AMOUNT)

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Dennis Osadchuk')
        sys.exit() # When Ctrl-C is pressed, end the program.
