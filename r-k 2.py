#2 порядок(Метод Рунге-Кутты с формулой приближения)
def f(a, b):
    return a + b


def runge_kutta(h, a0, b0, n, e):

    p = 4

    while a0 < n:
        t1 = h * f(a0, b0)
        t2 = h * f(a0 + h / 2, b0 + t1 / 2)

        b1 = b0 + (t1 + 2 * t2) / 2

        t1 = h / 2 * f(a0, b0)
        t2 = h / 2 * f(a0 + h / 4, b0 + t1 / 2)

        b2 = b0 + (t1 + 2 * t2) / 2
        r = (b1 - b2) / (2 ** p - 1)

        if abs(r) < e:
            b0 = b1
            a0 += h

            if abs(r) < e / 2:
                h = 2 * h

        else:
            h = h / 2

    return b0


a0 = 0
b0 = 1
h = 0.1
n = 0.2
e = 0.001

b = runge_kutta(h, a0, b0, n, e)
print(f'При a = {n}, b = {b}')
