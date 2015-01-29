__author__ = 'alberto'
from escom.pepo.config import CHROMOSOME_LENGTH, POPULATION_SIZE, random, logger

log = logger.getLogger(__file__)

def generate_population(chromosome_min_value, chromosome_max_value, generator=None):
    if generator:
        return [[generator(chromosome_min_value, chromosome_max_value) for i in range(0, CHROMOSOME_LENGTH)] for j
                in range(0, POPULATION_SIZE)]
    else:
        return [[random.randint(chromosome_min_value, chromosome_max_value) for i in range(0, CHROMOSOME_LENGTH)] for j
                in range(0, POPULATION_SIZE)]


def show_population(population, fitness):
    log.info("Population ")
    for index in range(0, len(population)):
        log.info("%f => %f", (population[index], fitness[index]))


def generate_new_population(population, fitness):
    pass