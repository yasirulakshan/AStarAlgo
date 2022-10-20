import copy

from matrix import Matrix


def fileToMatrix(file):
    arr = []
    lines = file.read().split("\n")
    for line in lines:
        arr.append(line.split())
    return arr


def findMisplaced(start, final):
    h = 0
    for i in range(len(start)):
        for j in range(len(start)):
            if start[i][j] != "-" and start[i][j] != final[i][j]:
                h += 1
    return h


def findIndex(arr, element):
    size = len(arr)
    for i in range(size):
        for j in range(size):
            if arr[i][j] == element:
                return [i, j]


def findManhattan(start, final):
    h = 0
    size = len(start)
    for i in range(size):
        for j in range(size):
            if start[i][j] != "-" and start[i][j] != final[i][j]:
                finalIndex = findIndex(final, start[i][j])
                h += (abs(i - finalIndex[0]) + abs(j - finalIndex[1]))
    return h


for fileName in range(1):
    startMatrix = fileToMatrix(open("./start/" + str(fileName) + ".txt", "r"))
    endMatrix = fileToMatrix(open("./end/" + str(fileName) + ".txt", "r"))

    print(findManhattan(startMatrix, endMatrix))
