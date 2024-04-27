import unittest

class TestAlternateAppends(unittest.TestCase):
    def test_single_array(self):
        self.assertEqual(alternate_appends([1, 2, 3]), [1, None, 2, None, 3])

    def test_multiple_arrays(self):
        self.assertEqual(alternate_appends([1, 2], [3, 4], [5, 6]), [1, 3, None, 2, 4, None, 5, 6])

if __name__ == '__main__':
    unittest.main()
