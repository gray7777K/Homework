import unittest
import tests_12_3_1, tests_12_3_2

Runner_and_TournamentST = unittest.TestSuite()

Runner_and_TournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_1.RunnerTest))
Runner_and_TournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity = 2)
runner.run(Runner_and_TournamentST)
