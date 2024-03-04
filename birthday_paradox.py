import datetime
import random

def getBirthdays(nb):
    birthdays = []
    for i in range(nb):
        startofyear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startofyear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA

print("Hello, this is the Birthday Paradox program.")
print("The Birthday Paradox shows us that in a group of N people, the odds")
print("that two of them have matching birthdays is surprisingly large.")
print("This program does a Monte Carlo simulation (that is, repeated random")
print("simulations) to explore this concept.")
print("It is not actually a paradox, it's just a surprising result.")

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

while True:
    print("How many birthdays shall I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break

print("\nHere are", numBDays, "birthdays:")
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(",", end="")
    monthname = MONTHS[birthday.month - 1]
    dateText = "{}{}".format(monthname, birthday.day)
    print(dateText, end="")

print("\n\nIn this simulation", end="")
match = getMatch(birthdays)
if match != None:
    monthname = MONTHS[match.month - 1]
    dateText = "{}{}".format(monthname, match.day)
    print(", multiple people have a birthday on", dateText)
else:
    print(", there are no matching birthdays")

print("\nGenerating", numBDays, "random birthdays 100,000 times...")
input("Press Enter to begin\n")
print("Let's run another 100,000 simulations")

simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1

print("100,000 simulations run.")

probability = round(simMatch / 100_000 * 100, 2)
print('\nOut of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print("That's probably more than you would think!")
