'''
Created on 09/09/2014
@author: azu
'''
import random
import numpy as np 
import math
from fitness import *

def initialize(number):
    return [[np.float(random.gauss(0,100)) for i in range(number)] for u in range(1)]

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

def select(fitnessArray, mode):
    f = fitnessArray[:]
    f.sort()
    middleValue = f.pop(len(f)/2)
    selected = {'best': fitnessArray.index(min(fitnessArray)),
        'worst': fitnessArray.index(max(fitnessArray))}
    return selected[mode]

def onePlusOne(func):
    print("\nES: u+1 \tFunction: %s"%(func))
    generation = 0
    replacement = 0
    ps = 0
    num = numberOfVariables[func]
    comparison = 1
    variables = initialize(num)
    fitnessArray = [function[func](variables[u]) for u in range(1)]
    best = select(fitnessArray, 'best')
    while(generation < maxGenerations and sigma[generation] > epsilon and min(fitnessArray) > float('-inf')):
        actualBest = min(fitnessArray)
        selectedIndex = select(fitnessArray, 'best')
        offspring = mutate(variables[selectedIndex], generation, num)
        fitnessSon = function[func](offspring)
        worst = select(fitnessArray, 'worst')
        if(fitnessSon < fitnessArray[worst]): #Son better than worst dad
            variables[worst] = offspring
            fitnessArray[worst] = fitnessSon
            replacement += 1
        if(actualBest > min(fitnessArray)):
            comparison = abs(actualBest - min(fitnessArray))
        generation += 1
        if(generation < maxGenerations):
            sigma[generation] = success(replacement, generation, num)
        best = select(fitnessArray, 'best')
    print(variables[best], fitnessArray[best], generation, sigma[generation], comparison)
    if(num > 1):
        print(imageMaker(number_of_variables=num, function_id = func, name=str(func)+"_onePlusOne", point=([variables[best][0]],[variables[best][1]], [fitnessArray[best]])))
    else:
        print(imageMaker(number_of_variables=num, function_id = func,name=str(func)+"_onePlusOne", point=(variables[best], [fitnessArray[best]])))
    return "Vars: %s Fitness: %s Generations: %d"%(variables[best], fitnessArray[best], generation)

#onePlusOne(0)