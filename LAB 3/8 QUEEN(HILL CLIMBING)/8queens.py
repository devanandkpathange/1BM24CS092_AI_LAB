
from random import randint

N = 8

def configureRandomly(board, state):
    for i in range(N):
        state[i] = randint(0, N - 1)
        board[state[i]][i] = 1

def printBoard(board):
    for row in board:
        print(*row)

def calculateObjective(board, state):
    attacking = 0

    for i in range(N):
        for j in range(i + 1, N):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                attacking += 1

    return attacking

def generateBoard(board, state):
    for i in range(N):
        for j in range(N):
            board[i][j] = 0

    for i in range(N):
        board[state[i]][i] = 1

def getNeighbour(board, state):
    opState = state[:]
    opObjective = calculateObjective(board, state)

    for i in range(N):
        for j in range(N):
            if j != state[i]:
                tempState = state[:]
                tempState[i] = j

                tempBoard = [[0] * N for _ in range(N)]
                generateBoard(tempBoard, tempState)

                temp = calculateObjective(tempBoard, tempState)

                if temp <= opObjective:
                    opObjective = temp
                    opState = tempState

    state[:] = opState
    generateBoard(board, state)

def hillClimbing(board, state):
    neighbourState = state[:]
    neighbourBoard = [[0] * N for _ in range(N)]

    while True:
        state[:] = neighbourState
        generateBoard(board, state)

        getNeighbour(neighbourBoard, neighbourState)

        if state == neighbourState:
            printBoard(board)
            break

        elif (calculateObjective(board, state) ==
              calculateObjective(neighbourBoard, neighbourState)):

            neighbourState[randint(0, N - 1)] = randint(0, N - 1)
            generateBoard(neighbourBoard, neighbourState)

state = [0] * N
board = [[0] * N for _ in range(N)]

configureRandomly(board, state)
hillClimbing(board, state)
