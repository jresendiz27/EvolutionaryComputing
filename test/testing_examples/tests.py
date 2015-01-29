__author__ = 'alberto'
import unittest
from src.SimpleCalculator import SimpleCalculator
from escom.pepo.genetic_algorithms.selectors.roulette import roulette_selector
from escom.pepo.genetic_algorithms.selectors.strict import strict_selector


class TestSelectors(unittest.TestCase):
    def setUp(self):
        # test population
        self.population = [[1, 1, 0, 0, 0, 1, 0, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1],
                           [0, 0, 0, 1, 0, 1, 1, 1]]
        # test fitness
        self.fitness = [0.4, 0.4, 0.2, 0.4]

    def test_roulette_selector(self):
        self.assertEqual(2, roulette_selector(self.fitness))

    def test_strict_selector(self):
        self.assertEqual(2, strict_selector(self.fitness, asc=True))