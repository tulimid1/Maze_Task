# %% Functions 
def genMaze(numTurns, pathLength, xMax=10, yMax=10, xMin=0, yMin=0, maxIter=250, closePrev=True):
    '''
    Parameters
    ----------
    numTurns : int
        number of turns for maze.
    pathLength : int
        number of blocks maze traverses.
    xMax : int, optional
        maximum x value. The default is 10.
    yMax : int, optional
        maximum maximum y value. The default is 10. 
    xMin : int, optional
        minimum x value. The default is 0.
    yMin : int, optional
        minimum y value. The default is 0.
    maxIter : int, optional
        number of iterations for "convergence". The default is 100.
    closePrev : boolean, optional
        close previous attempts to make figure. The default is True

    Returns
    -------
    Random maze figure.

    '''
    import numpy 
    import matplotlib.pyplot
    import time 

    def makeMaze(num_turns, path_length): # make path 

        '''
        
        Parameters
        ----------
        num_turns : int
            number of turns
        path_length : int
            length of path to be traveled.

        Returns
        -------
        directions : ndarray
            array of directions [0: north, 1: south, 2: east, 3: west].

        '''

        turnTimes = numpy.random.choice(range(1,path_length-1), num_turns, replace=False)
        # can't turn to start and to end 
        
        direction  = numpy.random.choice(4)
        
        directions = numpy.zeros(shape=(path_length,1))
        
        for step in range(path_length):
            if step in turnTimes: # make a turn 
                if direction == 0 or direction == 1: # north or south 
                    weights = numpy.array([0, 0, 0.5, 0.5])
                elif direction == 2 or direction == 3: # east or west
                    weights = numpy.array([0.5, 0.5, 0, 0])
                direction = numpy.random.choice(4, 1, p = weights)
            # index in 
            directions[step] = direction; 
            
        return directions 

    def setGrid(xmin, xmax, ymin, ymax): # visualize 
        '''

        Parameters
        ----------
        xmin : int
            minimum x value.
        xmax : int
            maximum x value.
        ymin : int
            minimum y value.
        ymax : int
            maximum y value.

        Returns
        -------
        None

        '''
        # Create space for maze
        matplotlib.pyplot.figure()
        for x in range(xmin, xmax+1):
            matplotlib.pyplot.axvline(x, color='k')
        for y in range(ymin, ymax+1):
            matplotlib.pyplot.axhline(y, color='k')
        matplotlib.pyplot.xticks(range(xmin, xmax+1))
        matplotlib.pyplot.yticks(range(ymin, ymax+1))

    def plotAgent(agent_position, numTurns, pathLength): # plot agent 
        '''

        Parameters
        ----------
        agent_position : array
            x,y location of agent.
        numTurns : int
            # of tunrs.
        pathLength : int
            length of path.

        Returns
        -------
        None.

        '''
        ax = matplotlib.pyplot.gca()
        ax.plot(agent_position[0,0]+0.5, agent_position[0,1]+0.5, marker='o',color='g')
        ax.plot(agent_position[:,0]+0.5, agent_position[:,1]+0.5)
        ax.plot(agent_position[-1,0]+0.5, agent_position[-1,1]+0.5, marker='o',color='r')
        matplotlib.pyplot.title(str(numTurns) + ' turns and ' + str(pathLength) + ' length')
        matplotlib.pyplot.show()
    
    def checkBounds(agent_position, xMin, xMax, yMin, yMax): # check boundaries 
        '''

        Parameters
        ----------
        agent_position : array
            x,y location of agent.
        xMin : int
            minimum x value .
        xMax : int
            maximum x value .
        yMin : int
            minimum y value .
        yMax : int
            maximum y value .

        Returns
        -------
        withinBounds : bool
            within bounds or not .

        '''
        if (numpy.min(agent_position[:,0])+0.5>= xMin and 
            numpy.max(agent_position[:,0])+0.5<= xMax and 
            numpy.min(agent_position[:,1])+0.5>= yMin and 
            numpy.max(agent_position[:,1])+0.5<= yMax):
            withinBounds = True
        else:
            withinBounds = False
            
        return withinBounds
    
    # set up 
    startT = time.time()
    currentIter = 1
    noPath = True
    
    while noPath:
        # Create grid 
        setGrid(xmin=xMin, xmax=xMax, ymin=yMin, ymax=yMax)
        
        # create a random path that satisifies all parameters (i.e. number of turns and path length)
        directions = makeMaze(num_turns=numTurns, path_length=pathLength+1)
        
        # translate to x,y coordinates  
        direction_xy = numpy.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
        # initialize position 
        agent_position = numpy.zeros(shape=(pathLength+1,2))
        agent_position[0,:] = numpy.random.choice(10, [1,2])
        for i in range(len(directions)-1):
            agent_position[i+1,:] = agent_position[i,:] + direction_xy[int(directions[i]), :]
        
        # plot agent position  
        plotAgent(agent_position, numTurns, pathLength)
        
        # check for overlap 
        for i in range(len(directions)-1):
            mask = numpy.ones(numpy.shape(agent_position)[0], dtype=bool)
            mask[i] = 0
            one_removed = agent_position[mask,:];  
            if numpy.sum( numpy.sum(agent_position[i] == one_removed, axis=1) == 2 ) > 0:
                noOverlap = False
                break
            else:
                noOverlap = True
        
        # see if within bounds 
        withinBounds = checkBounds(agent_position, xMin, xMax, yMin, yMax)
            
        # try to move to fix 
        if noOverlap and not withinBounds :
            shift = numpy.zeros(shape=numpy.shape(agent_position))
            if numpy.min(agent_position[:,0])<= xMin:
                shift[:,0] = xMin - numpy.min(agent_position[:,0])
            elif numpy.max(agent_position[:,0])>= xMax:
                shift[:,0] = xMax - numpy.max(agent_position[:,0])
            if numpy.min(agent_position[:,1])<= yMin:
                shift[:,1] = yMin - numpy.min(agent_position[:,1])
            elif numpy.max(agent_position[:,1])>= yMax:
                shift[:,1] = yMax - numpy.max(agent_position[:,1])
            # shift agent 
            agent_position = agent_position + shift

            if closePrev:
                matplotlib.pyplot.close()
            
            # replot 
            setGrid(xmin=xMin, xmax=xMax, ymin=yMin, ymax=yMax)
            plotAgent(agent_position, numTurns, pathLength)
            
            # check bounds 
            withinBounds = checkBounds(agent_position, xMin, xMax, yMin, yMax)
            
        # satisfy both constraints    
        if noOverlap and withinBounds :
            noPath = False; 
            endT = time.time()
            print(f'Algorithm converged.\nNumber of turns: {numTurns:d}\nPath length: {pathLength:d}\nNumber of iterations: {currentIter:d}\nExecution time: {endT-startT:.2f} seconds')
        
        if closePrev:
            matplotlib.pyplot.close()
            
        # "convergence"
        currentIter += 1
        if currentIter == maxIter:
            endT = time.time()
            print(f'Algorithm did not converge.\nNumber of turns: {numTurns:d}\nPath length: {pathLength:d}\nNumber of iterations: {currentIter:d}\nExecution time: {endT-startT:.2f} seconds\nConsider either increasing grid area, increasing maximum number of iterations, decreasing number of turns, or decreasing path length.')
            # print(f'Algorithm did not converge within {maxIter:d} iterations. ')
            break
