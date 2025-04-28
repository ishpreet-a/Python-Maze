#!/bin/python3
from enum import Enum
import random
from Coord2D import Coord2D

class Directions(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    BACK = 4
#

def rand(a, b=0):
    if b == 0:
        return random.randint(0, a)
    #
    else:
        return random.randint(a, b)
    #
#

class Maze:
    # functions
    # x is width, y is height
    def __init__(self, h, w):
        self.height = h
        self.width = w
        self.maze = []
        self.exit:Coord2D
        self.stack = []
        self.direction = Directions.BACK
        self.wall = '@'
        self.path = ' '
    #

    def Init(self):
        self.maze = []
        for h in range(0,self.height):
            self.maze.append([self.wall]*(self.width))
        #
        # pick a side of the maze to make the enterence
        side = rand(3)
        
        x:int
        y:int

        # side: 0=top, 1=right, 2=bottom, 3=left
        match side:
            case 0:
                x = 1+2*rand(int(self.width/2)-1)
                y = 1
                self.maze[0][x] = self.path
            case 1:
                x = self.width-2
                y = 1+2*rand(int(self.height/2)-1)
                self.maze[y][self.width-1] = self.path
            case 2:
                x = 1+2*rand(int(self.width/2)-1)
                y = self.height-2
                self.maze[self.height-1][x] = self.path
            case 3:
                x = 1
                y = 1+2*rand(int(self.height/2)-1)
                self.maze[y][0] = self.path
            case _:
                exit(1)
            #
        #
        self.maze[y][x] = self.path
        self.exit = Coord2D(x, y)
        self.stack.append(self.exit)
        self.maze[self.exit.y][self.exit.x] = self.path
        print(self.exit.x, self.exit.y)
        return
    #
    
    def Print(self):
        for i in range(self.height):
            row = self.maze[i]
            rowSum = "";
            for char in row:
                rowSum += char
            print(rowSum)
        #
    #

    def GetAvailDir(self, x, y):
        availDirs = [0]*4
        if y-2 > 0: # up
            if self.maze[y-2][x] == self.wall:
                availDirs[0] = random.random()
            #
        #
        if x+2 < self.width: # right
            if self.maze[y][x+2] == self.wall:
                availDirs[1] = random.random()
            #
        #
        if y+2 < self.height: # down
            if self.maze[y+2][x] == self.wall:
                availDirs[2] = random.random()
            #
        #
        if x-2 > 0: # left
            if self.maze[y][x-2] == self.wall:
                availDirs[3] = random.random()
            #
        #

        if max(availDirs) == 0:
            return Directions.BACK
        else:
            return Directions(availDirs.index(max(availDirs)))
        #
    #

    def MoveDir(self, dir, x, y):

        match dir.value:
            case 0:
                self.maze[y-1][x] = self.path
                self.maze[y-2][x] = self.path
                self.stack.append(Coord2D(x, y-2))
                return x, y-2
            case 1:
                self.maze[y][x+1] = self.path
                self.maze[y][x+2] = self.path
                self.stack.append(Coord2D(x+2, y))
                return x+2, y
            case 2:
                self.maze[y+1][x] = self.path
                self.maze[y+2][x] = self.path
                self.stack.append(Coord2D(x, y+2))
                return x, y+2
            case 3:
                self.maze[y][x-1] = self.path
                self.maze[y][x-2] = self.path
                self.stack.append(Coord2D(x-2, y))
                return x-2, y
            case 4:
                last_point = self.stack.pop()
                return last_point.x, last_point.y
            case _:
                print("WTF happened in Maze:MoveRandomDir():maxIndex: out of range")
                exit()
            #
        #
    #
    def Generate(self):
        self.Init()
        x, y = self.exit.x, self.exit.y

        #for _ in range(0, 5):
        dir = self.GetAvailDir(x, y)

        while self.stack:
            x, y = self.MoveDir(dir, x, y)
            dir = self.GetAvailDir(x, y)
            #print("x, y: %s, %s" %(x, y))
        #
        return
    #
#


maze = Maze(13, 9)
maze.Generate()
maze.Print()

