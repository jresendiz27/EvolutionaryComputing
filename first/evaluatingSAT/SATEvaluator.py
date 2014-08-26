# All the libraries we are going to use
import sys
import numpy as np
import thread
import cProfile
import re
# Start of script

variables = 20
# in case there is an argument for testing purposes
if len(sys.argv) is not 1:
    variables = int(sys.argv[1])
numberposibilites = 2 ** variables
array = np.zeros((numberposibilites, variables+1))
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


#gets all maxiterms and evaluate'em using threads again
def evaluateAllMaxiterms(numberOfVariables = variables):
    for row in range(0, 2**numberOfVariables):
        array[row,numberOfVariables] = -1 #that one will be evaluated :P

def getAllMaxiterms():
    
#main method, from this point all the program will be executed
def main():
    try:
        if variables >= 4:
            thread.start_new_thread(fillArray, ("Thread-1", 0, numberposibilites / 4 ))
            thread.start_new_thread(fillArray, ("Thread-2", (numberposibilites / 4), (numberposibilites / 4) * 2 ))
            thread.start_new_thread(fillArray, ("Thread-3", (numberposibilites / 4) * 2, (numberposibilites / 4) * 3 ))
            thread.start_new_thread(fillArray, ("Thread-4", (numberposibilites / 4) * 3, numberposibilites ))
        else:
            fillArray("Main", 0, numberposibilites)
    except Exception, e:
        raise
    else:
        evaluateAllMaxiterms()
        getAllMaxiterms()
    finally:
        print array
        #pass

#in order to get all execution time and all the calls the program did while executing time
#cProfile.run('main()')
main()