from AI import aiload, statecheck, aimove, aiadjust
from random import randint

#To do -
#Fix the currently crappy weight formatting system - maybe just scrap the formatting and adjust weights a different way during runtime
#Get the AI to select a position using the proabilities determined by the weights

board = list([["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]])


def printBoard():
    for i in range(0, 3):
        for x in range(0, 3):
            print(board[x][i], end=" ")
        print(end="\n")
    print(end="\n")

def isWinner():
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] != "B":
            return 1
    for i in range(0, 3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[1][i] != "B":
            return 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != "B":
        return 1
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != "B":
        return 1
    return 0


if __name__ == "__main__":
    aiload()
    turnCount = 1
    playerXChoice = 0
    playerYChoice = 0
    print("Welcome to XO!")
    printBoard()
    while turnCount <= 9:
        board = list(aimove(board))
        if isWinner() == 1:
            printBoard()
            aiadjust(1)
            break
        printBoard()
        turnCount += 1
        if turnCount > 9:
            break
        playerXChoice = randint(0, 2)
        playerYChoice = randint(0, 2)
        while board[playerYChoice][playerXChoice] != "B" and board[playerYChoice][playerXChoice] != "O":
            playerXChoice = randint(0, 2)
            playerYChoice = randint(0, 2)
        board[playerYChoice][playerXChoice] = "O"
        if isWinner() == 1:
            printBoard()
            aiadjust(0)
            break
        turnCount += 1
        printBoard()
    if turnCount > 9:
        aiadjust(2)


