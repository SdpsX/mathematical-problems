import matplotlib.pyplot as plt
import numpy as np


def classic_euler(x0, y0, x_final, h):
    x_values = [x0]
    y_values = [y0]

    while x0 < x_final:
        y0 += h * f(x0, y0)
        x0 += h

        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values


def f(x, y):
    return y / x - 2 * np.log(x) / x


def exact_solution(x):
    return 2 * np.log(x) - x + 2


x0 = 1
y0 = 1
x_final = 3
h = 0.2

classic_x_values, classic_y_values = classic_euler(x0, y0, x_final, h)

exact_x_values = np.arange(x0, x_final + h, h)
exact_y_values = [exact_solution(x) for x in exact_x_values]

print(f"Точное решение:{' ' * 4}Метод Эйлера:{' ' * 6}Погрешность:")

for x, y, classic_x, classic_y in zip(
    exact_x_values, exact_y_values, classic_x_values, classic_y_values
):
    print(
        f"({x:.1f}, {y:.6f}){' ' * 4}({classic_x:.1f}, {classic_y:.6f}){' ' * 4}{abs(y - classic_y):.6f}"
    )

plt.figure(figsize=(16, 9))

plt.plot(
    exact_x_values,
    exact_y_values,
    label="Точное решение",
    marker="o",
    linestyle="solid",
    color="black",
)

plt.plot(
    classic_x_values,
    classic_y_values,
    label="Решение методом Эйлера",
    marker="o",
    linestyle="dashed",
    color="red",
)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Сравнение точного решения и решения методом Эйлера")
plt.grid(True)
plt.show()
