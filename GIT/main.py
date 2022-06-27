class gameEND(Exception):
    pass


import random

board = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"],
]

playerPositions = [[2, 0], [2, 1], [2, 2]]
computerPositions = [[0, 0], [0, 1], [0, 2]]
possibleMoves = {}
computerPossibleMoves = {}


def drawBoard():
    print(f"""
        0   1   2

0       {board[0][0]}   {board[0][1]}   {board[0][2]}
1       {board[1][0]}   {board[1][1]}   {board[1][2]}    
2       {board[2][0]}   {board[2][1]}   {board[2][2]}


    """)


def drawPawns():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if [i, j] in playerPositions:
                board[i][j] = "G"
            elif [i, j] in computerPositions:
                board[i][j] = "C"
            else:
                board[i][j] = "O"

    for space in board:
        print(space)


drawPawns()


def checkMoves():
    possibleMoves.clear()
    for position in playerPositions:
        position = tuple(position)
        possibleMoves[position] = []
        if board[position[0] - 1][position[1]] == "O":
            possibleMoves[position].append([position[0] - 1, position[1]])

        try:
            if position[0] - 1 >= 0 and position[1] - 1 >= 0:
                if board[position[0] - 1][position[1] - 1] == "C":
                    possibleMoves[position].append([position[0] - 1, position[1] - 1])
            if position[0] - 1 >= 0:
                if board[position[0] - 1][position[1] + 1] == "C":
                    possibleMoves[position].append([position[0] - 1, position[1] + 1])

        except IndexError:
            pass
        if possibleMoves[position] == []:
            possibleMoves.pop(position)


def chooseMove():
    i = 1
    j = 1
    for key in possibleMoves:
        print(i, key)
        i += 1
    pawn = int(input("Którym pionkiem chcesz się ruszyć? "))
    pawn = list(possibleMoves.keys())[pawn - 1]
    print(pawn)
    for move in possibleMoves[pawn]:
        print(j, move)
        j += 1
    position_nr = int(input("Na które miejsce chcesz się ruszyć? "))
    print(possibleMoves[pawn])
    playerPositions[playerPositions.index(list(pawn))] = possibleMoves[pawn][position_nr - 1]


def checkComputerMoves():
    computerPossibleMoves.clear()
    for position in computerPositions:
        position = tuple(position)
        computerPossibleMoves[position] = []
        if board[position[0] + 1][position[1]] == "O":
            computerPossibleMoves[position].append([position[0] + 1, position[1]])

        try:
            if position[0] - 1 >= 0 and position[1] - 1 >= 0:
                if board[position[0] + 1][position[1] - 1] == "G":
                    computerPossibleMoves[position].append([position[0] + 1, position[1] - 1])
            if position[0] + 1 >= 0:
                if board[position[0] + 1][position[1] + 1] == "G":
                    computerPossibleMoves[position].append([position[0] + 1, position[1] + 1])
        except IndexError:
            pass
        if computerPossibleMoves[position] == []:
            computerPossibleMoves.pop(position)
    print(computerPossibleMoves)


def chooseComputerMove():
    pawn = list(computerPossibleMoves)[(random.randint(0, len(computerPossibleMoves) - 1))]
    print(f'pawn: {pawn}')
    move = computerPossibleMoves[pawn][random.randint(0, len(computerPossibleMoves[pawn]) - 1)]
    print(f'pawn: {pawn} -> move: {move}')
    computerPositions[computerPositions.index(list(pawn))] = move


def checkWinConditions():
    if "G" in board[0]:
        print("Players Win!")
        raise gameEND
    if "C" in board[2]:
        print("Computer Win!")
        raise gameEND
    if possibleMoves == {}:
        print("Computer Win!")
        raise gameEND
    if computerPossibleMoves == {}:
        print("Players Win!")
        raise gameEND


checkComputerMoves()
# checkMoves()
# print(playerPositions)
# print(possibleMoves)
# drawBoard()
# chooseMove()
# drawPawns()
# drawBoard()
# checkMoves()
# print(possibleMoves)
# chooseMove()
# drawPawns()

while True:
    try:

        drawPawns()
        drawBoard()
        checkMoves()
        chooseMove()
        drawPawns()
        checkWinConditions()
        checkComputerMoves()
        chooseComputerMove()
        drawPawns()
        checkWinConditions()
    except gameEND:
        print("Koniec!!!")
        exit()
