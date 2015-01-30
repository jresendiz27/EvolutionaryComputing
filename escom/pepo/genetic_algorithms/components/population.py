__author__ = 'alberto'
from escom.pepo.config import CHROMOSOME_LENGTH, OFFSPRING_POPULATION_SIZE, FITNESS_WEIGHT, logger, np
from escom.pepo.genetic_algorithms.components.selectors import *
from escom.pepo.genetic_algorithms.components.crosses import one_point_crosses
from escom.pepo.genetic_algorithms.components.mutation import whole_mutation


def generate_population(chromosome_min_value, chromosome_max_value, generator=None):
    if generator:
        return np.asarray(
            [[generator(chromosome_min_value, chromosome_max_value) for i in range(0, CHROMOSOME_LENGTH)] for j
             in range(0, POPULATION_SIZE)])
    else:
        return np.asarray(
            [[random.randint(chromosome_min_value, chromosome_max_value) for i in range(0, CHROMOSOME_LENGTH)] for j
             in range(0, POPULATION_SIZE)])


def show_population(population, fitness):
    logger.info("Population ")
    for index in range(0, POPULATION_SIZE):
        logger.info("%f => %f", (population[index], fitness[index]))


def generate_new_population(population, fitness):
    new_population = np.array([])
    for i in range(0, range(0, int(OFFSPRING_POPULATION_SIZE))):
        father_pos = roulette_selector(fitness)
        mother_pos = roulette_selector(fitness)

        father = population[father_pos]
        mother = population[mother_pos]

        offsprings = one_point_crosses(father, mother)

        for son in offsprings:
            whole_mutation(son)
            new_population.append(son)

    return population + new_population


def binary_fitness(single):
    fitness = 0.0
    for gen in single:
        if gen == 0:
            fitness = fitness + FITNESS_WEIGHT
    return fitness


def population_fitness(population, fitness_function=None):
    fitness = []
    if fitness_function:
        for single in population:
            fitness.append(fitness_function(single))
    else:
        for single in population:
            fitness.append(binary_fitness(single))
    return fitness