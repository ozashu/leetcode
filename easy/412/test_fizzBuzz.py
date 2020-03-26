import unittest
from fizzBuzz import Solution


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.sl = Solution()

    def testSimpleImput(self):
        self.assertEqual(self.sl.fizzBuzz(1), ['1'])

    def testFizzBuzz(self):
        ans = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
        self.assertEqual(self.sl.fizzBuzz(10), ans)

    def testMinusInput(self):
        self.assertEqual(self.sl.fizzBuzz(-1), [])

    def testZeroInput(self):
        self.assertEqual(self.sl.fizzBuzz(0), [])


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFizzBuzz)
    unittest.TextTestRunner(verbosity=2).run(suite)
