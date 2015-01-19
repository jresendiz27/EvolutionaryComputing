'''
mu, lambda
Created on 09/09/2014
@author: azu
'''
import random
import numpy as np 
import math
from fitness import *

def initialize(number):
    return [[np.float(random.gauss(0,100)) for i in range(number)] for u in range(mu)]

def mutate(variables, generation, numberOfVariables):
    return [[variables[i] + sigma[generation]*random.gauss(0,1) for i in range(numberOfVariables)] for u in range(mu)]

def success(replacement, generation, numberOfVariables):
    ps = replacement / float(generation)
    if(generation % numberOfVariables == 0):
        if(ps > 1/5.0):
            return sigma[generation - numberOfVariables]*0.817
        if(ps < 1/5.0):
            return sigma[generation - numberOfVariables]/0.817
        if(ps == 1/5.0):
            return sigma[generation - numberOfVariables]
    else:
        return sigma[generation - 1]

def select(fitnessArray, mode):
    f = fitnessArray[:]
    f.sort()
    middleValue = f.pop(len(f)/2)
    secondBestValue = f.pop(1)
    selected = {
        'best': fitnessArray.index(min(fitnessArray)), 
        '2nd': fitnessArray.index(secondBestValue),
        'middle': fitnessArray.index(middleValue),
        'worst': fitnessArray.index(max(fitnessArray))}
    return selected[mode]

def muCommaLambda(func):
    print("\nES: u+1 \tFunction: %s"%(func))
    generation = 0
    replacement = 0
    ps = 0
    num = numberOfVariables[func]
    comparison = 1
    variables = initialize(num)
    fitnessArray = [function[func](variables[u]) for u in range(mu)]
    best = select(fitnessArray, 'best')
    while(generation < maxGenerations and sigma[generation] > epsilon and min(fitnessArray) > float('-inf')):
        best = select(fitnessArray, 'best')
        actualBest = fitnessArray[best]
        offspring = mutate(variables[best], generation, num)
        fitnessSon = [function[func](offspring[u]) for u in range(mu)]
        variables = offspring[:]
        fitnessArray = fitnessSon
        if(actualBest > min(fitnessArray)):
            replacement += 1
            comparison = abs(actualBest - min(fitnessArray))
        generation += 1
        if(generation < maxGenerations):
            sigma[generation] = success(replacement, generation, num)
    print(variables[best], fitnessArray[best], sigma[generation], generation, sigma[generation], comparison)
    #
    if(num > 1):
        print(imageMaker(number_of_variables=num,function_id = func, name=str(func)+"_muCommaLamda", point=([variables[best][0]],[variables[best][1]], [fitnessArray[best]])))
    else:
        print(imageMaker(number_of_variables=num,function_id = func, name=str(func)+"_muCommaLamda", point=(variables[best], [fitnessArray[best]])))
    return "Vars: %s Fitness: %s Generations: %d"%(variables[best], fitnessArray[best], generation)

#muCommaLambda(0)