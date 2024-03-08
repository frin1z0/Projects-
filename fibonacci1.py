import sys 

print("Fibonacci Sequence, by Dennis Osadchuk osadchuk.denis07@gmail.com")

print("""The Fibonacci sequence begins with 0 and 1, and the next number is the
sum of the previous two numbers. The sequence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...""")

while True: # main program loop
    while True:   # we keep asking until the user enters valid input 
        print("Enter the Fibonacci number you wish to")
        print("calculate (such as 5, 50, 1000, 9999), or QUIT to quit:")
        response = input("> ").upper()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        if response.isdecimal() and int(response) != 0:
            number = int(response)
            break # exit the loop when the user enters a valid number 

        print("Please enter a number greater than 0, or QUIT ")
    print()
    
    # Handle the special cases if the user entered 1 of 2:
    if number == 1:
        print("0")
        print("The #1 Fibonacci number is 0.")
        break #(!)
    elif number == 2:
        print("0,1")
        print()
        print("The #2 Fibonacci number is 1.")
        continue

    # displaying the warning if the user entered a large number 

    if number >= 10000:
        print("WARNING: This can take a while to display on the screen.")
        print("If you want to quit this program before it is done, press Ctrl-C")
        input("Press Enter to begin...")

    # calculate the user entered Fibonacci number
    secondToLastNumber = 0
    lastNumber = 1 
    fibNumbersCalculated = 2 
    print("0,1", end="") # display the first two Fibonacci nubmers 

    # Display all the later nubmers of the fibonacci sequence 
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1 

        # Displaying the next number in a sequence:
        print(nextNumber, end="")
        # Check if we've found the n number the user wants:
        if fibNumbersCalculated == number:
            print()
            print()
            print("The # ", fibNumbersCalculated, "Fibonacci", "number is ", nextNumber, sep="")
            break 
        
        # print a comma in between the sequence numbers:
        print(",", end="")

        # shift the last two numbers:
        secondToLastNumber = lastNumber
        lastNumber = nextNumber 



