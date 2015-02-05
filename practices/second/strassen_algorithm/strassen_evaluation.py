__author__ = 'alberto'
from escom.pepo.config import STRASSEN_PRODUCTS, PRODUCT_SIZE, NUMBER_OF_PRODUCTS, NUMBER_OF_GENERATIONS, logger
from escom.pepo.genetic_algorithms.components.population import *
import numpy as np


def strassen_fitness(current_population):
    fitness = []
    for single in current_population:
        fitness.append(compare_chromosome(single))
    return fitness


def compare_chromosome(chromosome_b):
    generated_products = extract_products(chromosome_b)
    return evaluate_product(generated_products)


def extract_products(single):
    products = []
    for i in range(0, NUMBER_OF_PRODUCTS * PRODUCT_SIZE, PRODUCT_SIZE):  # considering a defined product size
        partial = single[i:i + PRODUCT_SIZE]
        products.append(partial)
    return products


def evaluate_product(generated_product):
    evaluation = 0.0
    for index in range(0, NUMBER_OF_PRODUCTS):
        for allele in range(0, PRODUCT_SIZE):
            # First evaluation
            if STRASSEN_PRODUCTS[index][allele] == generated_product[index][allele]:
                evaluation += 10
                continue
            # Second Evaluation
            if np.abs(STRASSEN_PRODUCTS[index][allele]) == np.abs(generated_product[index][allele]):
                evaluation += 2
            else:
                evaluation -= 7
    return evaluation


def strassen_mutation(allele):
    if allele == 1:
        return -1
    if allele == -1:
        return 1
    if allele == 0:
        rand_allele = random.randint(-1, 1)
        return rand_allele


def start_evaluation():
    logger.info("*" * 60)
    logger.info("Starting Strassen Finder")
    logger.info("*" * 60)
    # generating population
    logger.info("Starting population generation")
    population = generate_population(-1, 1)
    fitness = strassen_fitness(population)

    for i in range(0, NUMBER_OF_GENERATIONS):
        current_value = CHROMOSOME_LENGTH * 8  # Considering 8 value per chromosome (10 == ideal case)
        if fitness[0] > current_value:
            logger.info("*" * 60)
            logger.info("Best solution found at %s generation.", i)
            logger.info(population[0])
            logger.info(fitness[0])
            logger.info("*" * 60)
            break
        new_population = generate_new_population(population, fitness, mutator=strassen_mutation)
        population = sorted(population, key=compare_chromosome, reverse=True)[0:POPULATION_SIZE]
        fitness = strassen_fitness(population)

        if i % 10 == 0:
            logger.debug("-" * 60 + "\n")
            logger.debug("Generation %s ", i)
            logger.debug("Single %s ", population[0])
            logger.debug("Fitness %s ", fitness[0])
            logger.debug("-" * 60 + "\n")
    return population


if __name__ == '__main__':
    start_evaluation()