__author__ = 'alberto'

from escom.pepo.config import POPULATION_SIZE
from escom.pepo.config import random
#Returns the index of the most suitable
def roulette_selector(fitness):
    fitness_sum = sum(fitness)
    fitness_average = fitness_sum / POPULATION_SIZE

    expected_values = []
    for single_fitness in fitness:
        expected_value = single_fitness / fitness_average
        expected_values.append(expected_value)

    random_number = random.random() * POPULATION_SIZE  # same as random.random()*T
    partial_sum = 0.0
    index = 0
    for expected_value in expected_values:
        partial_sum = partial_sum + expected_value
        if partial_sum >= random_number:
            return index
        index = index + 1