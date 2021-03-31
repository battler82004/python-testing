# -*- coding: utf-8 -*-
# James Taddei
# Robot Grid
# 3/31/21

# This is an example of what you'd replace 'pass' in 'main' with
"""
Example version of main:
    # Starting values for the variables
    facing = "up"
    pos = [4,1]
    gridSize = [5,5]
    invalidPositions = [[2,1],[3,1],[5,1],[5,2],[5,3], [3,3],[4,3],[1,2],[1,3],[1,4],[1,5]]
    
    # Robot commands
    forward(facing, pos, gridSize, invalidPositions)
    facing = left(facing, directions)
    for i in range(2):
        forward(facing, pos, gridSize, invalidPositions)
    facing = right(facing, directions)
    for i in range(2):
        forward(facing, pos, gridSize, invalidPositions)
        
    if can_move("left", facing, pos, gridSize, invalidPositions) == True:
        facing = left(facing, directions)
        
    # Final Prints Statements
    print (pos)
    print (facing)
"""

# Variable Creation
facing = ""
pos = []
directions = ["up", "right", "down", "left"]
gridSize = []
invalidPositions = []

# Main Function, replace pass with what you want the robot to do
def main(facing, pos, directions, gridSize, invalidPositions):
    # Replace 'pass' with what you want the robot to do, bottom left = [1, 1]
    pass
    
# Turns the robot left 90 degrees
def left(facing, directions):
    a = 0
    while (facing != directions[a]):
        a += 1
        
    return(directions[(a-1)])
    
# Turns the robot right 90 degrees
def right(facing, directions):
    a = 0
    while (facing != directions[a]):
        a += 1
    if a == 3:
        a = -1
        
    return(directions[(a+1)])
    
# Moves the robot one block forward (if possible)
def forward(facing, pos, gridSize, invalidPositions):
    if (can_move("forward", facing, pos, gridSize, invalidPositions) == True):
        if (facing == "up"):
            pos[1] += 1
        elif (facing == "left"):
            pos[0] -= 1
        elif (facing == "down"):
            pos[1] -= 1
        else:
            pos[0] += 1
    else:
        print("Error, invalid move")
    
# This checks if the robot can move 1 forward in a direction
def can_move(direction, facing, pos, gridSize, invalidPositions):
    # This finds the position that should be checked if the robot can go to it
    if (facing == "up"):
        if (direction == "left"):
            checkPos = [pos[0]-1, pos[1]]
        elif (direction == "forward"):
            checkPos = [pos[0], pos[1]+1]
        elif (direction == "backward"):
            checkPos = [pos[0], pos[1]-1]
        else:
            checkPos = [pos[0]+1, pos[1]]
    elif (facing == "right"):
        if (direction == "left"):
            checkPos = [pos[0], pos[1]+1]
        elif (direction == "forward"):
            checkPos = [pos[0]+1, pos[1]]
        elif (direction == "backward"):
            checkPos = [pos[0]-1, pos[1]]
        else:
            checkPos = [pos[0], pos[1]-1]
    elif (facing == "down"):
        if (direction == "left"):
            checkPos = [pos[0]+1, pos[1]]
        elif (direction == "forward"):
            checkPos = [pos[0], pos[1]-1]
        elif (direction == "backward"):
            checkPos = [pos[0], pos[1]+1]
        else:
            checkPos = [pos[0]-1, pos[1]]
    else:
        if (direction == "left"):
            checkPos = [pos[0], pos[1]-1]
        elif (direction == "forward"):
            checkPos = [pos[0]-1, pos[1]]
        elif (direction == "backward"):
            checkPos = [pos[0]+1, pos[1]]
        else:
            checkPos = [pos[0], pos[1]+1]
            
    # This checks if the possition is valid or not then returns it
    return (invalid_checker(checkPos, gridSize, invalidPositions))

# This function checks if a move is possible
def invalid_checker(pos, gridSize, invalidPositions):
    # These two check if the location is in the grid
    if (pos[0] < 1 or pos[0] > gridSize[0]):
        return False
    elif (pos[1] < 1 or pos[1] > gridSize[1]):
        return False
    
    # This if-else checks if the pos being checked is greyed out (invalid) or not
    if (pos in invalidPositions):
        return False
    else:
        return True
    
# Calls the main function of the program which is where the robot commands should be placed
main(facing, pos, directions, gridSize, invalidPositions)