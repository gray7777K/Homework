from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        return cls.all_results

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)
        return self.runner1, self.runner2, self.runner3

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        tournament1 = Tournament(90, self.runner1, self.runner3)
        result = tournament1.start()
        result_name = {i: str(j) for i, j in result.items()}
        max_key = max(result_name.keys())
        last_res = result_name.get(max_key)
        self.assertEqual(last_res, 'Ник')
        self.all_results.append(result_name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        tournament2 = Tournament(90, self.runner2, self.runner3)
        result = tournament2.start()
        result_name = {i: str(j) for i, j in result.items()}
        max_key = max(result_name.keys())
        last_res = result_name.get(max_key)
        self.assertEqual(last_res, 'Ник')
        self.all_results.append(result_name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        tournament3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament3.start()
        result_name = {i: str(j) for i, j in result.items()}
        max_key = max(result_name.keys())
        last_res = result_name.get(max_key)
        self.assertEqual(last_res, 'Ник')
        self.all_results.append(result_name)

if __name__ == '__main__':
    unittest.main()
