#Вычислить матрицу
def gas(A, B):
    n = len(A)
    for i in range(n):
        elem = abs(A[i][i])
        row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > elem:
                elem = abs(A[k][i])
                row = k
# переставление строк
        if row != i:
            A[row], A[i] = A[i], A[row]
            B[row], B[i] = B[i], B[row]

        for j in range(i+1, n):
            factor = -A[j][i]/A[i][i]
            for k in range(i+1, n):
                A[j][k] += factor*A[i][k]
            B[j] += factor*B[i]

    x = [0]*n
    for i in range(n-1, -1, -1):
        x[i] = B[i]/A[i][i]
        for j in range(i-1, -1, -1):
            B[j] -= A[j][i]*x[i]

    return x


num_rows = int(input('Введите количество строк: '))
num_cols = int(input('Введите количество столбцов: '))

matrix = []
vector = []

for i in range(num_rows):
    row = []
    for j in range(num_cols):
        value = float(input(f'Введите значение  элемента ({i+1}, {j+1}): '))
        row.append(value)
    matrix.append(row)

    value = float(input(f'ответ  уравнения {i + 1}: '))
    vector.append(value)

print(*gas(matrix, vector), sep='\n')