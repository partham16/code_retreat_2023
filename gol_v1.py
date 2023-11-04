import numpy as np

# we implement a toriodal grid, where the top and bottom are connected to each other, 
# as well as the left and right - that's how we simulate infinite grid

# we take large enough dimensions i.e. 100


class Grid:
    def __init__(self, dim=100, start_random=True):
        self.dim = dim
        if start_random:
            self.array = np.random.randint(2, size=(dim, dim))

    def calc_neighbor_boundaries(self, x, y):
        x_start, x_end = (x-1) % self.dim, (x+2) % self.dim,
        y_start, y_end = (y-1) % self.dim,, (y+2) % self.dim,
        return x_start, x_end, y_start, y_end

    def slice_mask_neighbors(self, x, y, x_start, x_end, y_start, y_end):
        if x_end <= x_start:
            x_slice = np.r_[self.grid[x_start:,y_start:y_end], self.grid[:x_end,y_start:y_end]]
        else:
            x_slice = self.grid[x_start:x_end, y_start:y_end]
            
        if y_end <= y_start:
            y_slice = np.c_[x_slice[:,:y_end], x_slice[:,y_start:]]
        else:
            y_slice = x_slice[:,:]
            
        # Remove the element (x, y) because we don't want to count the cell as its own neighbour
        mask = np.ones((3, 3), bool)
        mask[1, 1] = False
    
        return y_slice[mask]
    
    def count_living(self, neighbors):    
        # We sum up the values of the neighbors to know how many are 1 (living)
        return neighbors.sum()

    