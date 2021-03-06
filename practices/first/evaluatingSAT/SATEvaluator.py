'''
López Garduño Blanca Azucena
Reséndiz Arteaga Juan Alberto
SAT problem
'''  # All the libraries we are going to use
import sys
import thread
import cProfile
from threading import Thread
import time
import numpy as np
from pylab import *

# Start of script
variables = 13
# in case there is an argument for testing purposes
if len(sys.argv) is not 1:
    variables = int(sys.argv[1])
numberposibilites = 2 ** variables
array = np.zeros((numberposibilites, variables + 1))
actual_time = np.zeros(variables)
# Basic array information
print "Array Shape : " + str(array.shape)
print "Size of array : " + str(array.nbytes / 1024) + " Kbytes"
# The method which becomes part of a thread in order to fill the huge array
def fillArray(threadName, startPoint, endPoint):
    for column in range(variables, 0, -1):
        for row in range(startPoint, endPoint):
            if row % (2 ** column) < 2 ** (column - 1):
                array[row, column - 1] = 1


# gets all maxiterms and evaluate'em using threads again
def evaluateAllMaxiterms(numberOfVariables=variables):
    numberposibilitesToEvaluate = 2 ** numberOfVariables
    allTerms = getGlobalExpression(numberOfVariables)
    if numberOfVariables >= 4:
        t1 = Thread(target=evaluateMaxitermsThread,
                    args=("ThreadMaxiterm-1", 0, numberposibilitesToEvaluate / 4, numberOfVariables, allTerms ))
        t2 = Thread(target=evaluateMaxitermsThread, args=(
        "ThreadMaxiterm-2", (numberposibilitesToEvaluate / 4), (numberposibilitesToEvaluate / 4) * 2, numberOfVariables,
        allTerms))
        t3 = Thread(target=evaluateMaxitermsThread, args=(
        "ThreadMaxiterm-3", (numberposibilitesToEvaluate / 4) * 2, (numberposibilitesToEvaluate / 4) * 3,
        numberOfVariables, allTerms))
        t4 = Thread(target=evaluateMaxitermsThread, args=(
        "ThreadMaxiterm-4", (numberposibilitesToEvaluate / 4) * 3, numberposibilitesToEvaluate, numberOfVariables,
        allTerms))
        # Initializacion of each thread
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        #wait for all the threads to finish
        t1.join()
        t2.join()
        t3.join()
        t4.join()

    else:
        evaluateMaxitermsThread("ThreadMaxiterm", 0, numberposibilitesToEvaluate, numberOfVariables, allTerms)


# Get all the expression to be evaluated
def getGlobalExpression(numberOfVariables=-1):
    if numberOfVariables is -1:
        return array[:, :-1]
    else:
        return array[0:(2 ** numberOfVariables), 0:numberOfVariables]


# function to be concurrent in order to evaluate all the expression
def evaluateMaxitermsThread(threadName, startPoint, endPoint, numberOfVariables, allTerms=getGlobalExpression()):
    for row in range(startPoint, endPoint):
        evaluateExpression(array[row, :numberOfVariables], allTerms)


# Defines if its necessary to use threads or not!
def generateHugeArray():
    if variables >= 4:
        # Like Java style!
        t1 = Thread(target=fillArray, args=("Thread-1", 0, numberposibilites / 4 ))
        t2 = Thread(target=fillArray, args=("Thread-2", (numberposibilites / 4), (numberposibilites / 4) * 2 ))
        t3 = Thread(target=fillArray, args=("Thread-3", (numberposibilites / 4) * 2, (numberposibilites / 4) * 3))
        t4 = Thread(target=fillArray, args=("Thread-4", (numberposibilites / 4) * 3, numberposibilites))
        #Initializacion of each thread
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        #wait for all the threads to finish
        t1.join()
        t2.join()
        t3.join()
        t4.join()

    else:
        fillArray("Main", 0, numberposibilites)


# 'cuz expression was toooo big we decided to split all the information in threads (again ...)
def evaluateExpressionThread(threadIdentifier, arrayExpression, allTerms, startPoint, endPoint):
    result = 1
    arrayExpressionLength = len(arrayExpression)
    try:
        for row in range(startPoint, endPoint):
            partial = 1
            for column in range(0, arrayExpressionLength):
                if allTerms[row, column] is 1:
                    partial = partial and 1
                if allTerms[row, column] is 0:
                    partial = partial and not (arrayExpression[column])
            result = partial or result
            array[row, -1] = result
    except Exception, e:
        print sys.exc_traceback.tb_lineno


# evaluating expression
def evaluateExpression(arrayExpression, allTerms):
    allTermsLength = len(allTerms)
    numerOfTerms = len(arrayExpression)
    if numerOfTerms >= 4:
        t1 = Thread(target=evaluateExpressionThread, args=(1, arrayExpression, allTerms, 0, (allTermsLength / 4 )))
        t2 = Thread(target=evaluateExpressionThread,
                    args=(2, arrayExpression, allTerms, (allTermsLength / 4), (allTermsLength / 4) * 2))
        t3 = Thread(target=evaluateExpressionThread,
                    args=(3, arrayExpression, allTerms, (allTermsLength / 4) * 2, (allTermsLength / 4) * 3))
        t4 = Thread(target=evaluateExpressionThread,
                    args=(4, arrayExpression, allTerms, (allTermsLength / 4) * 3, allTermsLength))
        #Initializacion of each thread
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        #wait for all the threads to finish
        t1.join()
        t2.join()
        t3.join()
        t4.join()
    else:
        evaluateExpressionThread(-1, arrayExpression, allTerms, 0, allTermsLength)


# main method, from this point all the program will be executed
def main():
    try:
        generateHugeArray()
        #for variableToEvaluate in range(1, variables+1):
        #    evaluateAllMaxiterms(variableToEvaluate)
        var = arange(0, variables, 1)
        start_time = time.time()
        for i in var:
            evaluateAllMaxiterms(i)
            actual_time[i] = time.time() - start_time
            print ("Variables: %s --- Execution time:  %s seconds ---" % (i, actual_time[i]))
            start_time = time.time()
        plot(var, actual_time)
        ylabel('time (s)')
        xlabel('number or variables')
        title('Time evaluation')
        grid(True)
        savefig("test.png")
        show()
    except Exception, e:
        print e
    else:
        pass
    finally:  #print array
        pass

#in order to get all execution time and all the calls the program did while executing time
#cProfile.run('main()')
main()
