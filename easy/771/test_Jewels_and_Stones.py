import unittest
from Jewels_and_Stones import Solution


class JewelsStonesTest(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_count(self):
        sl = Solution()
        self.assertEqual(3, sl.numJewelsInStones("aA", "aAAbbbb"))
        self.assertEqual(3, sl.numJewelsInStones("aA", "aAbbbb"))
        self.assertEqual(0, sl.numJewelsInStones("z", "ZZ"))


if __name__ == "__main__":
    unittest.main()
