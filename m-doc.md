---
layout: page
title: MATLAB
permalink: /MATLAB/
categories: media
---

# genMaze 
---

Generate a maze with given parameters. See [MazeAlgo_main.mlx](https://github.com/tulimid1/Maze_Task/blob/main/MazeAlgo_main.mlx) for a notebook of given examples. 

## Syntax
---
[genMaze(num_turns, path_length)](#a)

[genMaze(num_turns, path_length, Name, Value)](#b)

## Description
---
### A
genMaze([num_turns](#num_turns), [path_length](#path_length)) returns a random maze with specified number of turns and path length in a 10x10 space. [example](#general-maze)

### B
genMaze([num_turns](#num_turns), [path_length](#path_length), [Name, Value)](#name-value-arguments) returns a random maze with additional options specified by one or more name-value pair arguments. For example, you can change the number of iterations or size of grid. [example](#more-complicated-maze-with-more-iterations)

## Examples 
---
### General maze
Generate a general maze 

    num_turns = 5;
    path_length = 10; 
    genMaze(num_turns, path_length)
    
<img src="https://github.com/tulimid1/Maze_Task/blob/gh-pages/assets/gen.png" width=400 height="350"/>
    
### More complicated maze with more iterations
Generate a maze that has only one more length than it does turns, 

    num_turns = 15;
    path_length=16;
    genMaze(num_turns, path_length, 'maxIter',1e3)
    
<img src="https://github.com/tulimid1/Maze_Task/blob/gh-pages/assets/comp.png" width=400 height="350"/>

### Maze that isn't a square
Generate a maze that doesn't have the same size width and height.

    num_turns = 5;
    path_length=10;
    gridX = 15;
    genMaze(num_turns, path_length, 'gridX',gridX)
    
<img src="https://github.com/tulimid1/Maze_Task/blob/gh-pages/assets/rect.png" width=400 height="350"/>

## Input Arguments
---
### ```num_turns```
Number of turns

Number of non-overlapping turns the maze should have. 

Data Types: double | scalar

### ```path_length```
Length of the path.

The number of the blocks the maze should go across. 

Data Types: double | scalar

### Name-Value Arguments

Specified optional comma-separated pairs of ```Name,Value``` arguments. ```Name``` is the is the argument name and ```Value``` is the corresponding value. ```Name``` musta ppear inside single or double quotes. You can specify several name and value pair arguments in any order as ```Name1,Value1,...,NameN,ValueN```. 

**Example**: ```'gridX', 15, 'maxIter', 500``` specifies a maze with 15 columns and 500 iterations to try to converge.

### ```gridX```
Number of blocks on x-dimension. 

How many blocks for wide. 

Data Types: double | scalar

### ```gridY```
Number of blocks on y-dimension.

How many blocks tall. 

Data Types: double | scalar

### ```maxIter```
Maximum iterations to test

How many attempts to make a maze with given parameters. This may need to be increased for more complicated mazes. 

## More About 
---

## Tips 
---

