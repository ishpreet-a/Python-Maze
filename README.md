A random maze generator and solver system built in Python

File Hierarchy
MazeRunner              - host the program
|__ MazeMenu            - Manage input and execution for the program
    |__ Maze            - class to manage maze
    |__ MazeGen         - maze generation algorithm
    |   |__ StackMan    - stack manager for maze generator
    |
    |__ BFS             - solve the maze using breadth-first-search algorithm
    |   |__ QueueMan    - queue manager for BFS
    |
    |__ AStar           - solve the maze using A* formula
       |__ PQueueMan    - priority queue manage for BFS

