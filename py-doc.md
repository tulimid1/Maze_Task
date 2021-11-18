---
layout: page
title: Python
permalink: /Python/
---

# [genMaze](https://github.com/tulimid1/Maze_Task/blob/main/MazeGen.py)
---

Generate a random maze. See [MazeAlgo_main.ipynb](https://github.com/tulimid1/Maze_Task/blob/main/MazeAlgo_main.ipynb) for a notebook of given examples. 

## Syntax
---
    import MazeGen as mg

[mg.genMaze(numTurns, pathLength)](#a)

[mg.genMaze(numTurns, pathLength, Name=Value)](#b)

## Description
---
### A
mg.genMaze([numTurns](#numturns), [pathLength](#pathlength)) returns a random maze with specified number of turns and path length in a 10x10 space. [example](#general-maze)

### B 
mg.genMaze([numTurns](#numturns), [pathLength](#pathlength), [Name=Value](#name-value-arguments)) returns a random maze with additional options specified by one or more name-value pair arguments. For example, you can change the number of iterations or size of grid. [example](#more-complicated-maze-with-more-iterations)

## Examples 
---
### General maze
Generate a general maze

    numTurns = 5
    pathLength=10
    mg.genMaze(numTurns=numTurns, pathLength=pathLength)

![gen](/assets/genPy.png)

Algorithm converged.

Number of turns: 5

Path length: 10

Number of iterations: 1

Execution time: 0.16 seconds

### More complicated maze with more iterations
Generate a maze that has only one more length than it does turns.

    numTurns=15
    pathLength=16
    mg.genMaze(numTurns=numTurns, pathLength=pathLength, maxIter=1000)
    
![comp](/assets/compPy.png)

Algorithm converged.

Number of turns: 15

Path length: 16

Number of iterations: 16

Execution time: 2.60 seconds

### Maze that isn't a square
Generate a maze that doesn't have the same size width and height.

    numTurns=5
    pathLength = 10
    gridX=15
    mg.genMaze(numTurns=numTurns, pathLength=pathLength, xMax=gridX)
    
![rect](/assets/rectPy.png)

Algorithm converged.

Number of turns: 5

Path length: 10

Number of iterations: 1

Execution time: 0.31 seconds

## Input Arguments
---
### ```numTurns```
Number of turns.

Number of non-overlapping turns the maze should have. 

Data Types: (double, scalar)

### ```pathLength```
Length of the path.

The number of blocks the maze shoudl go across. 

Data Types: (double, scalar)

### Name-Value Arguments

Specified optional pairs of ```Name=Value``` arguments. ```Name``` is the is the argument name and ```Value``` is the corresponding value. You can specify several name and value pair arguments in any order as ```Name1=Value1,...,NameN=ValueN```. 

**Example**: ```gridX=15, maxIter=500``` specifies a maze with 15 columns and 500 iterations to try to converge. 

### ```gridX```
Number of blocks on x-dimension. 

How many blocks wide. 

Data Types: (double, scalar)

### ```gridY```
Number of blocks on y-dimension. 

How many blocks wide. 

Data Types: (double, scalar)

### ```maxIter```
Maximum iterations to test.

How many attempts to make a maze with given parameters. This may need to be increased for more complicated mazes. 

## More About 
---

## Tips 
---
