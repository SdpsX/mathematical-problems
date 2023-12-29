#Найти обратную матрицу
def inverse_matrix(A):
    n = len(A)
    # находим матрицу
    for i in range(n):
        A[i].extend([0] * i + [1] + [0] * (n - i - 1))

    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
        pivot = A[i][i]
        if pivot == 0:
            return None
        for j in range(i, n * 2):
            A[i][j] /= pivot
        for j in range(n):
            if i != j:
                factor = A[j][i]
                for k in range(i, n * 2):
                    A[j][k] -= factor * A[i][k]

    x = [[A[i][j] for j in range(n, n * 2)] for i in range(n)]

    return x


num_rows = int(input('количество строк: '))
num_cols = int(input('количество столбцов: '))

matrix = []
vector = []

for i in range(num_rows):
    row = []

    for j in range(num_cols):
        value = float(input(f'значение для элемента ({i + 1}, {j + 1}): '))
        row.append(value)
    matrix.append(row)

print(*inverse_matrix(matrix), sep='\n')