__author__ = 'alberto'
import unittest
from src.SimpleCalculator import SimpleCalculator


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_sum_method_should_return_correct_result(self):
        self.assertEqual(7, self.calc.sum([4, 3]))

    def test_multiply_method_should_return_correct_result(self):
        self.assertEqual(12, self.calc.multiply([4, 3]))