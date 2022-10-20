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


for fileName in range(1):
    startMatrix = fileToMatrix(open("./start/" + str(fileName) + ".txt", "r"))
    endMatrix = fileToMatrix(open("./end/" + str(fileName) + ".txt", "r"))

    print(findMisplaced(startMatrix, endMatrix))
