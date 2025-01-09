from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walking = Runner('Миша')
        for i in range(10):
            walking.walk()
        self.assertEqual(walking.distance, 50)

    def test_run(self):
        running = Runner('Гриша')
        for i in range(10):
            running.run()
        self.assertEqual(running.distance, 100)

    def test_challenge(self):
        walking = Runner('Миша')
        running = Runner('Гриша')
        for i in range(10):
            walking.walk()
            running.run()
        self.assertNotEqual(walking.distance, running.distance)

if __name__ == '__main__':
    unittest.main()

