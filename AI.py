from random import randint
import os

weightindex = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
states = {}
statesplayed = {}


def aisave():
    global statesplayed
    global states
    with open("states.txt", "w") as statefile:
        for state, weights in zip(states.keys(), states.values()):
            print(state + ":" + weights, end="\n", file=statefile)
    statesplayed = {}


def aiadjust(outcome):
    #print(statesplayed)
    for state in statesplayed.keys():
        weights = states[state].split(",")
        weights = [int(i) for i in weights]
        #print(statesplayed.keys())
        #print(str(weights[statesplayed[state]]) + " " + str(statesplayed[state]) + " " + str(len(weights)))
        if outcome == 0:
            for i in range(0, 2):
                for x in range(0, len(weights) - 1):
                    if weights[x] == weights[statesplayed[state]]:
                        weights.pop(x)
                        statesplayed[state] -= 1
                        break
        elif outcome == 1:
            weights.append(weights[statesplayed[state]])
            weights.append(weights[statesplayed[state]])
        elif outcome == 2:
            weights.append(weights[statesplayed[state]])
        weights = [str(i) for i in weights]
        states[state] = ",".join(weights)
        #check the outcome of the game
        #adjust the weight in question
        #adjust the other weights - if they go below 0, make them 0
        #Think about the weight system, is it really that good, maybe change it up to the old version - create an algorithm which could work with that?
    aisave()


def aiload():
    if os.path.getsize("states.txt") > 0:
        with open("states.txt", "r") as statefile:
            for state in statefile:
                stateArr = state.strip().split(":")
                stateArr[1] = stateArr[1].strip(":")
                states[stateArr[0]] = stateArr[1]


def statecheck(state):
    alreadySeen = False
    for i in states.keys():
        if i == state:
            alreadySeen = True
    if not alreadySeen:
        states[state] = ""
        for i in range(0, 9):
            states[state] += str(i) + "," + str(i)
            if i != 8:
                states[state] += ","
    return alreadySeen


def aimove(board):
    boardState = "".join(board[0]) + "".join(board[1]) + "".join(board[2])
    statecheck(boardState)
    weights = states[boardState].split(",")
    weights = [int(i) for i in weights]
    positionFound = False
    position = 0
    while not positionFound:
        position = randint(0, len(weights) - 1)
        boardLocation = weightindex[int(weights[position])]
        if board[boardLocation[1]][boardLocation[0]] != "X" and board[boardLocation[1]][boardLocation[0]] != "O":
            board[boardLocation[1]][boardLocation[0]] = "X"
            statesplayed[boardState] = position
            positionFound = True
    return board