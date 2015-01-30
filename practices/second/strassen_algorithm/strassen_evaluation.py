__author__ = 'alberto'
from escom.pepo.config import logger
from escom.pepo.config import STRASSEN_PRODUCTS
from escom.pepo.genetic_algorithms.components.population import *


def strassen_fitness(current_population):
    fitness = np.array([])
    for single in current_population:
        for strassen_chromosome in STRASSEN_PRODUCTS:
            fitness.append(compare_chromosomes(strassen_chromosome, single))
    return fitness


def compare_chromosomes(chromosome_a, chromosome_b):
    pass


if __name__ == '__main__':
    logger.info("*" * 60)
    logger.info("Starting Strassen Finder")
    logger.info("*" * 60)
    # generating population
    logger.info("Starting population generation")
    population = generate_population(-1, 1)
    logger.info(population)
    fitness = strassen_fitness(population)
    logger.info(fitness)