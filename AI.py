from random import randint

states = {}
statesplayed = {}

def formatstates():
    for state in statesplayed.keys():
        formattedWeights = []
        weightTotal = 0
        weights = states[state].split(";")
        weights = ",".join(weights)
        weights = weights.strip(":")
        weights = weights.split(",")
       #print(weights)
        for weight in weights:
            weightTotal += int(weight)
            formattedWeights.append(str(weightTotal))
        formattedWeights = ",".join(formattedWeights[0:3]) + ";" + ",".join(formattedWeights[3:6]) + ";" + ",".join(formattedWeights[6:9])
        states[state] = formattedWeights


def aisave():
    with open("states.txt", "w") as statefile:
        for state, weights in zip(states.keys(), states.values()):
            print(state + ":" + weights, end="\n", file=statefile)

def aiadjust(won):
    for state in statesplayed.keys():
        print(state)
        weights = states[state].split(";")
        #print(weights)
        weights = [weights[0].split(","), weights[1].split(","), weights[2].split(",")]
        weights[0][0] = weights[0][0].strip(":")
        if won == 0:
            weights[statesplayed[state][1]][statesplayed[state][0]] = str(int(weights[statesplayed[state][1]][statesplayed[state][0]]) - 2)
            if int(weights[statesplayed[state][1]][statesplayed[state][0]]) < 0:
                weights[statesplayed[state][1]][statesplayed[state][0]] = "0"#This also is not working
        if won == 1:
            weights[statesplayed[state][1]][statesplayed[state][0]] = str(int(weights[statesplayed[state][1]][statesplayed[state][0]]) + 2)
        if won == 2:
            weights[statesplayed[state][1]][statesplayed[state][0]] = str(int(weights[statesplayed[state][1]][statesplayed[state][0]]) + 1)
        weights = [",".join(weights[0]), ",".join(weights[1]), ",".join(weights[2])]
        weights = ";".join(weights)
        states[state] = weights#Fix the problem that weights are becoming super high for no reason
        print(weights)
        formatstates()
        aisave()

def aiload():
    with open("states.txt", "r") as statefile:
        for state in statefile:
            stateArr = state.strip().split(":")
            deformattedWeights = []
            weights = stateArr[1].split(";")
            weights = (",".join(weights)).split(",")
            deformattedWeights.append(weights[0])
            for i in range(1, 9):
                deformattedWeights.append(str(int(weights[i]) - int(weights[i - 1])))
            states[stateArr[0]] = str(",".join(deformattedWeights[0:3])) + ";" + str(",".join(deformattedWeights[3:6]) + ";" + str(",".join(deformattedWeights[6:9])))
            #print(states[stateArr[0]])

def statecheck(state):
    alreadySeen = False
    for i in states.keys():
        if i == state:
            alreadySeen = True
    if not alreadySeen:
        states[state] = ":2,2,2;2,2,2;2,2,2"
    return alreadySeen

def aimove(board):
    x = 0
    y = 0
    boardState = ""
    boardState += "".join(board[0]) + "".join(board[1]) + "".join(board[2])
    statecheck(boardState)
    x = randint(0, 2)
    y = randint(0, 2)
    while board[y][x] != "B":
        x = randint(0, 2)
        y = randint(0, 2)
    board[y][x] = "X"
    statesplayed[boardState] = (x, y)
    return board
