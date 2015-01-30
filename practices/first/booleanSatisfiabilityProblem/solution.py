__author__ = 'alberto'
import sys
import numpy as np
from string import Template

print sys.argv


def getDicionary(elements):
    dictionary = {}
    for index in range(0, len(elements)):
        dictionary["x" + str(index)] = elements[index]
    return dictionary


def generatetruthtable(nvariables, template):
    truthtable = np.zeros((2 ** nvariables, nvariables + 2), dtype='S1000')
    numberposibilites = 2 ** nvariables
    for column in range(nvariables, 0, -1):
        for row in range(0, numberposibilites):
            if row % (2 ** column) < 2 ** (column - 1):
                truthtable[row, column - 1] = "True"
            else:
                truthtable[row, column - 1] = "False"
    # evaluating the template
    for row in range(0, numberposibilites):
        # true/false
        dictionary = getDicionary(truthtable[row, 0: nvariables])
        expression = Template(template).substitute(dictionary)
        truthtable[row, nvariables] = expression
        truthtable[row, nvariables + 1] = eval(expression)
        # truthtable[row, nvariables] = expession
    return truthtable


def readfile(pathtofile):
    file = open(pathtofile, 'r').read()
    formatFlag = True
    initialLength = 0
    counter = 0
    strings = []
    maxiterms = []
    indexVariable = 0
    # checking if file format is right
    with open(pathtofile, 'r') as file:
        for line in file:
            # getting the strings to be evaluated
            expression = line.split(" ")
            for term in expression:
                if int(term) is 1:
                    strings.append("$x" + str(indexVariable))
                if int(term) is 0:
                    strings.append(" not($x" + str(indexVariable) + ") ")
                indexVariable += 1
            maxiterms.append("(" + " and ".join(strings) + ")")
            indexVariable = 0
            strings = []

            if counter is 0:
                initialLength = len(expression)
                counter += 1
                continue
            if not (len(expression) is initialLength):
                formatFlag = False
            counter += 1
    if not (formatFlag):
        return None, 0, False, "Wrong format!", None
    return file, initialLength, True, "File is ok!", " or ".join(maxiterms)


def satsolution(pathtofile):
    file, nvariables, status, message, template = readfile(pathtofile)
    print "Expression to be evaluated : \n"
    print template
    print "-" * 60 + "\n"
    if status:
        truthtable = generatetruthtable(nvariables, template)
        for row in range(0, len(truthtable)):
            print truthtable[row]
            print "-" * 60 + "\n"
    else:
        print message


satsolution("./content.txt")