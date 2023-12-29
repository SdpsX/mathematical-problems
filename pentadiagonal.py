import numpy as np


def pentadiagonal_solver(A, b):
    n = len(b)

    # Извлекаем коэффициенты
    a = [A[i][i - 2] if i > 1 else 0 for i in range(n)]
    print("a:", *a)

    c = [A[i][i - 1] if i > 0 else 0 for i in range(n)]
    print("c:", *c)

    d = [A[i][i] for i in range(n)]
    print("d:", *d)

    e = [A[i][i + 1] if i < n - 1 else 0 for i in range(n)]
    print("e:", *e)

    f = [A[i][i + 2] if i < n - 2 else 0 for i in range(n)]
    print("f:", *f)

    print()

    # Прямой ход
    for i in range(2, n):
        if a[i] != 0.0 and d[i - 2] != 0.0:
            print(a[i], "/", d[i - 2])
            m = a[i] / d[i - 2]
            print("m", m)

            d[i] -= m * e[i - 2]
            print("d", *d)

            c[i] -= m * f[i - 2]
            # c[i] /= (d[i])
            print("c", *c)

            b[i] -= m * b[i - 2]
            print("b", *b)

            print()

    # Обратный ход
    # Инициализация вектора решения x
    x = np.zeros_like(b, dtype = float)
    x[-1] = b[-1] / d[-1]

    for i in range(n - 3, 0, -1):
        x[i] = (b[i] - c[i] * x[i + 1] - e[i] * x[i + 2]) / d[i]

    # Обработка первых двух уравнений (i=0 и i=1)
    x[0] = (b[0] - c[0] * x[1] - e[0] * x[2]) / d[0]
    x[1] = (b[1] - c[1] * x[0] - e[1] * x[2]) / d[1]

    return x


# Пример использования
A = np.array([[-4.4704, 4.4554, 0, 0, 0, 0, 0],
              [1.8824, -4.015, 2.1176, 0, 0, 0, 0],
              [0, 1.8889, -4.015, 2.1111, 0, 0, 0],
              [0, 0, 1.8947, -4.015, 2.1053, 0, 0],
              [0, 0, 0, 1.9, -4.015, 2.1, 0],
              [0, 0, 0, 0, 1.9048, -4.015, 2.0952],
              [0, 0, 0, 0, 0, -3.6042, 4.0002]])

b = np.array([[0.3276],
             [0.01],
             [0.01],
             [0.01],
             [0.01],
             [0.01],
             [0.5615]])

result = pentadiagonal_solver(A, b)

print()
for i in range(len(result)):
    result[i][0] = float("{:.4f}".format(result[i][0]))

print(*result[i])
