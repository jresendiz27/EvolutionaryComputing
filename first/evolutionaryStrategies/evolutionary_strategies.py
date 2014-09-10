'''
Created on 09/09/2014

@author: azu
'''
import numpy as np;
import random

numberOfVariables = 1 #configurable
maxGenerations = 1000 #configurable
epsilon = 0.000001 #configurable
sigma = np.zeros(maxGenerations) 
sigma[0] = 1 #configurable

generations = 0

#Creates a random array with values between 0 and 1
def initializeVariables():
    return [np.long(random.uniform(0,1)) for i in range(numberOfVariables)]

#Creates new values using the sigma value and a random number between 0 and 1
def mutateVariables(variables):
    return [variables[i] + sigma[generations] * random.uniform(0,1) for i in range(numberOfVariables)]

#Function/problem to be solved (minimized)
def evaluateVariables(x):
    return ((1-x[0])**4 - (2*x[0]+10)**2)

def evolutionaryStrategies():
    generations = 0
    replacement = 0
    ps = 0
    epsilon = 0
    variables = initializeVariables() #Initialize random values for the variables
    print(variables)
    while True:
        last = variables
        variableEvaluation = evaluateVariables(variables) #Evaluating variables
        offspring = mutateVariables(variables) #Mutation of the variables
        generations += 1
        if(evaluateVariables(offspring) < variableEvaluation): #If the offspring is better than the original population
            replacement += 1 
            ps = replacement / generations
            variables = offspring #Replaces with the better solution
            if(generations % numberOfVariables == 0): #Conditions to change sigma value
                if(ps > 1/5):
                    sigma[generations] = sigma[generations - numberOfVariables]/0.817
                if(ps < 1/5):
                    sigma[generations] = sigma[generations - numberOfVariables]*0.817
                if(ps == 1/5):
                    sigma[generations] = sigma[generations - numberOfVariables]
            else:
                sigma[generations] = sigma[generations - 1]
        print(variables, replacement, generations)
        #Stop condition. If maximum number of generation has been reached or the variables changed less than an epsilon value
        if(generations >= maxGenerations or min(np.subtract(variables,last)) <= epsilon): 
            break;

evolutionaryStrategies()