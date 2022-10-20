import copy

from matrix import Matrix


def fileToMatrix(file):
    arr = []
    lines = file.read().split("\n")
    for line in lines:
        arr.append(line.split())
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


for fileName in range(1):
    startMatrix = fileToMatrix(open("./start/" + str(fileName) + ".txt", "r"))
    endMatrix = fileToMatrix(open("./end/" + str(fileName) + ".txt", "r"))

    h = findManhattan(startMatrix, endMatrix)
    # h = findMisplaced(startMatrix,endMatrix)

    stack = [Matrix(startMatrix, 0, h)]
    finalized = []

    print(findDash(stack[0].values))
