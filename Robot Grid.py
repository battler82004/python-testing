# James Taddei
# Robot Grid
# 3/31/21

"""
Example version of main:
    facing = "up"
    pos = [4,1]
    gridSize = [5,5]
    invalidPositions = [[2,1],[3,1],[5,1],[5,2],[5,3], [3,3],[4,3],[1,2],[1,3],[1,4],[1,5]]
    
    forward(facing, pos, gridSize, invalidPositions)
    facing = left(facing, directions)
    for i in range(2):
        forward(facing, pos, gridSize, invalidPositions)
    facing = right(facing, directions)
    for i in range(2):
        forward(facing, pos, gridSize, invalidPositions)
        
    if can_move("left", facing, pos, gridSize, invalidPositions) == True:
        facing = left(facing, directions)
        
    print (pos)
    print (facing)
"""

facing = ""
pos = []
directions = ["up", "right", "down", "left"]
gridSize = []
invalidPositions = []

def main(facing, pos, directions, gridSize, invalidPositions):
    # Put what do here, bottom left = [1, 1]
    pass
    
def left(facing, directions):
    a = 0
    while (facing != directions[a]):
        a += 1
        
    return(directions[(a-1)])
    
def right(facing, directions):
    a = 0
    while (facing != directions[a]):
        a += 1
    if a == 3:
        a = -1
        
    return(directions[(a+1)])
    
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
    
def can_move(direction, facing, pos, gridSize, invalidPositions):
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
            
    return (invalid_checker(checkPos, gridSize, invalidPositions))

def invalid_checker(pos, gridSize, invalidPositions):
    if (pos[0] < 1 or pos[0] > gridSize[0]):
        return False
    elif (pos[1] < 1 or pos[1] > gridSize[1]):
        return False
    
    if (pos in invalidPositions):
        return False
    else:
        return True
    
main(facing, pos, directions, gridSize, invalidPositions)