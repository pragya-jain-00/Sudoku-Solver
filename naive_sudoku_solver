class SudokuSolver:
    def __init__(self, size=9):
        self.N = size

    def print_grid(self, grid):
        for row in grid:
            print(" ".join(map(str, row)))

    def is_safe(self, grid, row, col, num):
        for x in range(self.N):
            if grid[row][x] == num or grid[x][col] == num:
                return False

        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve_sudoku(self, grid, row, col):
        if row == self.N - 1 and col == self.N:
            return True

        if col == self.N:
            row += 1
            col = 0

        if grid[row][col] > 0:
            return self.solve_sudoku(grid, row, col + 1)

        for num in range(1, self.N + 1):
            if self.is_safe(grid, row, col, num):
                grid[row][col] = num

                if self.solve_sudoku(grid, row, col + 1):
                    return True

                grid[row][col] = 0

        return False


# Driver Code
grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
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
    print("No solution exists")
