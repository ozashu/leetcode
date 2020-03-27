import unittest
from HowManyNumbersAreSmallerThantheCurrentNumber import Solution


class TestCountNumbers(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def testSimpleImput(self):
        self.assertEqual(self.sl.smallerNumbersThanCurrent(
            [8, 1, 2, 2, 3]), [4, 0, 1, 1, 3])

    def testAllSama(self):
        self.assertEqual(self.sl.smallerNumbersThanCurrent(
            [7, 7, 7, 7]), [0, 0, 0, 0])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCountNumbers)
    unittest.TextTestRunner(verbosity=2).run(suite)
