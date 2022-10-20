import copy

from matrix import Matrix


def fileToMatrix(file):
    arr = []
    lines = file.read().split("\n")
    for line in lines:
        arr.append(line.split())
    return arr


for fileName in range(1):
    startMatrix = fileToMatrix(open("./start/" + str(fileName) + ".txt", "r"))
    endMatrix = fileToMatrix(open("./end/" + str(fileName) + ".txt", "r"))
    print(startMatrix)
    print(endMatrix)
