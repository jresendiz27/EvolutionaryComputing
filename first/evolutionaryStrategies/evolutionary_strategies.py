'''
Created on 09/09/2014

@author: azu
'''
import random
import numpy as np 
import math

numberOfVariables = 1
maxGenerations = 10000
epsilon = 0.001
sigma = [np.float(0) for i in range(0,maxGenerations+1)]
sigma[0] = 10

def start(number):
    return [np.float(0) for i in range(number)]

def mutate(variables, generation):
    return [variables[i] + sigma[generation]*random.gauss(0,1) for i in range(numberOfVariables)]

def fitness(x):
    return ((1-x[0])**4 - (2*x[0]+10)**2)

def success(replacement, generation):
    ps = replacement / generation
    if(generation % numberOfVariables == 0):
        if(ps > 1/5):
            return sigma[generation - numberOfVariables]/0.817
        if(ps < 1/5):
            return sigma[generation - numberOfVariables]*0.817
        if(ps == 1/5):
            return sigma[generation - numberOfVariables]
    else:
        return sigma[generation - 1]

def evolutionaryStrategies():
    generation = 0
    replacement = 0
    ps = 0
    variables = start(numberOfVariables)
    fitnessDad = fitness(variables)
    last = fitnessDad + 1
    comparison = abs(last-fitnessDad)
    while(generation < maxGenerations and comparison > epsilon):
        offspring = mutate(variables, generation)
        fitnessSon = fitness(offspring)
        if(fitnessSon < fitnessDad): #Son better than Dad
            last = fitnessDad 
            variables = offspring
            fitnessDad = fitnessSon
            replacement += 1
        generation += 1
        if(generation < maxGenerations):
            sigma[generation] = success(replacement, generation)
        comparison = abs(last-fitnessDad)
        print(variables, fitnessDad, offspring, fitnessSon, generation, comparison )        

evolutionaryStrategies()