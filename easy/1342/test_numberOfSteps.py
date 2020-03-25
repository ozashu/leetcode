import unittest
from numberOfSteps import Solution


class TestnumberOfSteps(unittest.TestCase):
    def test_steps(self):
        sl = Solution()
        self.assertEqual(6, sl.numberOfSteps(14))
        self.assertEqual(4, sl.numberOfSteps(8))
        self.assertEqual(12, sl.numberOfSteps(123))


if __name__ == '__main__':
    unittest.main()
