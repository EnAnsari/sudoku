# powered by Rahmat
# github: https://github.com/EnAnsari
# Email: Rahmat2022a@gmail.com

N = 9


def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()


def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if (arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


def isSafe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def solveSudoku(arr):
    l = [0, 0]
    if not find_empty_location(arr, l):
        return True
    row = l[0]
    col = l[1]

    for num in range(1, N + 1):
        if isSafe(arr, row, col, num):
            arr[row][col] = num
            if (solveSudoku(arr)):
                return True
            arr[row][col] = 0
    return False


print('Enter a 9*9 Matrix with 0 instead of unknown numbers:')
grid = [list(map(int, input().split())) for i in range(N)]

print('\nResult:')
if (solveSudoku(grid)):
    printing(grid)
else:
    print("no solution exists ")

# Example:
# input:
# 3 0 6 5 0 8 4 0 0
# 5 2 0 0 0 0 0 0 0
# 0 8 7 0 0 0 0 3 1
# 0 0 3 0 1 0 0 8 0
# 9 0 0 8 6 3 0 0 5
# 0 5 0 0 9 0 6 0 0
# 1 3 0 0 0 0 2 5 0
# 0 0 0 0 0 0 0 7 4
# 0 0 5 2 0 6 3 0 0
# output:
# 3 1 6 5 7 8 4 9 2
# 5 2 9 1 3 4 7 6 8
# 4 8 7 6 2 9 5 3 1
# 2 6 3 4 1 5 9 8 7
# 9 7 4 8 6 3 1 2 5
# 8 5 1 7 9 2 6 4 3
# 1 3 8 9 4 7 2 5 6
# 6 9 2 3 5 1 8 7 4
# 7 4 5 2 8 6 3 1 9

# Enjoy the code! 😊
