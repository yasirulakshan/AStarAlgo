import copy
import sys

from matrix import Matrix


def fileToMatrix(file):
    arr = []
    lines = file.read().strip().split("\n")
    for line in lines:
        arr.append(line.strip().split())
    return arr


def findMisplaced(arr, final):
    h = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != "-" and arr[i][j] != final[i][j]:
                h += 1
    return h


def findIndex(arr, element):
    size = len(arr)
    for i in range(size):
        for j in range(size):
            if arr[i][j] == element:
                return [i, j]


def findManhattan(arr, final):
    h = 0
    size = len(arr)
    for i in range(size):
        for j in range(size):
            if arr[i][j] != "-" and arr[i][j] != final[i][j]:
                finalIndex = findIndex(final, arr[i][j])
                h += (abs(i - finalIndex[0]) + abs(j - finalIndex[1]))
    return h


def findDash(arr):
    length = len(arr)
    dashed = []
    for i in range(length):
        for j in range(length):
            if arr[i][j] == "-":
                dashed.append([i, j])
    return dashed


def findH(arr, final):
    # h = findManhattan(arr, final)
    h = findMisplaced(arr, final)
    return h


def move(matrix):
    arr = matrix.values
    g = matrix.g
    moved = matrix.lastMoved
    dash = findDash(arr)
    lastIndex = len(arr) - 1
    posibleMatrixes = []

    for i in range(len(dash)):
        if dash[i][0] - 1 >= 0 and [dash[i][0] - 1, dash[i][1]] != moved and arr[dash[i][0] - 1][dash[i][1]] != "-":
            tempArr = copy.deepcopy(arr)
            tempArr[dash[i][0]][dash[i][1]] = tempArr[dash[i][0] - 1][dash[i][1]]
            tempArr[dash[i][0] - 1][dash[i][1]] = "-"
            posibleMatrixes.append(
                Matrix(tempArr, g + 1, findH(tempArr, endMatrix), matrix, dash[i],
                       [tempArr[dash[i][0]][dash[i][1]], "Down"]))

        if dash[i][1] - 1 >= 0 and [dash[i][0], dash[i][1] - 1] != moved and arr[dash[i][0]][dash[i][1] - 1] != "-":
            tempArr = copy.deepcopy(arr)
            tempArr[dash[i][0]][dash[i][1]] = tempArr[dash[i][0]][dash[i][1] - 1]
            tempArr[dash[i][0]][dash[i][1] - 1] = "-"
            posibleMatrixes.append(
                Matrix(tempArr, g + 1, findH(tempArr, endMatrix), matrix, dash[i],
                       [tempArr[dash[i][0]][dash[i][1]], "Right"]))

        if dash[i][0] + 1 <= lastIndex and [dash[i][0] + 1, dash[i][1]] != moved and arr[dash[i][0] + 1][
            dash[i][1]] != "-":
            tempArr = copy.deepcopy(arr)
            tempArr[dash[i][0]][dash[i][1]] = tempArr[dash[i][0] + 1][dash[i][1]]
            tempArr[dash[i][0] + 1][dash[i][1]] = "-"
            posibleMatrixes.append(
                Matrix(tempArr, g + 1, findH(tempArr, endMatrix), matrix, dash[i],
                       [tempArr[dash[i][0]][dash[i][1]], "Up"]))

        if dash[i][1] + 1 <= lastIndex and [dash[i][0], dash[i][1] + 1] != moved and arr[dash[i][0]][
            dash[i][1] + 1] != "-":
            tempArr = copy.deepcopy(arr)
            tempArr[dash[i][0]][dash[i][1]] = tempArr[dash[i][0]][dash[i][1] + 1]
            tempArr[dash[i][0]][dash[i][1] + 1] = "-"
            posibleMatrixes.append(
                Matrix(tempArr, g + 1, findH(tempArr, endMatrix), matrix, dash[i],
                       [tempArr[dash[i][0]][dash[i][1]], "Left"]))

    return posibleMatrixes


def findMinMatrixes(matrixes):
    f = sys.maxsize
    result = []
    ifFinalized = False
    for matrix in matrixes:
        if matrix.h == 0:
            result = [matrix]
            ifFinalized = True
            break
        if matrix.f < f:
            result = [matrix]
            f = matrix.f
        elif matrix.f == f:
            result.append(matrix)

    return result, ifFinalized


outputs = []

for fileName in range(100):
    startMatrix = fileToMatrix(open("./start/" + str(fileName) + ".txt", "r"))
    endMatrix = fileToMatrix(open("./end/" + str(fileName) + ".txt", "r"))

    h = findH(startMatrix, endMatrix)

    stack = [Matrix(startMatrix, 0, h, None)]
    final = None
    isEnd = False

    while not isEnd:
        fMinMatrixes, isEnd = findMinMatrixes(stack)
        if isEnd:
            final = fMinMatrixes[0]
        else:
            for matrix in fMinMatrixes:
                stack.remove(matrix)
                stack += move(matrix)

    out = []

    while final.parent:
        out.append(final.movement)
        final = final.parent

    print(out)

    outputs.append(out.reverse())


for out in outputs:
    print(" ".join(out))
