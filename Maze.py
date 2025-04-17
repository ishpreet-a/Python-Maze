#!/bin/python3
from dataclasses import dataclass
import random

class coord2D:
    x, y = 0, 0
    def __init__(self, a, b):
        self.x = a
        self.y = b
    #
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
        self.exit:coord2D
    #



    def Init(self):
        self.maze = []
        for h in range(0,self.height):
            self.maze.append(['X']*(self.width))
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
                self.maze[0][x] = '.'
            case 1:
                x = self.width-2
                y = 1+2*rand(int(self.height/2)-1)
                self.maze[y][self.width-1] = '.'
            case 2:
                x = 1+2*rand(int(self.width/2)-1)
                y = self.height-2
                self.maze[self.height-1][x] = '.'
            case 3:
                x = 1
                y = 1+2*rand(int(self.height/2)-1)
                self.maze[y][0] = '.'
            case _:
                exit(1)
            #
        #
        self.maze[y][x] = '.'
        self.exit = coord2D(x, y)
        self.maze[self.exit.y][self.exit.x] = '.'
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
            if self.maze[y-2][x] == 'X':
                availDirs[0] = random.random()
            #
        #
        if x+2 < self.width: # right
            if self.maze[y][x+2] == 'X':
                availDirs[1] = random.random()
            #
        #
        if y+2 < self.height: # down
            if self.maze[y+2][x] == 'X':
                availDirs[2] = random.random()
            #
        #
        if x-2 > 0: # left
            if self.maze[y][x-2] == 'X':
                availDirs[3] = random.random()
            #
        #

        return availDirs
    #
    def MoveDir(self, dir, x, y):
        maxIndex = availDirs.index(max(availDirs))
        match maxIndex:
            case 0:
                self.maze[y-1][x] = '.'
                self.maze[y-2][x] = '.'
                return x, y-2
            case 1:
                self.maze[y][x+1] = '.'
                self.maze[y][x+2] = '.'
                return x+2, y
            case 2:
                self.maze[y+1][x] = '.'
                self.maze[y+2][x] = '.'
                return x, y+2
            case 3:
                self.maze[y][x-1] = '.'
                self.maze[y][x-2] = '.'
                return x-2, y
            case _:
                print("WTF happened in Maze:MoveRandomDir():maxIndex: out of range")
                exit()
            #
        #
    #
    def Generate(self):
        self.Init()
        x, y = self.exit.x, self.exit.y
        x, y = self.MoveDir(x, y)
        print("x, y: %s, %s" %(x, y))
        return
    #
#


maze = Maze(5, 7)
maze.Generate()
maze.Print()

