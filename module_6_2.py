class Vehicle:
    _COLOR_VARIANTS = [',белый', 'красный', 'серый', 'чёрный', 'синий']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in self._COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Михайлов М.М.', 'ВАЗ 2105', 71, 'сафари')
vehicle2 = Sedan('Иванов И.И.', 'Audi 100', 174, 'зелёный')
vehicle3 = Sedan('Петров Н.В.', 'Maybach S 680', 612, 'Nautical Blue Metallic')
vehicle4 = Sedan('Королёв Г.С.', 'Skoda Octavia', 110, 'бежевый металлик')

vehicle1.print_info()
vehicle2.print_info()
vehicle3.print_info()
vehicle4.print_info()
vehicle1.set_color('серый металлик')
vehicle2.owner = 'Папандопулос О.Н.'
vehicle3.set_color('ЧЁРНЫЙ')
vehicle4.set_color('серый')
vehicle1.print_info()
vehicle2.print_info()
vehicle3.print_info()
vehicle4.print_info()
