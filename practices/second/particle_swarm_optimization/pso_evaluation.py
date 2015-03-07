__author__ = 'azu'

import random
import numpy as np

from practices.config import SELECTED_FUNCTION, POPULATION_SIZE, NUMBER_OF_GENERATIONS, EPSILON, PRINTING_INTERVAL
from escom.pepo.utils import measure_time
from practices.second.particle_swarm_optimization.pso_fitness import function
from escom.pepo.config import NUMBER_OF_VARIABLES, VARIABLE_RANGE_START, VARIABLE_RANGE_END, VELOCITY_RANGE_START, \
    VELOCITY_RANGE_END, \
    logger


class Particle:
    def __init__(self):
        self.position = generate_random_array(NUMBER_OF_VARIABLES, VARIABLE_RANGE_START, VARIABLE_RANGE_END)
        self.velocity = generate_random_array(NUMBER_OF_VARIABLES, VELOCITY_RANGE_START, VELOCITY_RANGE_END)
        self.fitness = evaluate(self.position)
        self.best = self.position + 0

    def __str__(self):
        return "Position: " + str(self.position) + " Velocity: " + str(self.velocity) + " Fitness: " + str(
            self.fitness) + " Best: " + str(self.best)

    def move_position(self, best_of_all):
        self.position += self.velocity
        self.velocity = self.velocity + [x * random.random() for x in (self.best - self.position)] + [
            x * random.random() for x in (best_of_all - self.position)]
        new_fitness = evaluate(self.position)
        if new_fitness < evaluate(self.best):
            self.best = self.position + 0
        self.fitness = new_fitness


def generate_random_array(size, start, end):
    return np.asarray([random.random() * (end - start) + start for i in range(size)])


def evaluate(position):
    return function[SELECTED_FUNCTION](position)


def get_best_of_all(population, actual_best):
    # Get fitnesses for each best particle position
    fitness = [evaluate(p.best) for p in population]
    # Get best position [x,y,...] in actual population
    new_best = population.__getitem__(fitness.index(min(fitness))).best
    if evaluate(new_best) < evaluate(actual_best):  # If there's a new "best position ever"
        return new_best
    return actual_best


def generate_population():
    population = []
    for i in range(POPULATION_SIZE):
        particle = Particle()
        # logger.debug("%s", particle)
        population.append(particle)
    return population


@measure_time
def start_pso():
    logger.info("*" * 80)
    logger.info("*" * 80)
    logger.info("Particle Swarm Optimization")
    logger.info("*" * 80)
    logger.info("Number of Generations: %s", NUMBER_OF_GENERATIONS)
    logger.info("Population Size: %s", POPULATION_SIZE)
    logger.info("Function: %s", SELECTED_FUNCTION)
    logger.info("Epsilon: %s", EPSILON)
    logger.info("*" * 80)
    logger.info("*" * 80)
    # Generate population[] of Particle()
    population = generate_population()
    # Get the best position in population
    best_of_all = get_best_of_all(population, population[0].best)
    logger.info("Best: %s Fitness: %s", best_of_all, evaluate(best_of_all))

    for y in range(NUMBER_OF_GENERATIONS):
        if abs(evaluate(best_of_all)) < EPSILON:  # Stop condition
            logger.info("*" * 80)
            logger.info("Best solution found at %s generation.", y)
            logger.info("Best  of all: %s Fitness: %s", str(best_of_all), str(evaluate(best_of_all)))
            logger.info("*" * 80)
            break

        for particle in population:
            # Move each particle using its velocity
            particle.move_position(best_of_all)
        # Update best position ever in population's history
        best_of_all = get_best_of_all(population, best_of_all)
        # logger,info("%s", particle)
        if y % PRINTING_INTERVAL == 0:
            logger.debug("-" * 80)
            logger.debug("Generation: %s", y)
            logger.debug("Best  of all: %s Fitness: %s", str(best_of_all), str(evaluate(best_of_all)))
            logger.debug("-" * 80)

    logger.info("*" * 80)
    logger.info("No better solution found. ")
    logger.info("Best solution at %s generation", NUMBER_OF_GENERATIONS)
    logger.info("Best  of all: %s Fitness: %s", str(best_of_all), str(evaluate(best_of_all)))
    logger.info("*" * 80)

    return population


if __name__ == '__main__':
    result = start_pso()