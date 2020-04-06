from AI import aiload, statecheck, aimove

board = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]


def printBoard():
    for i in range(0, 3):
        for x in range(0, 3):
            print(board[x][i], end=" ")
        print(end="\n")

def isWinner():
    for i in range(0, 3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][1] != "0":
            return 1
    for i in range(0, 3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[1][i] != "0":
            return 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != "0":
        return 1
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != "0":
        return 1

if __name__ == "__main__":
    aiload()
    playerXChoice = 0
    playerYChoice = 0
    print("Welcome to XO!")
    printBoard()
    while isWinner() != 1:
        print("X enter X choice: ", end="")
        playerXChoice = int(input())
        print("X enter Y choice: ", end="")
        playerYChoice = int(input())
        board[playerYChoice][playerXChoice] = "X"
        printBoard()
        aimove()
