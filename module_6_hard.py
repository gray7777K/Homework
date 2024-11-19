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
            print('Указаны неверные параметры цвета; каждый из параметров "r", "g," и "b" должен быть целым числом в интервале от 0 до 255 включительно')

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
                print('Указано количество сторон не равное 1 или указанное значение не является целым положительным числом')
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




# figure = Figure([4, 6, 8], 7, 4, 5, 9, 11, filled= True )
# print(figure.get_color())
# print(figure.get_sides())
# figure.set_color(85, 296, 178)
# figure.set_color(47, 68, 135)
# print(figure.get_color())
# figure.set_sides(9, 3, 8, 4, 5, 2, 1)
# figure.set_sides(8, 1, 7, 3, 6)
# print(figure.get_sides())
# print(figure.__len__())
# print(figure.sides_count)

# circle = Circle([89, 148, 96], 7, 8, 9)
# print(circle.get_color())
# print(circle.get_sides())
# circle = Circle([89, 148, 96], 7)
# print(circle.get_color())
# print(circle.get_sides())
# circle.set_color(35, 177.7, 251)
# circle.set_color(97, 185, 206)
# print(circle.get_color())
# circle.set_sides(8, 9, 10)
# circle.set_sides(16)
# print(circle.get_sides())
# print(circle.radius)
# print(circle.get_square())
# print(circle.__len__())
# print(circle.sides_count)

# triangle = Triangle([128, 39, 216], 3, 4, 5, 6, 7)
# print(triangle.get_color())
# print(triangle.get_sides())
# triangle = Triangle([128, 39, 216], 3, 4, 5)
# print(triangle.get_color())
# print(triangle.get_sides())
# triangle.set_color(87, 346, 219)
# triangle.set_color(78, 235, 144)
# print(triangle.get_color())
# triangle.set_sides(6, 5, 2, 7, 11)
# triangle.set_sides(7, 9, 11)
# print(triangle.get_sides())
# print(triangle.get_square())
# print(triangle.__len__())
# print(triangle.sides_count)

# cube = Cube([89, 194, 235], 8, 9, 10)
# print(cube.get_color())
# print(cube.get_sides())
# cube = Cube([89, 194, 235], 8)
# print(cube.get_color())
# print(cube.get_sides())
# cube.set_color(47, 259, 138)
# cube.set_color(76, 244, 112)
# print(cube.get_color())
# cube.set_sides(7.5)
# cube.set_sides(7)
# print(cube.get_sides())
# print(cube.get_volume())
# print(cube.__len__())
# print(cube.sides_count)

