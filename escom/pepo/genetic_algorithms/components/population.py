__author__ = 'alberto'
from escom.pepo.config import CHROMOSOME_LENGTH, OFFSPRING_POPULATION_SIZE, FITNESS_WEIGHT, logger, np
from escom.pepo.genetic_algorithms.components.selectors import *
from escom.pepo.genetic_algorithms.components.crosses import one_point_crosses
from escom.pepo.genetic_algorithms.components.mutation import whole_mutation


def generate_population(chromosome_min_value, chromosome_max_value, generator=None):
    if generator:
        return [[generator(chromosome_min_value, chromosome_max_value) for i in range(0, CHROMOSOME_LENGTH)] for j
             in range(0, POPULATION_SIZE)]
    else:
        return [[random.randint(chromosome_min_value, chromosome_max_value) for i in range(0, CHROMOSOME_LENGTH)] for j
             in range(0, POPULATION_SIZE)]


def show_population(population, fitness):
    logger.info("Population ")
    for index in range(0, POPULATION_SIZE):
        logger.info("%f => %f", (population[index], fitness[index]))


def generate_new_population(population, fitness, **kwargs):
    new_population = []
    for i in range(0, int(OFFSPRING_POPULATION_SIZE)):
        father_pos = roulette_selector(fitness)
        mother_pos = roulette_selector(fitness)

        father = population[father_pos]
        mother = population[mother_pos]

        offsprings = one_point_crosses(father, mother)

        for son in offsprings:
            if kwargs['mutator']:
                whole_mutation(son, kwargs['mutator'])
            else:
                whole_mutation(son, kwargs['mutator'])
            new_population.append(son)

    return np.append(population, new_population)


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
            fitness = np.append(fitness, fitness_function(single))
    else:
        for single in population:
            fitness = np.append(fitness, binary_fitness(single))
    return fitness


def choose_best(population, fitness_evaluator, number_of_singles=POPULATION_SIZE, reversed_order=True):
    return sorted(population, key=fitness_evaluator, reverse=reversed_order)[0:number_of_singles]