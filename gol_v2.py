class Grid:
    def __init__(self, size):
        self.array = np.random.choice([0, 1], size=size)

def visualize_game_of_life(grid, num_steps): 
    # Create a Rich table and styling
    table = Table(show_header=False, padding=(0, 0))
    table.pad_edge = False

    # Initialize a Rich Live context manager
    with Live(table, refresh_per_second=4, transient=True):
        # for each step
        for i in range(num_steps):
            
            for x in range(grid.array.shape[0]):
                row = ''.join('O' if cell else ' ' for cell in grid.array[x])
                table.add_row(row)
            
            # Compute number of living neighbours
            living_neighbours = vectorized_living_neighbours(grid.array)
            
            # Create new grid for next state of the game
            new_grid = np.zeros_like(grid.array)
            
            # Apply the rules of the game
            new_grid[((grid.array == 1) & (living_neighbours >= 2) & (living_neighbours <= 3))] = 1
            new_grid[((grid.array == 0) & (living_neighbours == 3))] = 1
            
            # Update the grid
            grid.array[:] = new_grid[:]
            
            # Clear the table
            table.rows.clear()
            
            time.sleep(0.2)  # introduce a delay of 0.2 seconds for user to visualize better

# Create a Grid object
grid = Grid(size=(20, 20))

# Start the simulation
visualize_game_of_life(grid, num_steps=100)