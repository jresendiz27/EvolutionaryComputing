'''
Created on 09/09/2014
@author: azu
'''
import random
import numpy as np 
import math
from fitness import *

def initialize(number):
    return [np.float(random.gauss(0,100)) for i in range(number)]

def mutate(variables, generation, numberOfVariables):
    return [variables[i] + sigma[generation]*random.gauss(0,1) for i in range(numberOfVariables)]

def success(replacement, generation, numberOfVariables):
    ps = replacement / float(generation)
    if(generation % numberOfVariables == 0):
        if(ps > 1/5.0):
            return sigma[generation - numberOfVariables]/0.817
        if(ps < 1/5.0):
            return sigma[generation - numberOfVariables]*0.817
        if(ps == 1/5.0):
            return sigma[generation - numberOfVariables]
    else:
        return sigma[generation - 1]

def onePlusOne(func):
    print("\nES: 1+1 \tFunction: %s"%(func))
    generation = 0
    replacement = 0
    ps = 0
    num = numberOfVariables[func]
    variables = initialize(num)
    fitnessDad = function[func](variables)
    actualBest = fitnessDad + 1
    comparison = abs(actualBest-fitnessDad)
    while(generation < maxGenerations and comparison > epsilon):
        offspring = mutate(variables, generation, num)
        fitnessSon = function[func](offspring)
        if(fitnessSon < fitnessDad): #Son better than Dad
            actualBest = fitnessDad 
            variables = offspring
            fitnessDad = fitnessSon
            replacement += 1
        generation += 1
        if(generation < maxGenerations):
            sigma[generation] = success(replacement, generation, num)
        comparison = abs(actualBest-fitnessDad)
        print(variables, fitnessDad, offspring, fitnessSon, generation, comparison, num)
    return "Vars: %s Fitness: %s Generations: %d"%(variables, fitnessDad, generation)

#onePlusOne(3)