import unittest

def square(x):
    val = x ** 2
    return val

class testsqr(unittest.TestCase):
    def sqr(self):
        result1 = square(4)
        result2 = square(3)
        self.assertEqual(result1, 16)
        self.assertEqual(result2, 2)

if __name__ == "__main__":
  unittest.main()