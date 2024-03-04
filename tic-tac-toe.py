ALL_SPACES = ["1","2","3","4","5","6","7","8","9"]
X, O, BLANK = "X", "O", " "  # constants for string values 

def main():
    print("Welcome to Tic-Tac-Toe!")
    gameBoard = getBlankBoard()  # creating TTT  board dictionary 
    currentPlayer, nextPlayer = X, O # X goes for the player, O goes for the program  
    
    while True:  # Main game loop
        # displaying the board on the screen
        print(getBoardStr(gameBoard))
        # keep asking the player until they enter a number 1-9:
        move = None 
        while True:
            move = input("What is {}'s move? (1-9): ".format(currentPlayer))
            if move.isdigit() and isValidSpace(gameBoard, str(int(move))):
                break
            else:
                print("Invalid move! Please enter a valid number for a given line.")
        updateBoard(gameBoard, str(int(move)), currentPlayer)  # Make a move 
        
        # check if the game is over:
        if isWinner(gameBoard, currentPlayer):  # Check for a winner
            print(getBoardStr(gameBoard))
            print(currentPlayer, "has won the game!")
            break 
        elif isBoardFull(gameBoard):
            print(getBoardStr(gameBoard))
            print("The game is a tie!")
            break 
        # Switch turns to the next player:
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print("Thanks for playing!")

def getBlankBoard():
    # Creating blank tic-tac-toe board
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK  # because all spaces start as blank 
    return board 
def getBoardStr(board):
    # return a text-representation of the board
    return '''
       {}|{}|{}  1 2 3
       -+-+-
       {}|{}|{}  4 5 6
       -+-+-
       {}|{}|{}  7 8 9'''.format(board["1"],board["2"],board["3"],
                                 board["4"],board["5"],board["6"],
                                 board["7"],board["8"],board["9"])
def isValidSpace(board, space):
    # This function returns if the space on the board is a valid space number and whether the space is blank
    return space in ALL_SPACES and board[space] == BLANK
def isWinner(board, player):
    # return true if player is a winner on this TTT board
    b, p = board, player 
    # Check for 3 marks across 3 rows, 3 columns, and 2 diagonals.
    return ((b["1"] == b["2"] == b["3"] == p) or  # across top
            (b['4'] == b['5'] == b['6'] == p) or  # Across middle
            (b['7'] == b['8'] == b['9'] == p) or  # Across bottom
            (b['1'] == b['4'] == b['7'] == p) or  # Down left
            (b['2'] == b['5'] == b['8'] == p) or  # Down middle
            (b['3'] == b['6'] == b['9'] == p) or  # Down right
            (b['3'] == b['5'] == b['7'] == p) or  # Diagonal
            (b['1'] == b['5'] == b['9'] == p))    # Diagonal
def isBoardFull(board):
    # return true if every space on this board has been taken
    for space in ALL_SPACES:
        if board[space] == BLANK: 
            return False  # if any space is blank, return False 
    return True  # no spaces are blank, so in this case we return True
def updateBoard(board, space, mark):
    # set the space on the board to mark
    board[space] = mark 
if __name__ == "__main__":
    main()  # call main() if this module is run, but not when imported 
