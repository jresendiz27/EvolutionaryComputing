__author__ = 'alberto'
import random

CHROMOSOME_LENGTH = 8
POPULATION_SIZE = 4
NUMBER_OF_GENERATIONS = 5000
FITNESS_WEIGHT = 0.1
EPSILON = 0.01
chromosome = [random.randint(0, 1) for i in range(0, CHROMOSOME_LENGTH)]


def init():
    return [[random.randint(0, 1) for i in range(0, CHROMOSOME_LENGTH)] for j in range(0, POPULATION_SIZE)]


def print_single(single, fitness):
    print single, " => ", fitness


def print_population(population, fitness):
    i = 0
    for single in population:
        single_fitness = fitness[i]
        print_single(single, single_fitness)
        i = i + 1


def fitness_calculation(single):
    fitness = 0.0
    for gen in single:
        if gen == 0:
            fitness = fitness + FITNESS_WEIGHT
    return fitness


def population_fitness(population):
    fitness = []
    for single in population:
        fitness.append(fitness_calculation(single))
    return fitness


def choose_single(fitness):
    fitness_sum = sum(fitness)
    fitness_average = fitness_sum / POPULATION_SIZE

    expected_values = []
    for single_fitness in fitness:
        expected_value = single_fitness / fitness_average
        expected_values.append(expected_value)

    random_number = random.random() * POPULATION_SIZE  # same as random.random()*T
    partial_sum = 0.0
    index = 0
    for expected_value in expected_values:
        partial_sum = partial_sum + expected_value
        if partial_sum >= random_number:
            return index
        index = index + 1


def one_point_crosses(father, mother):
    cross_point = random.randint(1, CHROMOSOME_LENGTH - 1)
    #
    left_side_father = father[0:cross_point]
    right_side_father = father[cross_point:CHROMOSOME_LENGTH]
    #
    left_side_mother = mother[0:cross_point]
    right_side_mother = mother[cross_point:CHROMOSOME_LENGTH]
    #
    son_one = left_side_father + right_side_mother
    son_two = left_side_mother + right_side_father

    return son_one, son_two


def mutate(single):
    mutation_point = random.randint(0, CHROMOSOME_LENGTH - 1)
    if single[mutation_point] is 1:
        single[mutation_point] = 0
    else:
        single[mutation_point] = 1


def generate_new_population(population, fitness):
    new_population = []
    for i in range(0, int(POPULATION_SIZE / 2)):
        position_one = choose_single(fitness)
        position_two = choose_single(fitness)
        #
        father = population[position_one]
        mother = population[position_two]
        #
        son_one, son_two = one_point_crosses(father, mother)
        #
        mutate(son_one)
        mutate(son_two)
        #
        new_population.append(son_one)
        new_population.append(son_two)
    new_population = population + new_population
    return new_population


def choose_best(population):
    return sorted(population, key=fitness_calculation, reverse=True)


def find_best(n):
    population = init()
    fitness = population_fitness(population)
    for i in range(0, NUMBER_OF_GENERATIONS):
        value = FITNESS_WEIGHT * CHROMOSOME_LENGTH - EPSILON
        if fitness[0] >= value:
            print "**" * 60 + "\n"
            print "Found at %s generation!" % (str(i))
            print_single(population[0], fitness[0])
            print "**" * 60 + "\n"
            break
        new_population = generate_new_population(population, fitness)
        population = (choose_best(new_population))[0:POPULATION_SIZE]
        fitness = population_fitness(population)
        print "+-" * 60 + "\n"
        print "Generation: ", i
        print "Single : ", population[0]
        print "Fitness : ", fitness[0]
        print "+-" * 60 + "\n"
        #
    return population[0:n]


if __name__ == '__main__':
    find_best(1)