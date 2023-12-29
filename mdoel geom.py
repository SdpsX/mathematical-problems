#моделирование геометрических фигур
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Пример использования классов
rect = Rectangle(5, 10)
print("Площадь прямоугольника: ", rect.area())

circ = Circle(7)
print("Площадь круга: ", circ.area())