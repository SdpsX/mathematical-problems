#Метод касательных (Ньютона)
def fun(y):
    d = y ** 3 - y + 1
    return d


def diff(y):
    d = 3 * (y ** 2) - 1
    return d


def diff2(y):
    d = y * 6
    return d


a = -2
b = -1
x0 = 0
k = 0
if diff2(a) * fun(a) > 0:
    x = a
else:
    x = b
while abs(x - x0) > 0.001:
    x0 = x
    x = x0 - (fun(x0) / diff(x0))
    k += 1
print(format(x, '.6f'), k, format(abs(x - x0), '.6f'))