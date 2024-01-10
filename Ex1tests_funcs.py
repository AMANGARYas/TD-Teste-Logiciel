
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


    def test_is_prime(self):
        self.assertTrue(Ex1funcs.is_prime(2))      
        self.assertTrue(Ex1funcs.is_prime(3))      
        self.assertTrue(Ex1funcs.is_prime(5))      
        self.assertFalse(Ex1funcs.is_prime(4))     
        self.assertFalse(Ex1funcs.is_prime(9))     
        self.assertTrue(Ex1funcs.is_prime(11))    
        self.assertFalse(Ex1funcs.is_prime(1))     
        self.assertFalse(Ex1funcs.is_prime(0))     
        self.assertFalse(Ex1funcs.is_prime(-7))   
        self.assertTrue(Ex1funcs.is_prime(13))                 

    def test_is_arithmetic_sequence(self):
        self.assertTrue(Ex1funcs.is_arithmetic_sequence([2, 4, 6, 8, 10]))   
        self.assertTrue(Ex1funcs.is_arithmetic_sequence([1, 5, 9, 13, 17]))  
        self.assertTrue(Ex1funcs.is_arithmetic_sequence([3, 0, -3, -6, -9]))  
        self.assertFalse(Ex1funcs.is_arithmetic_sequence([1, 3, 6, 10, 15]))  
        self.assertFalse(Ex1funcs.is_arithmetic_sequence([2, 5, 10, 17, 26])) 
        self.assertTrue(Ex1funcs.is_arithmetic_sequence([]))                


if __name__ == '__main__':
    unittest.main()

