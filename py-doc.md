---
layout: page
title: Python
permalink: /Python/
---

# GenerateAndTest
---

Generate a random maze. See [MazeAlgo_main.ipynb](https://github.com/tulimid1/Maze_Task/blob/main/MazeAlgo_main.ipynb) for a notebook of given examples. 

## Syntax
---

[GenerateAndTest(numTurns, pathLength)](#a)

[GenerateAndTest(numTurns, pathLength, Name=Value](#b)

## Description
---
### A
GenerateAndTest([numTurns](#numturns), [pathLength](#pathlength)) returns a random maze with specified number of turns and path length in a 10x10 space. [example](#general-maze)

### B 
GenerateAndTest([numTurns](#numturns), [pathLength](#pathlength), [Name=Value](#name-value-arguments)) returns a random maze with additional options specified by one or more name-value pair arguments. For example, you can change the number of iterations or size of grid. [example](#more-complicated-maze-with-more-iterations)

## Examples 
---
### General maze
Generate a general maze

    code

More description 

    code

### More complicated maze with more iterations

### Maze that isn't a square

## Input Arguments
---
### ```numTurns```
Number of turns.

Number of non-overlapping turns the maze should have. 

Data Types: double | scalar

### ```pathLength```
Length of the path.

The number of blocks the maze shoudl go across. 

Data Types: double | scalar

### Name-Value Arguments

Specified optional pairs of ```Name=Value``` arguments. ```Name``` is the is the argument name and ```Value``` is the corresponding value. You can specify several name and value pair arguments in any order as ```Name1=Value1,...,NameN=ValueN```. 

**Example**: ```gridX=15, maxIter=500``` specifies a maze with 15 columns and 500 iterations to try to converge. 

### ```gridX```
Number of blocks on x-dimension. 

How many blocks wide. 

Data Types: double | scalar

### ```gridY```
Number of blocks on y-dimension. 

How many blocks wide. 

Data Types: double | scalar

### ```maxIter```
Maximum iterations to test.

How many attempts to make a maze with given parameters. This may need to be increased for more complicated mazes. 

## More About 
---

## Tips 
---
