from math import pi

class Figure:
    sides_count = 0
    def __init__(self, color, *sides, filled = False):
        self.__color = color
        self.__sides = list(sides)
        self.filled = filled
        self.sides_count = len(self.__sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and isinstance(r, int) and 0 <= g <= 255 and isinstance(g, int) and 0 <= b <= 255 and isinstance(b, int):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color = [r, g, b]
        else:
            # print('Указаны неверные параметры цвета; каждый из параметров "r", "g," и "b" должен быть целым числом в интервале от 0 до 255 включительно')
            pass
    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *new_sides):
        if self.__class__ is Cube:
            if len(list(new_sides)) == 1 and all(isinstance(side, int) and side > 0 for side in new_sides):
                return True
            else:
                return False
        else:
            if len(list(new_sides)) == len(self.__sides) and all(isinstance(side, int) and side > 0 for side in new_sides):
                return True
            else:
                return False

    def set_sides(self, *new_sides):
        if self.__class__ is Cube:
            if self.__is_valid_sides(*new_sides) == True:
                self.__sides = [new_sides[0]] * Cube.sides_count
            else:
                # print('Указано количество сторон не равное 1 или указанное значение не является целым положительным числом')
                pass
        else:
            if self.__is_valid_sides(*new_sides) == True:
                self.__sides = list(new_sides)
            else:
                print('Указано неверное количество сторон или не все указанные значения являются целыми положительными числами')

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) == Circle.sides_count and all(isinstance(side, int) and side > 0 for side in sides):
            super().__init__(color, *sides)
        else:
            super().__init__(color)
            self._Figure__sides = [1] * Circle.sides_count
            print('Для фигуры "круг" параметр "sides" должен содержать одно целое положительное число; создан круг с длиной окружности равной 1')
        self.radius = self.get_sides()[0] / (2 * pi)
        self.sides_count = Circle.sides_count

    def get_square(self):
        s = pi * (self.radius ** 2)
        return s

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) == Triangle.sides_count and all(isinstance(side, int) and side > 0 for side in sides):
            super().__init__(color, *sides)
        else:
            super().__init__(color)
            self._Figure__sides = [1] * Triangle.sides_count
            print('Для фигуры "треугольник" параметр "sides" должен содержать три целых положительных числа; создан равносторонний треугольник с длиной стороны равной 1')
        self.sides_count = Triangle.sides_count

    def get_square(self):
        sp = super().__len__() / 2
        return (sp * (sp - self.get_sides()[0]) * (sp - self.get_sides()[1]) * (sp - self.get_sides()[2])) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1 and all(isinstance(side, int) and side > 0 for side in sides):
            super().__init__(color)
            self._Figure__sides = [list(sides)[0]]*Cube.sides_count

        else:
            super().__init__(color)
            self._Figure__sides = [1] * Cube.sides_count
            print('Для фигуры "куб" параметр "sides" должен содержать одно целое положительное число; создан куб с ребром равным 1')
        self.sides_count = Cube.sides_count

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle([200, 200, 100], 10)
cube1 = Cube([222, 35, 130], 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
