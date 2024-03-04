import random
import sys
import time

PAUSE = 0.15  # this line adjusts  the speed of dna 

# these are individual rows of the DNA animation

ROWS = [
    #123456789 -- this is done to measure the number of spaces 
    '           ##',  # index 0 has no {}
    '         #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '       #{}-{}#',
    '       ##',  # here we don't use {}
    '      #{}-{}#',
    '      #{}---{}#',
    '     #{}----{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}--{}#',
    '         #{}-{}#',
]

# 123456789 <- We use this line to measure the number of spaces

try:
    print("DNA animation, by Dennis Osadchuk")
    print("Press Ctrl-C to quit")
    time.sleep(2)
    rowIndex = 0

    while True:  # Main program loop
        # incrementation of rowIndex to draw next row
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0

        # Row indexes 0 and 9 don't have nucleotides:
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue
        # select random nucleotide pairs, guanine-cytosine and adenine-thymine:
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = "A", "T"
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = "T", "A"
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = "C", "G"
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = "G", "C"

        # print row
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE)  # here i add a slight pause
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program
