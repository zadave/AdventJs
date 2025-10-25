def detect_bombs(grid):
    rows = len(grid)      # Number of rows
    cols = len(grid[0])   # Number of columns

    # Create a grid for the results
    result = [[0] * cols for _ in range(rows)]

    # Directions for the 8 adjacent positions (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Top: left, center, right
        (0, -1),         (0, 1),     # Left and right
        (1, -1), (1, 0), (1, 1)      # Bottom: left, center, right
    ]

    # Traverse the grid
    for i in range(rows):
        for j in range(cols):
            # If the current cell contains a bomb
            if grid[i][j]:
                for dx, dy in directions:
                    new_row = i + dx
                    new_col = j + dy

                    # Ensure the adjacent cell is within bounds
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        result[new_row][new_col] += 1

    return result