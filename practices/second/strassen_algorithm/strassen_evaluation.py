__author__ = 'alberto'
from escom.pepo.config import logger
from escom.pepo.config import STRASSEN_PRODUCTS
from escom.pepo.config import STRASSEN_CHROMOSOME, PRODUCT_SIZE, NUMBER_OF_PRODUCTS
import random
from escom.pepo.genetic_algorithms.components.population import *


def strassen_fitness(current_population):
    fitness = np.array([])
    for single in current_population:
        np.append(fitness, compare_chromosome(single))
    return fitness


def compare_chromosome(chromosome_b):
    generated_products = extract_products(chromosome_b)
    value = 0.0
    for index in range(0, 7):
        value = value + evaluate_product(STRASSEN_PRODUCTS[index], generated_products[index])
    return value


def extract_products(single):
    products = np.array([])
    for i in range(0, NUMBER_OF_PRODUCTS * PRODUCT_SIZE, PRODUCT_SIZE):  # considering a defined product size
        np.append(products, single[i:i + PRODUCT_SIZE])
    return products


def evaluate_product(original_product, generated_product):
    evaluation = 0.0
    for index in range(0, PRODUCT_SIZE):
        # First evaluation
        if original_product[index] == generated_product[index]:
            evaluation += 10
            continue
        # Second Evaluation
        if np.abs(original_product[index]) == np.abs(generated_product[index]):
            evaluation += 2
        else:
            evaluation -= 7
    return evaluation


def start_evaluation():
    logger.info("*" * 60)
    logger.info("Starting Strassen Finder")
    logger.info("*" * 60)
    # generating population
    logger.info("Starting population generation")
    population = generate_population(-1, 1)
    logger.info(population)
    fitness = strassen_fitness(population)
    logger.info(fitness)


if __name__ == '__main__':
    start_evaluation()