import numpy as np


def thomas_algorithm(A, b):
    n = len(b)

    for i in range(1, n):
        m = A[i][i - 1] / A[i - 1][i - 1]
        A[i][i] -= m * A[i - 1][i]
        b[i] -= m * b[i - 1]

    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - A[i][i + 1] * x[i + 1]) / A[i][i]

    return x


A = np.array([[-4.4704, 4.4554, 0, 0, 0, 0, 0],
              [1.8824, -4.015, 2.1176, 0, 0, 0, 0],
              [0, 1.8889, -4.015, 2.1111, 0, 0, 0],
              [0, 0, 1.8947, -4.015, 2.1053, 0, 0],
              [0, 0, 0, 1.9, -4.015, 2.1, 0],
              [0, 0, 0, 0, 1.9048, -4.015, 2.0952],
              [0, 0, 0, 0, 0, -3.6042, 4.0002]])

b = np.array([0.3276, 0.01, 0.01, 0.01, 0.01, 0.01, 0.5615])

result = thomas_algorithm(A.copy(), b.copy())
print("Метод прогонки:", *result, sep = "\n")
