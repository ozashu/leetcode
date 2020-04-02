import unittest
from singlenumber import Solution


class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def testSimpleImput(self):
        self.assertEqual(self.sl.singleNumber([2, 2, 1]))

    def testAllSame(self):
        self.assertEqual(self.sl.singleNumber([3, 3, 3, 3]))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSingleNumber)
    unittest.TextTestRunner(verbosity=2).run(suite)
