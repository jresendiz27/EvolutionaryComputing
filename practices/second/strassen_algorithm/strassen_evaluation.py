__author__ = 'alberto'
from escom.pepo.config import STRASSEN_CHROMOSOME, NUMBER_OF_GENERATIONS, EPSILON, logger
from escom.pepo.config import PRINTING_INTERVAL
from escom.pepo.genetic_algorithms.components.population import *
from escom.pepo.genetic_algorithms.components.mutation import random_mutation
from escom.pepo.utils import measure_time
import numpy as np


def strassen_fitness(current_population):
    fitness = []
    for single in current_population:
        fitness.append(evaluate_product(single))
    return fitness


def evaluate_product(single):
    current_chromosome = np.asarray(STRASSEN_CHROMOSOME)
    generated_chromosome = np.asarray(single)
    return sum(abs(current_chromosome - generated_chromosome))


def strassen_mutation(allele):
    if allele == 1:
        return -1
    if allele == -1:
        return 1
    if allele == 0:
        rand_allele = random.randint(-1, 1)
        return rand_allele


@measure_time
def start_evaluation():
    logger.info("*" * 80)
    logger.info("*" * 80)
    logger.info("Starting Strassen Finder")
    logger.info("*" * 80)
    logger.info("Number of Generations: %s", NUMBER_OF_GENERATIONS)
    logger.info("Chromosome Length: %s", CHROMOSOME_LENGTH)
    logger.info("Population Size: %s", POPULATION_SIZE)
    logger.info("*" * 80)
    logger.info("*" * 80)
    # generating population
    population = generate_population(-1, 1)
    fitness = strassen_fitness(population)
    #
    ancestor = fitness[0]
    for i in range(0, NUMBER_OF_GENERATIONS):
        if fitness[0] < EPSILON:
            logger.info("*" * 80)
            logger.info("Best solution found at %s generation.", i)
            logger.info(population[0])
            logger.info(fitness[0])
            logger.info("*" * 80)
            break

        # There's no change, let's create an unfortunate event!
        if (ancestor == fitness[0]) and (i % (PRINTING_INTERVAL / 2) == 0):
            logger.debug("Wake Up!!!!")
            new_sons = one_point_crosses(population[0], population[1])
            population[2] = new_sons[0]
            population[-1] = random_mutation(population[-1], -1, 1)
        else:
            ancestor = fitness[0]

        new_population = generate_new_population(population, fitness, mutator=strassen_mutation)
        population = sorted(new_population, key=evaluate_product, reverse=False)[0:POPULATION_SIZE]
        fitness = strassen_fitness(population)

        if i % PRINTING_INTERVAL == 0:
            #
            logger.debug("-" * 80)
            logger.debug("Generation %s ", i)
            logger.debug("BEST :")
            logger.debug("Single %s ", population[0])
            logger.debug("Fitness %s ", fitness[0])
            logger.debug("." * 80)
            logger.debug("WORST :")
            logger.debug("Single %s ", population[-1])
            logger.debug("Fitness %s ", fitness[-1])
            logger.debug("-" * 80)

    logger.info("*" * 80)
    logger.info("No better solution found. ")
    logger.info("Best solution at %s generation", NUMBER_OF_GENERATIONS)
    logger.info(population[0])
    logger.info(fitness[0])
    logger.info("*" * 80)

    return population


if __name__ == '__main__':
    result = start_evaluation()
