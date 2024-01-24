# backtracking algorithm to solve sudoku

# function to print the grid
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" "),
        print()

# function to find the first unassigned location in the grid
def find_empty_location(arr):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                return row, col
    return None

# returning a boolean to tell whether assigning the given number to that box is safe
def is_safe_assignment(arr, row, col, num):
    # checking if 'num' is not already placed in that row, column, or 3x3 box
    return not (
        any(arr[row][i] == num for i in range(9)) or
        any(arr[i][col] == num for i in range(9)) or
        any(arr[i + row - row % 3][j + col - col % 3] == num for i in range(3) for j in range(3))
    )

# recursive function to solve the grid 
def solve_sudoku(arr):
    # finding the first unassigned location
    empty_location = find_empty_location(arr)

    # no unassigned location-> solved sudoku
    if not empty_location:
        return True

    # give values to row and col
    row, col = empty_location

    # for digits 1 to 9
    for num in range(1, 10):
        # check if the assignment is safe
        if is_safe_assignment(arr, row, col, num):
            # tentative assignment
            arr[row][col] = num

            # attempt to solve the Sudoku
            if solve_sudoku(arr):
                return True

            # if the current assignment leads to failure -> backtrack
            arr[row][col] = 0

    # no solution found
    return False


if __name__ == "__main__":
    # creating a 2D array for Sudoku
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # success -> print the solved grid
    if solve_sudoku(grid):
        print_grid(grid)
    else:
        print("No solution exists")
