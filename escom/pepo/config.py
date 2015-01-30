__author__ = 'alberto'

import random
import logging
import numpy as np
# Genetic Algorithms basic configuration
CHROMOSOME_LENGTH = 8
POPULATION_SIZE = 4
OFFSPRING_POPULATION_SIZE = (POPULATION_SIZE / 2)
NUMBER_OF_SONS_PER_CROSS = 1
NUMBER_OF_GENERATIONS = 5000
FITNESS_WEIGHT = 0.1
EPSILON = 0.01
# Extra configuration
DEBUG = False
# Importing special config
try:
    from practices.config import *
except:
    print "No local configuration file"
#Configuring logger
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()