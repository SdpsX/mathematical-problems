#Метод второго порядка точности
import math


def f(x, y):
    a = 0
    b = 1
    c = -x ** 2
    return (a + b * x) * math.exp(c * x) + 2 * (2 - x) * y


def runge_kutta(x0, y0, X, n):
    h = (X - x0) / n
    x = x0
    y = y0

    print("x\t\ty")
    print(f"{x}\t\t{y}")

    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        y = y + (1 / 3) * (k1 + 2 * k2 + k3)
        x = x + h

        print(f"{x:.2f}\t\t{y:.5f}")


x0 = 1
y0 = 10
X = 6

n_values = [10, 20, 40]

for n in n_values:
    print(f"\nРезультат для n = {n}")
    runge_kutta(x0, y0, X, n)
