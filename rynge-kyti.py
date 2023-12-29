#2 порядок (Метод Рнге-Кутты)
def Runge(a0, b0, n):
    h = 0.1
    a = a0
    b = b0

    print("a\t\tb")
    print(f"{a}\t\t{b}")

    for i in range(n):
        t1 = f(a, b)
        t2 = f(a + h / 2, b + t1 * h / 2)

        b = b + h * t2
        a = a + h

        print(f"{a:.2f}\t\t{b:.5f}")





def f(a, b):
    return a + b




n_values = [10, 20, 40]
a0 = 0
b0 = 1

for n in n_values:
    print(f"\nРезультат для n = {n}")
    Runge(a0, b0, n)
