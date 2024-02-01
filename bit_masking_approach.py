class SudokuSolver:
  def __init__(self, size=9):
      self.N = size

  def print_grid(self, grid):
      for row in grid:
          print(" ".join(map(str, row)))

  def is_safe(self, grid, row, col, num):
      # Check if num is present in the row
      if num in grid[row]:
          return False

      # Check if num is present in the column
      if num in [grid[i][col] for i in range(self.N)]:
          return False

      # Check if num is present in the 3x3 subgrid
      start_row, start_col = 3 * (row // 3), 3 * (col // 3)
      if num in [grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]:
          return False

      return True

  def solve_sudoku(self, grid, row, col):
      # Check if we have reached the end of the grid
      if row == self.N - 1 and col == self.N:
          return True

      # Move to the next row if the current column exceeds the grid size
      if col == self.N:
          row += 1
          col = 0

      # Skip to the next column if the cell is already filled
      if grid[row][col] > 0:
          return self.solve_sudoku(grid, row, col + 1)

      # Try placing numbers from 1 to N in the current cell
      for num in range(1, self.N + 1):
          if self.is_safe(grid, row, col, num):
              grid[row][col] = num

              # Recursively check the next possibilities
              if self.solve_sudoku(grid, row, col + 1):
                  return True

              # Backtrack if the assumption was incorrect
              grid[row][col] = 0

      return False

# Driver Code
grid = [
  [3, 0, 6, 5, 0, 8, 4, 0, 0],
  [5, 2, 0, 0, 0, 0, 0, 0, 0],
  [4, 8, 7, 0, 0, 0, 0, 3, 1],
  [0, 0, 3, 0, 1, 0, 0, 8, 0],
  [9, 0, 0, 8, 6, 3, 0, 0, 5],
  [0, 5, 0, 0, 9, 0, 6, 0, 0],
  [1, 3, 0, 0, 0, 0, 2, 5, 0],
  [0, 0, 0, 0, 0, 0, 0, 7, 4],
  [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

solver = SudokuSolver()
if solver.solve_sudoku(grid, 0, 0):
  solver.print_grid(grid)
else:
  print("No solution exists.")
