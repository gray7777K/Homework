import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        days_counter = 0
        live_enemies = 100
        while live_enemies:
            time.sleep(1)
            days_counter += 1
            live_enemies -= self.power
            if live_enemies < 0:
                live_enemies = 0
            print(f'{self.name} сражается {days_counter} дней(дня)..., осталось {live_enemies} воинов(воина, воин)\n', end = '')
        print(f'{self.name} одержал победу спустя {days_counter} дней(дня)!')

first_knight = Knight('Sir Gawain', 15)
second_knight = Knight('Sir Percival', 33)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')