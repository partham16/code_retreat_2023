from scipy.signal import convolve2d
import numpy as np
import time
from rich.live import Live
from rich.table import Table

class Grid:
    def __init__(self, dim=100, start_random=True):
        self.dim = dim
        self._set_conv_kernel()
        if start_random:
            self.grid = np.random.choice([0, 1], size=(dim, dim))

    def _set_conv_kernel(self):
        # Define the kernel to consider all adjacent cells
        self.kernel = np.array(
            [[1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]])
    
    def _vectorized_living_neighbours(self):
        # Use convolution to sum up neighbors, 
        # using 'wrap' as the mode to accomplish torus-like behavior
        return convolve2d(self.grid, self.kernel, mode='same', boundary='wrap')
    
    def update_grid_state(self):
        # Compute number of living neighbours using vectorized convolution operation
        living_neighbours = self._vectorized_living_neighbours()

        # Create new grid for next state of the game
        new_grid = np.zeros_like(self.grid)

        # Rule 1: Any live cell with fewer than two live neighbours dies, as if by underpopulation
        # Rule 2: Any live cell with two or three live neighbours lives on to the next generation
        # Rule 3: Any live cell with more than three live neighbours dies, as if by overpopulation
        # These rules are combined into a single condition
        new_grid[((self.grid == 1) & (living_neighbours >= 2) & (living_neighbours <= 3))] = 1

        # Rule 4: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
        new_grid[((self.grid == 0) & (living_neighbours == 3))] = 1

        self.grid = new_grid


def visualize_game_of_life(grid, num_steps): 
    # Create a Rich table and styling
    table = Table(show_header=False, padding=(0, 0))
    table.pad_edge = False

    # Initialize a Rich Live context manager
    with Live(table, refresh_per_second=4, transient=True):
        # for each step
        for i in range(num_steps):
            
            # Add each row of the grid to the table
            for x in range(grid.grid.shape[0]):
                row = ''.join('O' if cell else ' ' for cell in grid.grid[x])
                table.add_row(row)
            
            # Update the grid's state
            grid.update_grid_state()
            
            # Clear the table
            table.rows.clear()
            
            time.sleep(0.2)  # introduce a delay of 0.2 seconds for user to visualize better
            

if __name__ == '__main__':
    # Create a Grid object, 20x20 size
    grid = Grid(dim=20)

    # Start the simulation
    visualize_game_of_life(grid, num_steps=100)
        