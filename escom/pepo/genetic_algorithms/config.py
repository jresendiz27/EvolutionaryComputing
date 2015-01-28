__author__ = 'alberto'

import random

CHROMOSOME_LENGTH = 8
POPULATION_SIZE = 4
NUMBER_OF_GENERATIONS = 5000
FITNESS_WEIGHT = 0.1
EPSILON = 0.01
chromosome = [random.randint(0, 1) for i in range(0, CHROMOSOME_LENGTH)]

try:
    from second.config import *
except:
    print "Warning: Running without a local_settings file"
