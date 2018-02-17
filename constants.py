import numpy as np

#For screen dimensions
WIDTH = 125
HEIGHT = 125
FPS = 60

#Map structure
ROWS = 5
COLS = 5
CELL_TAM = float(WIDTH/COLS)
gameMap = np.matrix('1 1 1 1 1; 1 0 0 0 1; 1 1 0 1 1; 1 0 0 0 1; 1 1 1 1 1')
