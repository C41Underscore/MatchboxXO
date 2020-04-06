states = {}

def aiload():
    with open("states.txt", "r") as statefile:
        for state in statefile:
            stateArr = state.strip().split(":")
            states[stateArr[0]] = stateArr[1]

def statecheck(state):
    alreadySeen = False
    for i in states.keys():
        if i == state:
            alreadySeen = True
    if not alreadySeen:
        with open("states.txt", "a") as statefile:
            print(state + ":2,2,2", end="\n", file=statefile)

def aimove(board):
    boardState = ""
    boardState += "".join(board[0]) + "".join(board[1]) + "".join(board[2])
    statecheck(boardState)
