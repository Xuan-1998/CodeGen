import unittest

class TestSolution(unittest.TestCase):
    def test_small_input(self):
        self.assertEqual(solve(2), '3 6 6 3')

    def test_large_input(self):
        self.assertEqual(solve(10), '1 5 15 40 90 182 326 553 931 1654')

if __name__ == '__main__':
    unittest.main()
