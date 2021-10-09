# Maze Generation Algorithm Documentation 

This repository holds the code used to generate single path randomized mazes based off two important parameters: number of turns and path length. The code has been provided in MATLAB and Python. 

In general, the maze algorithm utilizes two functions: (From MATLAB code)

Generate Maze function 

__Inputs__: number of turns (num_turns), number of blocks / spaces to travel (path_length), x maximum (gridX), Y maximum (gridY), and maximum number of iterations (maxIter)

__Output__: Visualization of maze 

> noPath = True
> while noPath:
>> Create an array random directions that satisifies num_turns and path_length called *directions*
>> Randomly choose a starting location, called *agent_position*
>> for i in *directions*:
>>> Calculate new position and append to *agent_position*
>> if *agent_position* overlaps:
>>> noOverlap = False 
>>> break 
>> else:
>>> noOverlap = True 
>> if *agent_position* within grid bounds:
>>> withinBounds = True
>> else:
>>> withinBounds = False
>> if noOverlap and not withinBounds:
>>> Shift maze position to try to get within bounds 
>> if noOverlap and withinBounds:
>>> noPath = False
>>> Plot maze 
>>> break

Below is the python code within [Google Colab Notebook](https://colab.research.google.com/drive/1hKHnlq2hOVKw1-x4CG4hURgCfPhSdJ1N?usp=sharing).
