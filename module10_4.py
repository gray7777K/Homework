from queue import Queue
from random import randint
import time
import threading

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            if any(table.guest is None for table in self.tables):
                for table in self.tables:
                    if table.guest is None:
                        table.guest = guest
                        print(f'{guest.name} сел(-а) за стол номер {table.number}.\n', end = '')
                        table.guest.start()
                        break
                    else:
                        continue
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди.\n', end = '')

    def discuss_guests(self):
        while not self.queue.empty() or any(not table.guest is None for table in self.tables):
            for table in self.tables:
                if not table.guest is None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла).\n', end = '')
                    print(f'Стол номер {table.number} свободен.\n', end = '')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.\n', end = '')
                    table.guest.start()

tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
