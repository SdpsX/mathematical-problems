import matplotlib.pyplot as plt
import numpy as np


def improv_euler(x0, y0, x_final, h):
    x_values = [x0]
    y_values = [y0]

    while x0 < x_final:
        y_predictor = f(x0, y0)
        y_predictor = y0 + h * f(x0 + h / 2, y0 + h / 2 * y_predictor)
        y0 = y_predictor
        x0 = x0 + h

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

improv_x_values, improv_y_values = improv_euler(x0, y0, x_final, h)

exact_x_values = np.arange(x0, x_final + h, h)
exact_y_values = [exact_solution(x) for x in exact_x_values]

print(f"Точное решение:{' ' * 4}Улучшенный метод Эйлера:{' ' * 4}Погрешность:")
for x, y, improv_x, improv_y in zip(
    exact_x_values, exact_y_values, improv_x_values, improv_y_values
):
    print(
        f"({x:.1f}, {y:.6f}){' ' * 4}({improv_x:.1f}, {improv_y:.6f}){' ' * 13}{abs(y - improv_y):.6f}"
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
    improv_x_values,
    improv_y_values,
    label="Решение улучшенным методом Эйлера",
    marker="o",
    linestyle="dashed",
    color="orange",
)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Сравнение точного решения и решения улученным методом Эйлера")
plt.grid(True)
plt.show()
