__author__ = 'alberto'
import random

CHROMOSOME_LENGTH = 8
POPULATION_SIZE = 8

chromosome = [random.randint(0, 1) for i in range(0, CHROMOSOME_LENGTH)]


def init(number):
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
            fitness = fitness + 0.1
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

    # print "Sum of Expected Values = ", sum(expected_values)
    T = sum(expected_values)
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
    print "Cross point :", cross_point
    print "Father"
    print father
    print left_side_father
    print right_side_father
    print "Mother"
    print mother
    print left_side_mother
    print right_side_mother
    son_one = left_side_father + right_side_mother
    son_two = left_side_mother + right_side_father

    return son_one, son_two

def mutate(single):
    mutation_point = random.randint(0,CHROMOSOME_LENGTH-1)
    if single[mutation_point] is 1:
        single[mutation_point] = 0
    else:
        single[mutation_point] = 1


def eugenics(population, fitness):
    new_population = []
    for i in range(0,int(POPULATION_SIZE/2)):
        position_one = choose_single(fitness)
        position_two = choose_single(fitness)
        #
        father = population[position_one]
        mother = population[position_two]
        #
        son_one, son_two = one_point_crosses(father,mother)
        #
        mutate(son_one)
        mutate(son_two)
        #
        new_population.append(son_one)
        new_population.append(son_two)
    return new_population

def choose_best(parents, sons):
    pass

if __name__ == '__main__':
    population = init(POPULATION_SIZE)
    fitness = population_fitness(population)
    print_population(population, fitness)
    single_one = choose_single(fitness)
    single_two = choose_single(fitness)
    son_one, son_two = one_point_crosses(population[single_one], population[single_two])
    print_single(son_one,fitness_calculation(son_one))
    print_single(son_two,fitness_calculation(son_two))
