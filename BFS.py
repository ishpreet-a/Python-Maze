#!/bin/python3
import time
from Coord2D import Coord2D

class BFS:

    def __init__(self):
        self.maze:list
        self.wall:str
        self.path:str
        self.height:int
        self.width:int
    #

    def FindExit(self):
        entryFound = False

        for i in range(0, self.width):
            char = self.maze[0][i]
            if char == self.path:
                return Coord2D(i, 0)
            #
        #

        for i in range(0, self.width):
            char = self.maze[self.height-1][i]
            if char == self.path:
                return Coord2D(i, self.height-1)
            #
        #

        for i in range(0, self.height):
            char = self.maze[i][0]
            if char == self.path:
                return Coord2D(0, i)
            #
        #

        for i in range(0, self.height):
            char = self.maze[i][self.width-1]
            if char == self.path:
                return Coord2D(self.width-1, i)
            #
        #
        print("Exit not found!")
        print("Quitting")
        exit(1)
    #

    def GetDirs(self, x, y):
        dirs = []
        if y-1 >= 0: # up
            if self.maze[y-1][x] == self.path:
                dirs.append(Coord2D(x, y-1))
            #
        #
        if x+1 < self.width: # right
            if self.maze[y][x+1] == self.path:
                dirs.append(Coord2D(x+1, y))
            #
        #
        if y+1 < self.height: # down
            if self.maze[y+1][x] == self.path:
                dirs.append(Coord2D(x, y+1))
            #
        #
        if x-1 >= 0: # left
            if self.maze[y][x-1] == self.path:
                dirs.append(Coord2D(x-1, y))
            #
        #
        return dirs
    #

    def solve(self, m, w, p, x, y):
        self.maze = m
        self.height, self.width = len(m), len(m[0])
        self.wall, self.path = w, p
        startCoord = Coord2D(x, y)
        exitCoord = self.FindExit()
        #print("exit: %s, %s" % (exitCoord.x, exitCoord.y))
        queue = []
        
        links = {}
        returnPath = []
        current:Coord2D
        queue.append(Coord2D(x, y))
        pathAchieved = False
        

        while queue:
            self.PrintPavedMaze(self.maze, links, startCoord)
            time.sleep(0.5)
            #self.PrintCoordQueue('queue: ', queue)
            current = queue.pop(0)

            #print('current: (%s, %s)'%(current.x, current.y))
            if current == exitCoord:
                print('path achieved')
                pathAchieved = True
                break
            
            for dir in self.GetDirs(current.x, current.y):
                found = False
                for coords in links:
                    if dir == coords:
                        found = True
                if not found:
                    queue.append(dir)
                    links[dir] = current
                    #self.PrintCoordQueue('links: ', links)
                #
            #
        #

        if not pathAchieved:
            print("No path found")
            exit(0)
        #

        i=0
        returnPath.append(current)
        #print('finding exit path')
        while (not current == startCoord) and (i<200):
            current = links[current]
            #print("exit: %s, %s" % (exitCoord.x, exitCoord.y))
            
            returnPath.append(current)
            i += 1
        #

        #self.PrintCoordQueue('returnPath:', returnPath)
        self.PrintPavedMaze(self.maze, returnPath, startCoord)
        return
    #

    def PrintCoordQueue(self, sIn, q):
        s = sIn
        for obj in q:
            s += ('(%s, %s), ' % (obj.x, obj.y))
        print(s)
        return
    
    def PrintPavedMaze(self, m, p, i):
        for coord in p:
            m[coord.y][coord.x] = '*'
        m[i.y][i.x] = '+'
        for row in m:
            s = ''
            for char in row:
                s += char
            #
            print(s)
        #
    #
#

#start
mazeMap = [
    ['@', '@', '@', '@', '@', '@', '@', '@', '@'],
    ['@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '@'],
    ['@', ' ', '@', '@', '@', '@', '@', ' ', '@'],
    ['@', ' ', ' ', ' ', ' ', ' ', '@', ' ', '@'],
    ['@', '@', '@', '@', '@', '@', '@', ' ', '@'],
    ['@', ' ', ' ', ' ', ' ', ' ', '@', ' ', '@'],
    ['@', ' ', '@', '@', '@', ' ', '@', ' ', '@'],
    ['@', ' ', '@', ' ', '@', ' ', '@', ' ', '@'],
    ['@', ' ', '@', ' ', '@', ' ', '@', ' ', '@'],
    ['@', ' ', '@', ' ', '@', ' ', '@', ' ', '@'],
    ['@', ' ', '@', ' ', '@', ' ', '@', ' ', '@'],
    [' ', ' ', '@', ' ', ' ', ' ', ' ', ' ', '@'],
    ['@', '@', '@', '@', '@', '@', '@', '@', '@']
]

bfs = BFS()
bfs.solve(mazeMap, '@', ' ', 3, 11)
