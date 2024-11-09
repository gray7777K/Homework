class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

animal1 = Mammal('Буйвол')
animal2 = Mammal('Бабуин')
animal3 = Predator('Волк')
animal4 = Predator('Тигр')
plant1 = Fruit('Грейпфрут')
plant2 = Fruit('Банан')
plant3 = Flower('Безвременник')
plant4 = Flower('Ландыш')

print(animal1.name)
print(animal2.name)
print(animal3.name)
print(animal4.name)
print(plant1.name)
print(plant2.name)
print(plant3.name)
print(plant4.name)
print(animal2.alive)
print(animal2.fed)
print(animal3.alive)
print(animal3.fed)
animal1.eat(plant3)
print(animal1.alive)
print(animal1.fed)
animal2.eat(plant2)
print(animal2.alive)
print(animal2.fed)
animal3.eat(plant4)
print(animal3.alive)
print(animal3.fed)
animal4.eat(plant1)
print(animal4.alive)
print(animal4.fed)
