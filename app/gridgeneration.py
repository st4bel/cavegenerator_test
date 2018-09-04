import random
from app import app

def initialiseGrid(height = 20, width = 20, startalivechance=0.6):
    grid = []
    for row in range(0, height):
        grid.append([])
        for col in range(0, width):
            grid[row].append(random.random()<startalivechance)
    return grid

def simulateStep(oldgrid):
    newgrid = oldgrid
    for row in range(0,len(newgrid)):
        for col in range(0,len(newgrid[row])):
            neighbours = countNeighbours(grid = oldgrid, row = row, col = col)
            if oldgrid[row][col]:
                if neighbours < app.config["STARVE_LIMIT"]:
                    newgrid[row][col] = False
            else:
                if neighbours > app.config["MIN_POP_BIRTH"]:
                    newgrid[row][col] = True
    return newgrid



def countNeighbours(grid, row, col):
    counter = 0
    for dif_row in range(-1,2): #von -1 bis 1
        for dif_col in range(-1,2):
            if row+dif_row >= 0 and row+dif_row < len(grid) and col+dif_col >= 0 and col+dif_col < len(grid[row]):
                counter += 1 if grid[row+dif_row][col+dif_col] and not (dif_row==0 and dif_col==0)  else 0
    return counter
