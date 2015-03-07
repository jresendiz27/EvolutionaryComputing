__author__ = 'alberto, azu'

from escom.pepo.config import NUMBER_OF_GENERATIONS, EPSILON, logger, CURRENT_RESULT, CONSTANT_RESULT, CONSTANT_NON_ZERO
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
    generated_chromosome = np.asarray(single)
    generated_result = get_multiplication_result(generated_chromosome)
    return CONSTANT_RESULT * sum(abs(CURRENT_RESULT - generated_result)) + CONSTANT_NON_ZERO * np.count_nonzero(
        generated_chromosome)


def get_multiplication_result(chromosome):
    P1 = get_complete_product(chromosome[0:8])
    P2 = get_complete_product(chromosome[8:16])
    P3 = get_complete_product(chromosome[16:24])
    P4 = get_complete_product(chromosome[24:32])
    P5 = get_complete_product(chromosome[32:40])
    P6 = get_complete_product(chromosome[40:48])
    P7 = get_complete_product(chromosome[48:56])
    r = chromosome[56:63]
    s = chromosome[63:70]
    t = chromosome[70:77]
    u = chromosome[77:84]
    generated_r = r[0] * P1 + r[1] * P2 + r[2] * P3 + r[3] * P4 + r[4] * P5 + r[5] * P6 + r[6] * P7
    generated_s = s[0] * P1 + s[1] * P2 + s[2] * P3 + s[3] * P4 + s[4] * P5 + s[5] * P6 + s[6] * P7
    generated_t = t[0] * P1 + t[1] * P2 + t[2] * P3 + t[3] * P4 + t[4] * P5 + t[5] * P6 + t[6] * P7
    generated_u = u[0] * P1 + u[1] * P2 + u[2] * P3 + u[3] * P4 + u[4] * P5 + u[5] * P6 + u[6] * P7
    generated_result = np.asarray([])
    generated_result = np.append(generated_result, generated_r)
    generated_result = np.append(generated_result, generated_s)
    generated_result = np.append(generated_result, generated_t)
    generated_result = np.append(generated_result, generated_u)
    return generated_result


def get_complete_product(product):
    result = np.asarray([])
    for alelle in product[0:product.size / 2]:
        result = np.append(result, alelle * product[product.size / 2:product.size])
    return result

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
