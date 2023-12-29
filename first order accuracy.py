#МЕТОД РУНГЕ – КУТТЫ РЕШЕНИЯ ЗАДАЧИ КОШИ ДЛЯ ОБЫКНОВЕННОГО ДИФФЕРЕНЦИАЛЬНОГО УРАВНЕНИ
#Метод первого порядка точности
import math


def f(x, y):
    a = 0
    b = 1
    c = -x ** 2
    return (a + b * x) * math.exp(c * x) + 2 * (2 - x) * y

x0 = 1
y0 = 10


def runge_kutta(x0, y0, X, n):
    h = (X - x0) / n)
    x = x0
    y = y0

    print(f"x\t\ty")
    print(f"{x}\t\t{y}")

    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
        print(f"{x:.2f}\t\t{y:.5f}")

X = 6
n_values = [10, 20, 40]

for n in n_values:
    print(f"\nРезультат для n = {n}")
    runge_kutta(x0, y0, X, n)