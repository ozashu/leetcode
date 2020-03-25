import unittest
from defangIPaddr import Solution


class TestdefangIPaddr(unittest.TestCase):
    def test_defanging(self):
        sl = Solution()
        self.assertEquals('1[.]1[.]1[.]1', sl.defangIPaddr('1.1.1.1'))


if __name__ == '__main__':
    unittest.main()
