import sys
sys.path.append('C:/Users/Honor/PycharmProjects/LR3')
from src.lib import Fibonacchi
from src.lib import Bubble
from src.lib import Calculator

def test_Fibonacchi_correct():
    assert Fibonacchi(5) == [0, 1, 1, 2, 3]

def test_Fibonacchi_incorrect():
    assert Fibonacchi(5) == [1, 1, 2, 3, 5]

def test_Puzirec_correct():
    assert Bubble([4, 8, 1, 3, 9, 13, 0]) == [0, 1, 3, 4, 8, 9, 13]

def test_Puzirec_incorrect():
    assert Bubble([4, 8, 1, 3, 9, 13, 0]) == [4, 8, 3, 1, 9, 13, 0]

def test_Calc_correct():
    assert Calculator(13, 7, '+') == 20

def test_Calc_incorrect():
    assert Calculator(8, 2, '*') == 15
