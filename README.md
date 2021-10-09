# Maze Generation Algorithm Documentation 

This repository holds the code used to generate single path randomized mazes based off two important parameters: number of turns and path length. The code has been provided in MATLAB and Python. 

In general, the maze algorithm utilizes two functions: (From MATLAB code)

Generate Maze function 

__Inputs__: number of turns (num_turns), number of blocks / spaces to travel (path_length), x maximum (gridX), Y maximum (gridY), and maximum number of iterations (maxIter)

__Output__: Visualization of maze 

Steps in which a single path maze is randomly generated with this algorthim are as followed:

1. The dimensions of the grid in which the maze will be displayed within is created. The X,Y grid dimensions can be changed to any desired size.
2. The start location of the maze has randomized X and Y-cooridnate locations within the bounds of the grid.
3. The direction types: north, east, south, west are assigned as variables.
4. The starting path of the maze was created from the randomized start location and then randomized to indicate which direction the path will start.
5. The remaining path was generated from the specified input parameters.
6. The finish location of the maze will be where the last grid unit/blocks/space of the path ends.
7. If the maze at any points does not meet the parameters, does not stays within the bounds of the grid or the path overlaps, then the maze algorthim will keep generating mazes until all specifications/parameters are met.

Below is the python code within [Google Colab Notebook](https://colab.research.google.com/drive/1hKHnlq2hOVKw1-x4CG4hURgCfPhSdJ1N?usp=sharing):
