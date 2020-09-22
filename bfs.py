import math
import os
from collections import deque
import time

import psutil
from Tools.scripts.treesync import raw_input


class Board:
    def __init__(self, tiles):
        self.size = int(math.sqrt(len(tiles)))
        self.tiles = tiles

    def moves(self, move):
        size = self.size
        newTiles = self.tiles
        emptyTile = newTiles.index('0')
        if move == "R":
            if emptyTile % size < (size - 1):
                temp = newTiles[emptyTile + 1], newTiles[emptyTile]
                newTiles[emptyTile], newTiles[emptyTile + 1] = temp

        if move == "L":
            if emptyTile % size > 0:
                temp = newTiles[emptyTile - 1], newTiles[emptyTile]
                newTiles[emptyTile], newTiles[emptyTile - 1] = temp

        if move == "D":
            if emptyTile + size < size * size:
                temp = newTiles[emptyTile + size], newTiles[emptyTile]
                newTiles[emptyTile], newTiles[emptyTile + size] = temp

        if move == "U":
            if emptyTile - size >= 0:
                temp = newTiles[emptyTile-size], newTiles[emptyTile]
                newTiles[emptyTile], newTiles[emptyTile-size] = temp

        return Board(newTiles)


class Node:
    def __init__(self, nodeState, nodeParent, move):
        self.nodeState = nodeState
        self.nodeParent = nodeParent
        self.move = move

    def __repr__(self):
        return str(self.nodeState.tiles)

    def __eq__(self, other):
        return self.nodeState.tiles == other.nodeState.tiles


def finalGoal(finalTiles):
    return finalTiles == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '0']


def path(node):
    pathList = []
    while node.nodeParent is not None:
        pathList.append(node.move)
        node = node.nodeParent
    pathList.reverse()
    return pathList


def BFS(rootNode):
    startTime = time.time()
    frontier = deque([rootNode])
    exploredNodes = []
    nodeCount = 0
    children = []
    movesList = ['R', 'L', 'D', 'U']

    while len(frontier) > 0:
        currentNode = frontier.popleft()
        nodeCount = nodeCount + 1
        exploredNodes.append(currentNode)

        if finalGoal(currentNode.nodeState.tiles):
            graphPath = path(currentNode)
            endTime = time.time()
            finalTime = endTime-startTime
            return graphPath, nodeCount, finalTime

        for move in movesList:
            childState = currentNode.nodeState.moves(move)
            childNode = Node(childState, currentNode, move)
            children.append(childNode)

        for child in children:
            if child in exploredNodes: continue
            else:
                frontier.append(child)

    return False


if __name__ == "__main__":
    process = psutil.Process(os.getpid())
    initialMemory = process.memory_info().rss / 1024.0
    init = str(raw_input("Begin State: "))
    initialList = init.split(' ')
    rootNode = Node(Board(initialList), None, None)
    BFSResult = BFS(rootNode)
    print(BFSResult)
    finalMemory = process.memory_info().rss / 1024.0
    totalMemory = finalMemory - initialMemory
    print('Total memory used: ' + str(totalMemory) + ' KB')






