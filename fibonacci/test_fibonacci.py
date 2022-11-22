import unittest
import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fib1(self):
        self.assertEqual(fibonacci.fib1(7), 13)
        self.assertEqual(fibonacci.fib1(30), 832040)
        
        # self.assertEqual(fibonacci.fib1(100), 354224848179261915075)

    def test_fib2(self):
        self.assertEqual(fibonacci.fib2(7), 13)
        self.assertEqual(fibonacci.fib2(30), 832040)
        self.assertEqual(fibonacci.fib2(53), 53316291173)
        self.assertEqual(fibonacci.fib2(300), 222232244629420445529739893461909967206666939096499764990979600)

    def test_fib3(self):
        self.assertEqual(fibonacci.fib3(7), 13)
        self.assertEqual(fibonacci.fib3(30), 832040)
        self.assertEqual(fibonacci.fib3(53), 53316291173)
        self.assertEqual(fibonacci.fib3(300), 222232244629420445529739893461909967206666939096499764990979600)

    def test_fib4(self):
        self.assertEqual(fibonacci.fib4(7), 13)
        self.assertEqual(fibonacci.fib4(30), 832040)
        self.assertEqual(fibonacci.fib4(53), 53316291173)
        self.assertEqual(fibonacci.fib4(300), 222232244629420445529739893461909967206666939096499764990979600)

if __name__ == "__main__":
    unittest.main()
