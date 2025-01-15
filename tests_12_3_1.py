from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walking = Runner('Миша')
        for i in range(10):
            walking.walk()
        self.assertEqual(walking.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        running = Runner('Гриша')
        for i in range(10):
            running.run()
        self.assertEqual(running.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walking = Runner('Миша')
        running = Runner('Гриша')
        for i in range(10):
            walking.walk()
            running.run()
        self.assertNotEqual(walking.distance, running.distance)

if __name__ == '__main__':
    unittest.main()

