'''
Created on 09/09/2014

@author: azu
'''
import numpy as np;
import random

numberOfVariables = 1
maxGenerations = 100
sigma = np.zeros(maxGenerations)
sigma[0] = 10
generations = 0

#
def initializeVariables():
    return [random.uniform(0,1) for i in range(numberOfVariables)]
    
def mutateVariables(variables):
    return [variables[i-1] + sigma[generations] * random.uniform(0,1) for i in range(numberOfVariables)]

def evaluateVariables(x):
    return ((1-x[0])**4 - (2*x[0]+10)**2)

def evolutionaryStrategies():
    generations = 0
    replacement = 0
    ps = 0
    variables = initializeVariables() #Inicliaza las variables
    print(variables)
    while(generations < maxGenerations): #numero de generaciones que se repite el proceso
        variableEvaluation = evaluateVariables(variables) #Evalua las variables
        offspring = mutateVariables(variables) #Mutacion de las variables
        generations += 1
        if(evaluateVariables(offspring) < variableEvaluation): #Compara si la nueva variable es mejor
            replacement += 1 
            ps = replacement / generations
            variables = offspring #reemplaza las variables con los 'hijos'
            if(generations % numberOfVariables == 0): #Condiciones para que sigma cambie
                if(ps > 1/5):
                    sigma[generations] = sigma[generations - numberOfVariables]/0.817
                if(ps < 1/5):
                    sigma[generations] = sigma[generations - numberOfVariables]*0.817
                if(ps == 1/5):
                    sigma[generations] = sigma[generations - numberOfVariables]
            else:
                sigma[generations] = sigma[generations - 1]
        print(variables, replacement, generations)

evolutionaryStrategies()