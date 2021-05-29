import math
import unittest
import random

def wallis(n):
    pi2=1
    for i in range(1,n+1):
        a= 4*i**2
        b=a/(a-1)
        pi2=pi2*b
    return 2*pi2    

def monte_carlo(n):
    circle_=0
    square_=0
    for i in range(n):
        rand_x= random.uniform(-1, 1)
        rand_y= random.uniform(-1, 1)
        
        if rand_x**2 + rand_y**2<=1:
            circle_+=1
        square_+=1
    pi3=4*circle_/square_
    return pi3


class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
