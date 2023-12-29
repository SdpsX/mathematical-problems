#Метод хорд
def f(x):
    # заданная функций
    return -(x ** 3) + x - 3


def chord_method(a, b, eps):
    x0, x1 = a, b
    i = 1

    while abs(x1 - x0) >= eps:
        # функция для подсчета c
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fc = f(c)

        # проверка f(c)*f(a)
        if fc == 0:
            break

        # если меньше 0, то берем итервал [a, c]
        elif fc * f(a) < 0:
            b = c

        # если больше нуля, то [c, b]
        else:
            a = c

        x0, x1 = x1, c
        print(
            f'Итерация {i}, Интервал: [{a}, {b}]\nc = {c}\nf(c) = {f(c)}\nx = {x1}\nf(x) = {f(x1)}\nПриближение: {abs(x1 - x0)}')
        print('~' * 50)
        i += 1

    return f'x = {x1}'


# промежуток [-2; -1.5], приближение 0.001
print(chord_method(-2, -1.5, 0.001))