#import pdb
import numpy as np

from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs


'''
TO-DO 
I implemented this feature.
'''
def sense(color, grid, beliefs, p_hit, p_miss):
    grid, beliefs = np.array(grid), np.array(beliefs)
    
    #blocks where the observed color matches the block color. this is a mask
    hits = np.where(grid == color, p_hit, 1)
    
    #blocks where observed color does not match the block color. this is a mask
    misses = np.where(grid != color, p_miss, 1)
    
    #multiply the original beliefs by the hit/miss masks.
    new_beliefs = np.multiply(beliefs, hits)
    new_beliefs = np.multiply(new_beliefs, misses)
    
    #normalize new beliefs.
    new_beliefs = new_beliefs / np.sum(new_beliefs)
    
    return new_beliefs.tolist() #converting back to desired python list.

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)