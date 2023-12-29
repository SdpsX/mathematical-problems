import matplotlib.pyplot as plt
import numpy as np


def euler_cauchy(x0, y0, x_final, h):
    x_values = [x0]
    y_values = [y0]

    while x0 < x_final:
        y_predictor = f(x0, y0)
        y_corrector = f(x0 + h, y0 + h * y_predictor)
        y0 += h * (y_predictor + y_corrector) / 2
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

cauchy_x_values, cauchy_y_values = euler_cauchy(x0, y0, x_final, h)

exact_x_values = np.arange(x0, x_final + h, h)
exact_y_values = [exact_solution(x) for x in exact_x_values]

print(f"Точное решение:{' ' * 4}Метод Эйлера - Коши:{' ' * 5}Погрешность:")
for exact_x, exact_y, cauchy_x, cauchy_y in zip(
    exact_x_values, exact_y_values, cauchy_x_values, cauchy_y_values
):
    print(
        f"({exact_x:.1f}, {exact_y:.6f}){' ' * 4}({cauchy_x:.1f}, {cauchy_y:.6f}){' ' * 10}{abs(exact_y - cauchy_y):.6f}"
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
    cauchy_x_values,
    cauchy_y_values,
    label="Решение методом Эйлера — Коши",
    marker="o",
    linestyle="dashed",
    color="green",
)

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Сравнение точного решения и решения методом Эйлера — Коши")
plt.grid(True)
plt.show()
