import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from utils import *

def test_small_integers(test_case):
    print("Running", "test_small_integers")
    test_case.runAsJava(adjust("""
        for i in range(100):
            for j in range(100):
                x = -5
                for k in range(-5, 257):
                    x = x + 1
        """), timed=True)

def test_booleans(test_case):
    print("Running", "test_booleans")
    test_case.runAsJava(adjust("""
        for i in range(100000):
            x = True
            y = False

            x = (not x and y)
            y = x != y

            x = True and True and True
            y = x or False

            x = not True or (not x) or True
            y = y == y

            x = y != (not x)
            y = False or True or (not y)

            x = (x != x) or (not False)
            y = y and y and (not x)

            x = False or False or False or False
            y = True and True and True and True

            x = 1 != 0
            y = (not (not (not (not (not (not (not x)))))))

            x = ((not y) and y) == ((not (not x)) or y or (not y))
            y = False or False or (not True) or (not True) or (not True)

            x = True and (not False) and True and (not False) and False
            y = (False != False) != False
        """), timed=True)

def main():
    test_case = TranspileTestCase()
    test_case.setUpClass()
    test_small_integers(test_case)
    test_booleans(test_case)

if __name__== "__main__":
  main()
