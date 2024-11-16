from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, cords = [0, 0, 0]):
        self.speed = speed
        self._cords = cords

    def move(self, dx, dy, dz):
        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] = dx * self.speed
            self._cords[1] = dy * self.speed
            self._cords[2] = dz * self.speed

    def get_cords(self):
        print(f'X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}')

    def attack(self):
        if 0 <= self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
        else:
            pass

    def speak(self):
        pass

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        num_eggs = randint(1, 4)
        print(f'Here are(is) {num_eggs} eggs for you')

class AquaticAnimal (Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * self.speed/ 2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, name, sound = 'Click-click-click'):
        super().__init__(name)
        self.sound = sound

    def speak(self):
        print(self.sound)

db = Duckbill(13)

print(db.live)
print(db.beak)

db.get_cords()

db.lay_eggs()

db.move(5, -8, -10)
db.get_cords()

db.move(9, 7, 15)
db.get_cords()

db.dive_in(-31)
db.get_cords()

db.attack()

db.speak()
