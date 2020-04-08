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
        #print(state)
        weights = states[state].split(";")
        #print(weights)
        weights = [weights[0].split(","), weights[1].split(","), weights[2].split(",")]
        weights[0][0] = weights[0][0].strip(":")
        currentWeight = int(weights[weightindex[statesplayed[state]][1]][weightindex[statesplayed[state][0]]])
        if won == 0:
            if currentWeight - 2 < 0:
                weights[weightindex[statesplayed[state]][1]][weightindex[statesplayed[state][0]]] = "0"
            else:
                weights[weightindex[statesplayed[state]][1]][weightindex[statesplayed[state][0]]] = str(currentWeight - 2)
        if won == 1:
            weights[weightindex[statesplayed[state]][1]][weightindex[statesplayed[state][0]]] = str(currentWeight + 1)
        if won == 2:
            weights[weightindex[statesplayed[state]][1]][weightindex[statesplayed[state][0]]] = str(currentWeight + 2)
        weights = [",".join(weights[0]), ",".join(weights[1]), ",".join(weights[2])]
        weights = ";".join(weights)
        states[state] = weights
        #print(weights)
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
