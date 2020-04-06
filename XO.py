board = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]


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
    playerXChoice = 0
    playerYChoice = 0
    print("Welcome to XO!")
    while isWinner() != 1:
        print("X enter choice: ", end="")
