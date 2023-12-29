#ВЫЧИСЛЕНИЕ НАИБОЛЬШЕГО И НАИМЕНЬШЕГО СОБСТВЕННЫХ ЗНАЧЕНИЙ МАТРИЦЫ
import numpy as np


def rotation_method(A, eps=0.001):
    n = A.shape[0]
    Q = np.eye(n)
    B = np.copy(A)
    max_offdiag = lambda B: np.max(np.abs(B - np.diag(np.diag(B))))

    s1 = []
    s2 = []

    while max_offdiag(B) > eps:
        k, l = np.unravel_index(np.argmax(np.abs(B - np.diag(np.diag(B)))), (n, n))
        # print(f'k = {k} | l = {l})
        s1.append(k)
        s2.append(l)
        theta = 0.5 * np.arctan2(2 * B[k, l], B[l, l] - B[k, k])
        c = np.cos(theta)
        s = np.sin(theta)
        J = np.eye(n)
        J[k, k], J[l, l] = c, c
        J[k, l], J[l, k] = -s, s
        B = J.T @ B @ J
        Q = Q @ J
    return np.diag(B), Q.T, s1, s2


A = np.array([[5, 1, 2], [1, 4, 1], [2, 1, 3]])# матрица
eigenvalues, eigenvectors, s1, s2 = rotation_method(A)# кормим функции матрицу

print('k ', *s1, sep='')
print('l ', *s2, sep='')
for i, v in enumerate(eigenvectors):
    print(f'Лямбда{i + 1} = {eigenvalues[i]}')