'''
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
    return [[variables[i] + sigma[generation]*random.gauss(0,1) for i in range(numberOfVariables)] for l in range(lamb)]

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
    secondBestValue = f.pop(1)
    selected = {
        'best': fitnessArray.index(min(fitnessArray)), 
        '2nd': fitnessArray.index(secondBestValue),
        'middle': fitnessArray.index(middleValue),
        'worst': fitnessArray.index(max(fitnessArray))}
    return selected[mode]

def muPlusLambda(func):
    print("\nES: u+1 \tFunction: %s"%(func))
    generation = 0
    replacement = 0
    ps = 0
    num = numberOfVariables[func]
    comparison = 1
    variables = initialize(num)
    fitnessArray = [function[func](variables[u]) for u in range(mu)]
    best = select(fitnessArray, 'best')
    print(variables[best], fitnessArray[best], sigma[generation], generation, sigma[generation], comparison)
    while(generation < maxGenerations and sigma[generation] > epsilon and min(fitnessArray) > float('-inf')):
        actualBest = min(fitnessArray)
        best = select(fitnessArray, 'best')

        offspring = mutate(variables[best], generation, num)
        fitnessSon = [function[func](offspring[l]) for l in range(lamb)]
        for i in range(lamb):
            variables.append(offspring[i])
            fitnessArray.append(fitnessSon[i])
        f = fitnessArray[:]
        f.sort()
        del f[mu:]
        indexes = [fitnessArray.index(fi) for fi in f]
        v = []
        for index in indexes:
            v.append(variables[index])
        variables = v
        fitnessArray = f
        if(actualBest > min(fitnessArray)):
            replacement += 1
            comparison = abs(actualBest - min(fitnessArray))
        generation += 1
        if(generation < maxGenerations):
            sigma[generation] = success(replacement, generation, num)
        
    print(variables[best], fitnessArray[best], sigma[generation], generation, sigma[generation], comparison)

    if(num > 1):
        print(imageMaker(number_of_variables=num, name=str(func)+"_muPlusLamdba", point=([variables[best][0]],[variables[best][1]], [fitnessArray[best]]), func=function[func]))
    else:
        print(imageMaker(number_of_variables=num, name=str(func)+"_muPlusLamdba", point=(variables[best], [fitnessArray[best]]), func=function[func]))
    return "Vars: %s Fitness: %s Generations: %d"%(variables[best], fitnessArray[best], generation)

#muPlusLambda(0)