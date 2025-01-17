from rt_with_exceptions import Runner
import unittest
import logging

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            walking = Runner('Игорь', -5)
            for i in range(10):
                walking.walk()
            self.assertEqual(walking.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info = True)


    def test_run(self):
        try:
            running = Runner(['Миша', 'Гриша', 'Коля'], 10)
            for i in range(10):
                running.run()
            self.assertEqual(running.distance, 200)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info = True)



logging.basicConfig(level = logging.INFO, filemode = 'w', encoding = 'utf-8',
                    filename ='runner_tests.log',
                    format = '%(asctime)s | %(levelname)s | %(message)s')

if __name__ == '__main__':
    unittest.main()
