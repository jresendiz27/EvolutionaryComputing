import sys
import numpy as np
import thread
import time

variables = 4

if len(sys.argv) is not 1:
    variables = int(sys.argv[1])
numberposibilites = 2 ** variables
array = np.ones((numberposibilites, variables + 2))
print "Array Shape : " + str(array.shape)
print "Size of array : " + str(array.nbytes / 1024) + " Kbytes"
# threads
def fillArray(threadName, startPoint, endPoint):
    print "From thread [ " + threadName + " ]\n"
    for column in range(variables, 0, -1):
        for row in range(0, numberposibilites):
            if row % (2 ** column) < 2 ** (column - 1):
                array[row, column - 1] = 1
            else:
                array[row, column - 1] = 0


try:
    fillArray("Main", 0, numberposibilites)
except Exception, e:
    raise
else:
    pass
finally:
    pass