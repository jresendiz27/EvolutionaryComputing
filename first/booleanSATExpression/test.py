'''
Created on 25/08/2014
@author: azu
'''
import sys
import thread
import cProfile
import numpy as np

numberOfVariables = 20
'''results = open('superSolutions.txt','w')'''
if len(sys.argv) is not 1:
    numberOfVariables = int(sys.argv[1])

def createExpression():
	#Creates the 'matrix' of maxiterms in a string expression
	expression = ""
	for row in range(0, 2 ** numberOfVariables):
		expression += int2binAnd(row,numberOfVariables)
		if((row+1) < 2 ** numberOfVariables):
			expression += ' or '
	expression = expression.replace('0','not 1')
	return expression

def int2binAnd(n, count):
    #returns the binary of integer n, using count number of digits'''
    return " and ".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def int2bin(n, count):
    #returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def evaluateVariables():
	listExpression = createExpression()
	for variableIterator in range(2 ** numberOfVariables):
		evaluableExpression = listExpression[0]
		combination = int2bin(variableIterator,numberOfVariables)
		for j in range(0,len(listExpression)-1):
			evaluableExpression += str(combination[j%numberOfVariables]) + str(listExpression[j+1])
        	'''
        	if(eval(evaluableExpression) == 1):
        		results = open('superSolutions.txt','a+')
        		results.write("F("+str(int2bin(variableIterator,numberOfVariables))+") = True\n")
        		print("F("+str(int2bin(variableIterator,numberOfVariables))+") = True")
			'''
def evaluateMaxiterms():
	expression = createExpression()
	if (eval(expression) ==1):
		print ("function is true")

def main():
	evaluateMaxiterms()

cProfile.run('main()')
