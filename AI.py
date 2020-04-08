from random import randint

weightindex = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
states = {}
statesplayed = {}


def aisave():
    with open("states.txt", "w") as statefile:
        for state, weights in zip(states.keys(), states.values()):
            print(state + ":" + weights, end="\n", file=statefile)


def aiadjust(won):
    for state in statesplayed.keys():
        weights = states[state].split(";")
        weights = [weights[0].split(","), weights[1].split(","), weights[2].split(",")]
        weights[0][0] = weights[0][0].strip(":")
        print(weights)
        #check the outcome of the game
        #adjust the weight in question
        #adjust the other weights - if they go below 0, make them 0
        #Think about the weight system, is it really that good, maybe change it up to the old version - create an algorithm which could work with that?
        aisave()


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
        states[state] = ":2,4,6;8,10,12;14,16,18"
    return alreadySeen


def aimove(board):
    x = 0
    y = 0
    boardState = ""
    boardState += "".join(board[0]) + "".join(board[1]) + "".join(board[2])
    statecheck(boardState)
    weights = states[boardState].strip(":").split(";")
    weights = weights[0].split(",") + weights[1].split(",") + weights[2].split(",")
    weights = [int(i) for i in weights]
    weights.insert(0, 0)
    position = 0
    positionfound = False
    while not positionfound:
        position = randint(0, weights[9])
        for i in range(1, 10):
            if weights[i - 1] <= position < weights[i]:
                if board[weightindex[i - 1][1]][weightindex[i - 1][0]] != "X" or board[weightindex[i - 1][1]][weightindex[i - 1][0]] != "O":
                    x = weightindex[i - 1][0]
                    y = weightindex[i - 1][1]
                    board[weightindex[i - 1][1]][weightindex[i - 1][0]] = "X"
                    position = i - 1
                    positionfound = True
    statesplayed[boardState] = position
    return board
