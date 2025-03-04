from math import floor

def printPatterns(p):
    for x in p:
        for r in x:
            print(r)
        print(" ")

def compare_vertical(grid, x1, x2):
    for x in grid:
        if x[x1] != x[x2]:
            return False
    return True

def compare_n_vertical(grid, x, num_cols):
    for i in range(num_cols):
        if not compare_vertical(grid, x+i, x-i):
            return False
    return True


def compare_n_horizontal(grid, x, num_rows):
    # starting at row x, compare num_rows above and below for mirroring

    for i in range(num_rows):
        if grid[x + 1 + i] != grid[x - i]:
            return False
    return True


with open("./P13/test.txt", "r") as f:
    
    # try to work with one pattern at a time, not a whole table of patterns
    
    curr_grid = []
    for line in f:
        if line == '\n':
            # do the processing

            # horizontal first
            num_rows_to_comp = 1
            for row in range(floor(len(curr_grid)/2)):
                if compare_n_horizontal(curr_grid, row, row):
                    
                    
                
            
            curr_grid = []
        else:
            curr_grid.append(line.strip())