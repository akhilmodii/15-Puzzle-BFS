import os
import time
from collections import deque

import psutil


# Method tp check if two lists are equal.
def checkEQ(list1, list2):
    if list1 == list2:
        return True
    else:
        return False


movesList = []  # Empty List. Will contain all the moves made to reach the solution.
moveValue = ''


# Method to evaluate moves made.
def moves(input):
    list = []
    boardList = eval(input)
    x = 0
    while 0 not in boardList[x]:
        x = x + 1
    y = boardList[x].index(0)

    if x > 0:  # Shifting UP
        boardList[x][y], boardList[x - 1][y] = boardList[x - 1][y], boardList[x][y]
        list.append(str(boardList))
        movesList.append('U')
        # moveValue = 'U'
        boardList[x][y], boardList[x - 1][y] = boardList[x - 1][y], boardList[x][y]

    if x < 3:  # Shifting DOWN
        boardList[x][y], boardList[x + 1][y] = boardList[x + 1][y], boardList[x][y]
        list.append(str(boardList))
        movesList.append('D')
        # moveValue = 'D'
        boardList[x][y], boardList[x + 1][y] = boardList[x + 1][y], boardList[x][y]

    if y > 0:  # Shifting LEFT
        boardList[x][y], boardList[x][y - 1] = boardList[x][y - 1], boardList[x][y]
        list.append(str(boardList))
        movesList.append('L')
        # moveValue = 'L'
        boardList[x][y], boardList[x][y - 1] = boardList[x][y - 1], boardList[x][y]

    if y < 3:  # Shifting RIGHT
        boardList[x][y], boardList[x][y + 1] = boardList[x][y + 1], boardList[x][y]
        list.append(str(boardList))
        movesList.append('R')
        # moveValue = 'R'
        boardList[x][y], boardList[x][y + 1] = boardList[x][y + 1], boardList[x][y]

    return list


class Node:
    def __init__(self, nodeState, nodeParent, move):
        # print('Node init')
        self.nodeState = nodeState
        self.nodeParent = nodeParent
        self.move = move


def path(node):
    pathList = []
    while node.nodeParent not in None:
        pathList.append(node.move)
        node = node.nodeParent
    pathList.reverse()
    return pathList


# Breadth First Search Algorithm
def BFS(initialBoard, finalBoard):
    nodeDict = {}
    visitedList = []
    nodeCount = 0
    list = [[initialBoard]]
    frontier = deque(list)
    # print('Frontier: ' + str(frontier))
    # value = ''

    while True:
        global moveValue
        x = 0
        listElement = list[x]
        list = list[:x] + list[x + 1:]
        lastElement = listElement[-1]
        # currentNode = frontier.popleft()

        for move in moves(lastElement):
            if move in visitedList:
                continue
            else:
                nodeDict[lastElement] = move + moveValue
                moveValue = nodeDict.get(lastElement)
                list.append(listElement + [move])
                # print(moveValue)
        visitedList.append(lastElement)
        nodeCount = nodeCount + 1

        if checkEQ(lastElement, finalBoard):
            # path(currentNode)
            # print(moveValue)
            break
    print('Nodes expanded: ' + str(nodeCount))


# Formats the user input.
def inputFormat(userInput):
    newList = []
    userInput = userInput.replace(" ", ",")
    newUserInput = [str(k) for k in userInput.split(',')]
    newUserInput = list(map(int, newUserInput))
    for i in range(0, len(newUserInput), 4):
        newList.append(newUserInput[i:i + 4])
    return newList


# printing all the moves made to reach the solution.
def printMoves(list):
    for i in range(len(list)):
        print(list[i], end="")
    print('\n')


if __name__ == "__main__":
    userInput = input("Enter initial configuration: ")
    startTime = time.time()
    process = psutil.Process(os.getpid())
    initialMemory = process.memory_info().rss / 1024.0
    newList = inputFormat(userInput)
    initialBoard = str(newList)
    finalBoard = str([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    BFS(initialBoard, finalBoard)
    printMoves(movesList)
    finalMemory = process.memory_info().rss / 1024.0
    totalMemory = finalMemory - initialMemory
    endTime = time.time()
    totalTime = endTime - startTime
    print('Time taken: ' + str(totalTime))
    print('Total Memory used: ' + str(finalMemory) + ' KB')

"""
Inputs: 
1 0 3 4 5 2 6 8 9 10 7 11 13 14 15 12   

1 2 3 4 5 6 8 0 9 11 7 12 13 10 14 15

1 0 2 4 5 7 3 8 9 6 11 12 13 10 14 15

1 2 0 4 6 7 3 8 5 9 10 12 13 14 11 15 

1 3 4 8 5 2 0 6 9 10 7 11 13 14 15 12

"""
