#!/usr/bin/env python

with open("input.txt", "r") as fd:
    lines = fd.read().splitlines()

def newMatrix():
    matrix = [
        [None] * 9,
        [None] * 9,
        [None] * 9,
        [None] * 9,
        [None] * 9,
        [None] * 9,
        [None] * 9,
        [None] * 9,
    ]

    total = 0
    lineNumber = 0
    for lineNumber in range(0, 9):

        chars = list(lines[lineNumber])
        index = 0
        column = 0
        while index < len(chars):
            if chars[index] == '[':
                matrix[lineNumber][column] = chars[index+1]
            index += 4
            column += 1
    return matrix

matrix = newMatrix()

def showPile():
    for i in range(len(matrix)):
        for f in range(len(matrix[i])):
            if matrix[i][f] is None:
                print('_', end='  ')
            else:
                print(matrix[i][f], end='  ')
        print()


def findValid(column):
    global matrix
    i = 0
    for i in range(len(matrix)):
        if matrix[i][column] is not None:
            break

    return i


def moveBoxes(fromColumn, toColumn):
    # find first item
    fromIndex = findValid(fromColumn)
    toIndex = findValid(toColumn)
    if toIndex == 0:
        matrix.insert(0, [None] * 9)
        fromIndex += 1
    else:
        toIndex -= 1

    matrix[toIndex][toColumn] = matrix[fromIndex][fromColumn]
    matrix[fromIndex][fromColumn] = None


def moveBoxesSamePosition(fromColumn, toColumn, amount):
    # find first item
    fromIndex = findValid(fromColumn)
    toIndex = findValid(toColumn)

    diff = amount - toIndex
    if diff > 0:
        for i in range(diff):
            matrix.insert(0, [None] * 9)
            fromIndex += 1
            toIndex += 1

    for newIndex in range(1, amount+1):
        matrix[toIndex-newIndex][toColumn] = matrix[fromIndex +
                                                    (amount-newIndex)][fromColumn]
        matrix[fromIndex+(amount-newIndex)][fromColumn] = None


def getFinalAnswer():
    r = ""
    for i in range(9):
        r += matrix[findValid(i)][i]
    return r

for line in lines[10:]:
    move, moveUnit, fran, fromColumn, to, toColumn = line.split()

    for i in range(int(moveUnit)):
        moveBoxes(int(fromColumn)-1, int(toColumn)-1)
print("First " + str(getFinalAnswer()))

matrix = newMatrix()

for line in lines[10:]:
    move, moveUnit, fran, fromColumn, to, toColumn = line.split()

    moveBoxesSamePosition(int(fromColumn)-1, int(toColumn)-1, int(moveUnit))
print("Second " + str(getFinalAnswer()))

