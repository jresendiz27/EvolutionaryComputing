# All the libraries we are going to use
import sys
import thread

import cProfile

import numpy as np


# Start of script
variables = 3
# in case there is an argument for testing purposes
if len(sys.argv) is not 1:
    variables = int(sys.argv[1])
numberposibilites = 2 ** variables
array = np.zeros((numberposibilites, variables + 1))
print "Array Shape : " + str(array.shape)
print "Size of array : " + str(array.nbytes / 1024) + " Kbytes"
# The method which becomes part of a thread in order to fill the huge array
def fillArray(threadName, startPoint, endPoint):
    for column in range(variables, 0, -1):
        for row in range(startPoint, endPoint):
            if row % (2 ** column) < 2 ** (column - 1):
                array[row, column - 1] = 1
            else:
                array[row, column - 1] = 0


# gets all maxiterms and evaluate'em using threads again
def evaluateAllMaxiterms(numberOfVariables=variables):
    numberposibilitesToEvaluate = 2 ** numberOfVariables
    allTerms = getGlobalExpression(numberOfVariables)
    if numberOfVariables >= 4:
        thread.start_new_thread(evaluateMaxitermsThread,
                                ("ThreadMaxiterm-1", 0, numberposibilitesToEvaluate / 4, allTerms ))
        thread.start_new_thread(evaluateMaxitermsThread,
                                ("ThreadMaxiterm-2", (numberposibilitesToEvaluate / 4),
                                 (numberposibilitesToEvaluate / 4) * 2, allTerms))
        thread.start_new_thread(evaluateMaxitermsThread,
                                ("ThreadMaxiterm-3", (numberposibilitesToEvaluate / 4) * 2,
                                 (numberposibilitesToEvaluate / 4) * 3, allTerms))
        thread.start_new_thread(evaluateMaxitermsThread,
                                ("ThreadMaxiterm-4", (numberposibilitesToEvaluate / 4) * 3,
                                 numberposibilitesToEvaluate, allTerms))
    else:
        evaluateMaxitermsThread("ThreadMaxiterm", 0, numberposibilitesToEvaluate)


# Get all the expression to be evaluated
def getGlobalExpression(numberOfVariables = -1):
    if numberOfVariables is -1:
        return array[:, :-1]
    else:
        return array[0:(2**numberOfVariables), 0:numberOfVariables]


# function to be concurrent in order to evaluate all the expression
def evaluateMaxitermsThread(threadName, startPoint, endPoint, allTerms=getGlobalExpression()):
    for row in range(startPoint, endPoint):
        array[row, -1] = evaluateExpression(array[row, :-1], allTerms)


# Defines if its necessary to use threads or not!
def generateHugeArray():
    if variables >= 4:
        thread.start_new_thread(fillArray, ("Thread-1", 0, numberposibilites / 4 ))
        thread.start_new_thread(fillArray, ("Thread-2", (numberposibilites / 4), (numberposibilites / 4) * 2 ))
        thread.start_new_thread(fillArray, ("Thread-3", (numberposibilites / 4) * 2, (numberposibilites / 4) * 3 ))
        thread.start_new_thread(fillArray, ("Thread-4", (numberposibilites / 4) * 3, numberposibilites ))
    else:
        fillArray("Main", 0, numberposibilites)


# evaluating expression
def evaluateExpression(arrayExpression, allTerms):
    result = 0
    try:
        for row in range(0, len(allTerms)):
            partial = 1
            for column in range(0, len(arrayExpression)-1):
                if allTerms[row, column] is 1:
                    partial = partial and 1
                if allTerms[row, column] is 0:
                    partial = partial and not (arrayExpression[column])
            result = partial or result
        return result
    except Exception, e:
        print arrayExpression
        print allTerms
        print "-"*60+"\n"
        print e
        exit()


# main method, from this point all the program will be executed
def main():
    try:
        generateHugeArray()
        for variableToEvaluate in range(1,variables+1):
            evaluateAllMaxiterms(variableToEvaluate)
    except Exception, e:
        print e
    else:
        pass
    finally:
        pass

#in order to get all execution time and all the calls the program did while executing time
#cProfile.run('main()')
main()