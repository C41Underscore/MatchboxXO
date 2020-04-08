from AI import aiload, statecheck, aimove, aiadjust
from random import randint

#To do -
#Fix the currently crappy weight formatting system - maybe just scrap the formatting and adjust weights a different way during runtime
#Get the AI to select a position using the proabilities determined by the weights

board = list([["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]])
trainerwins = 0
aiwins = 0


def printBoard():
    for i in range(0, 3):
        for x in range(0, 3):
            print(board[i][x], end=" ")
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


def playgame(random, showBoard):
    global trainerwins
    global aiwins
    global board
    aiload()
    turnCount = 1
    x = 0
    y = 0
    while turnCount <= 9:
        if showBoard:
            printBoard()
        board = list(aimove(board))
        if isWinner() == 1:
            if showBoard:
                printBoard()
            print("The AI won!")
            aiwins += 1
            aiadjust(1)
            break
        if showBoard:
            printBoard()
        turnCount += 1
        if turnCount > 9:
            break
        if random:
            x = randint(0, 2)
            y = randint(0, 2)
        else:
            print("Enter X")
            x = int(input())
            print("Enter Y")
            y = int(input())
        while board[y][x] == "X" or board[y][x] == "O":
            if random:
                x = randint(0, 2)
                y = randint(0, 2)
            else:
                print("Enter valid position")
                print("Enter X")
                x = int(input())
                print("Enter Y")
                y = int(input())
        board[y][x] = "O"
        if isWinner() == 1:
            if showBoard:
                printBoard()
            print("The trainer won!")
            trainerwins += 1
            aiadjust(0)
            break
        turnCount += 1
    if turnCount > 9:
        print("It was a draw!")
        aiadjust(2)


if __name__ == "__main__":
    # for i in range(0, 2750):
    #     board = list([["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]])
    playgame(False, True)



