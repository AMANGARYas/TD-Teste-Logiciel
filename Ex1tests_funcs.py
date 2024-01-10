
import unittest
import Ex1funcs 
class TestFuncs(unittest.TestCase):

    def test_max_three(self):
        self.assertEqual(Ex1funcs.max_three([5, 2, 8, 1, 7]), [8, 7, 5])
        self.assertEqual(Ex1funcs.max_three([10, 20, 30, 40, 50]), [50, 40, 30])
        self.assertEqual(Ex1funcs.max_three([1, 2, 3]), [3, 2, 1])
        self.assertEqual(Ex1funcs.max_three([-5, -2, -8, -1, -7]), [-1, -2, -5])
        self.assertEqual(Ex1funcs.max_three([]), [])

    def test_min_n(self):
        self.assertEqual(Ex1funcs.min_n([5, 2, 8, 1, 7], 3), [1, 2, 5])
        self.assertEqual(Ex1funcs.min_n([10, 20, 30, 40, 50], 2), [10, 20])
        self.assertEqual(Ex1funcs.min_n([1, 2, 3], 1), [1])
        self.assertEqual(Ex1funcs.min_n([-5, -2, -8, -1, -7], 4), [-8, -7, -5, -2])
        self.assertEqual(Ex1funcs.min_n([], 5), [])


             



if __name__ == '__main__':
    unittest.main()

