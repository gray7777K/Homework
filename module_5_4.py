class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

house1 = House('ЖК Лютик', 14)
print(House.houses_history)
house2 = House('ЖК Консорт', 8)
print(House.houses_history)
house3 = House('ЖК Изумруд', 18)
print(House.houses_history)
del house2
del house1
house4 = House('ЖК Вертикаль', 29)
print(House.houses_history)
del house3
house5 = House('ЖК Упоение', 6)
print(House.houses_history)
del house4
print(House.houses_history)
