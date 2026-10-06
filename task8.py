def can_put(matrix, row, col, num):
    # проверяем строку
    for j in range(4):
        if matrix[row][j] == num:
            return False
    # проверяем столбец
    for i in range(4):
        if matrix[i][col] == num:
            return False
    # проверяем квадрат 2x2
    start_row = row // 2 * 2
    start_col = col // 2 * 2
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if matrix[i][j] == num:
                return False
    return True


def find_empty(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return i, j
    return -1, -1


def solve_sudoku(matrix):
    row, col = find_empty(matrix)
    # базовый случай: пустых клеток нет, всё решено
    if row == -1:
        return True
    # рекурсивный случай: пробуем поставить числа 1-4
    for num in range(1, 5):
        if can_put(matrix, row, col, num):
            matrix[row][col] = num
            if solve_sudoku(matrix):
                return True
            matrix[row][col] = 0  # не получилось, возвращаем как было
    return False


def print_matrix(matrix):
    for row in matrix:
        line = ""
        for num in row:
            line = line + str(num) + " "
        print(line)


matrix = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4],
]

print("Исходная матрица:")
print_matrix(matrix)

if solve_sudoku(matrix):
    print("Решение:")
    print_matrix(matrix)
else:
    print("Решения нет")
