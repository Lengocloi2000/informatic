"""
Напишите программу, которая объявляет класс Shape, конструктор которого принимает ширину и высоту.
После этого унаследуйте от него класс Triangle и Rectangle. Реализуйте метод area(), который возвращает площадь этих фигур.
Продемонстрируйте работоспособность программы.
"""

class Shape:
    __width = 0
    __height = 0
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Triangle(Shape):
    def area_triangle(self):
        return 1/2*self.get_width()*self.get_height()


class Rectangle(Shape):
    def area_rectangle(self):
        return self.get_width()*self.get_height()

print(Triangle(3,4).area_triangle())
print(Rectangle(3,4).area_rectangle())


