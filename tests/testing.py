import unittest

from ripasso.ripasso import Calc

class TestCalculations(unittest.TestCase):

    def setUp(self) -> None:
        self.calculations=Calc(8,2)
    
    def test_sum(self):
        self.assertEqual(self.calculations.get_sum(),10,"The sum is wrong.")