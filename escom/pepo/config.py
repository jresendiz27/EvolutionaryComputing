__author__ = 'alberto'

import random
import logging
# Genetic Algorithms basic configuration
CHROMOSOME_LENGTH = 8
POPULATION_SIZE = 4
NUMBER_OF_GENERATIONS = 5000
FITNESS_WEIGHT = 0.1
EPSILON = 0.01
chromosome = [random.randint(0, 1) for i in range(0, CHROMOSOME_LENGTH)]
# Extra configuration
DEBUG = False
#Importing special config
try:
    from practices.config import *
except:
    print "No local configuration file"
#Configuring logger
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)