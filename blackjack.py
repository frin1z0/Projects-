import random
import sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
 
def main():
    print("Blackjack, by Dennis Osadchuk")
    print("""Rules:
          Try to get as close to 21 without going over.
          Kings, Queens, and Jacks are worth 10 points.
          Aces are worth 1 or 11 points.
          Cards 2 through 10 are worth their face value.
          (H)it to take another card.
          (S)tand to stop taking cards.
          On your first play, you can (D)ouble down to increase your bet
          but must hit exactly one more time before standing.
          In case of a tie, the bet is returned to the player.
          The dealer stops hitting at 17.""")
    money = 5000
    while True:
        if money <= 0:
            print("You are broke")
            print("Thank God, you weren't playing with real money.")
            sys.exit()
        
        print("Money:", money)
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        
        print("Bet:", bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()
            if getHandValue(playerHand) > 21:
                break
            
            move = getMove(playerHand, money - bet)
            if move == "D":
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print("Bet increased to {}".format(bet))
                print("Bet:", bet)

            if move in ("H", "D"):
                newCard = deck.pop()
                rank, suit = newCard
                print("You drew a {} of {}".format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue

            if move in ("S", "D"):
                break 
            
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break
                    
                input("Press Enter to continue")
                print("\n\n")

            displayHands(playerHand, dealerHand, True)
            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)
                    
            if dealerValue > 21:
                print("Dealer busts! You ")
                money += bet 
            elif playerValue > 21 or playerValue < dealerValue:
                print("You lost!")
                money -= bet 
            elif playerValue > dealerValue:
                print("You won ${}!".format(bet))
                money += bet 
            elif playerValue == dealerValue:
                print("It's a tie, the bet is returned to you")
                    
            input("Press enter to continue...")
            print("\n\n")

def getBet(maxBet):
    # how much player wants to bet for this round 

    while True: # we keep asking until player enters a valid amount 
        print("How much do you bet? (1-{},or QUIT)".format(maxBet))
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue 
        
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # this happens if player returns a valid bet 
        
def getDeck():
    # returning a list of rank,suit tuples for all 52 cards
        
    deck = []
    for suit in (HEARTS,DIAMONDS,SPADES,CLUBS):
        for rank in range(2,11):
            deck.append((str(rank),suit)) # adding the numbered cards
        for rank in ("J","Q","K","A"):
            deck.append((rank,suit))

    random.shuffle(deck)
    return deck 

def displayHands(playerHand, dealerHand, showDealerHand):
    # show player's and dealer's cards. Hide the dealer's first card if showDealerHand is False
    print()
    if showDealerHand:
        print("DEALER:", getHandValue(dealerHand))
        displayCards(dealerHand)

    else:
        print("DEALER:???")
        # hide the dealer's first card:
        displayCards(['BACKSIDE'] + dealerHand[1:])

    print("PLAYER:", getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    # returns the value of the cards
    value = 0 
    numberOfAces = 0
    # add the value for the non-ace cards
    for card in cards:
        rank = card[0] # cards is a tuple like(rank,suit)
        if rank == "A":
            numberOfAces += 1 
        elif rank in ("K","Q","J"): # face cards are worth 10 points 
            value += 10 
        
        else:
            value += int(rank)

    # Add the value for the aces:
    value += numberOfAces # add 1 per ace
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value + 10
    return value 

def displayCards(cards):
    # display all the cards in the cards list
    rows = ["", "", "", "", ""]

    for i, card in enumerate(cards):
        rows[0] += "___"
        if card == 'BACKSIDE':
            # print a card's back
            rows[1] += "|## |"
            rows[2] += "|###|"
            rows[3] += "|_##|"
        
        else:
            # print the card's front 
            rank, suit = card
            rows[1] += "|{} |".format(rank.ljust(2))
            rows[2] += "| {} |".format(suit)
            rows[3] += "|_{}|".format(rank.rjust(2, "_"))
    
    # print each row on the screen
    for row in rows:
        print(row)

def getMove(playerHand, money):
    # asks the player for their move, and returns H for hit, S for stand, and D for double down
    while True:
        moves = ["(H)it", "(S)tand"]
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        # Get the player's move:
        movePrompt = ",".join(moves) + ">"
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and '(D)ouble down' in moves:
            return move # player has entered a valid move 

if __name__ == "__main__":
    main()



