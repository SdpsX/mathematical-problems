import numpy as np


def runge_kutty(x0, y0, z0, x_final, h):
    x_values = [x0]
    y_values = [y0]
    z_values = [z0]
    print(f"x{' ' * 4}y{' ' * 9}z")

    while x0 < x_final:
        k1 = h * z0
        l1 = h * f(x0, y0, z0)

        k2 = h * (z0 + l1 / 2)
        l2 = h * f(x0 + h / 2, y0 + k1 / 2, z0 + l1 / 2)

        k3 = h * (z0 + l2 / 2)
        l3 = h * f(x0 + h / 2, y0 + k2 / 2, z0 + l2 / 2)

        k4 = h * (z0 + l3)
        l4 = h * f(x0 + h, y0 + k3, z0 + l3)

        y0 += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        z0 += (l1 + 2 * l2 + 2 * l3 + l4) / 6

        x_values.append(x0)
        y_values.append(y0)
        z_values.append(z0)

        # print(
        #     f"k1 = {k1:.6f}, l1 = {l1:.6f}\n"
        #     f"k2 = {k2:.6f}, l2 = {l2:.6f}\n"
        #     f"k3 = {k3:.6f}, l3 = {l3:.6f}\n"
        #     f"k4 = {k4:.6f}, l4 = {l4:.6f}\n"
        #     f"x = {x0:.1f}\ny = {y0:.6f}\nz = {z0:.6f}"
        # )
        print(f"{x0:.1f}  {y0:.6f}  {z0:.6f}")
        x0 += h
    print("-" * 24)

    return z0


def shoot(x0, y0, z0, x_final, z_final, h, e):
    i = 1
    error = e
    while error >= e:
        print(f"Итерация: {i}")
        z10 = runge_kutty(x0, y0, z0, x_final, h)
        error = np.abs(z_final - z10)
        if z10 < z_final:
            print("z10 < z_final")
            # z0 += h
            z0 += error
            # z0 += z10 % z_final
            # print(f"z10 = {z10}\n" f"z10 % z_final = {z0}")

        elif z10 > z_final:
            print("z10 > z_final")
            # z0 -= h
            z0 -= error
            # z0 -= z_final % z10
            # z0 -= z10 % z_final
            # z0 += z_final % z10
            # z0 += z10 % z_final
            # print(f"z10 = {z10}\n" f"z10 % z_final = {z0}")
        print(f"z0 = {z0}\n" f"Погрешность: {error}\n")
        i += 1


def f(x, y, z):
    return -np.cos(x) * z - x ** 2 * (y + 1)


x0 = 0
y0 = 1
z0 = 0
x_final = 1
z_final = 3
h = 0.1
e = 10 ** (-2)

shoot(x0, y0, z0, x_final, z_final, h, e)
