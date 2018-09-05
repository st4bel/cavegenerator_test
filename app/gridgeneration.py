import random
from app import app

def initialiseGrid(height = app.config["GRID_HEIGHT"], width = app.config["GRID_WIDTH"], startalivechance=app.config["START_ALIVE_CHANCE"]):
    grid = []
    for row in range(0, height):
        grid.append([])
        for col in range(0, width):
            grid[row].append(random.random()<startalivechance)
    return grid

def simulateStep(oldgrid):
    newgrid = []
    for row in range(0,len(oldgrid)):
        newgrid.append([])
        for col in range(0,len(oldgrid[row])):
            neighbours = countNeighbours(grid = oldgrid, row = row, col = col)
            if oldgrid[row][col]:
                if neighbours < app.config["STARVE_LIMIT"]:
                    newgrid[row].append(False)
                else:
                    newgrid[row].append(True)
            else:
                if neighbours > app.config["MIN_POP_BIRTH"]:
                    newgrid[row].append(True)
                else:
                    newgrid[row].append(False)
    return newgrid



def countNeighbours(grid, row, col):
    counter = 0
    for dif_row in range(-1,2): #von -1 bis 1
        for dif_col in range(-1,2):
            if row+dif_row >= 0 and row+dif_row < len(grid) and col+dif_col >= 0 and col+dif_col < len(grid[row]):
                counter += 1 if grid[row+dif_row][col+dif_col] and not (dif_row==0 and dif_col==0)  else 0
    return counter
