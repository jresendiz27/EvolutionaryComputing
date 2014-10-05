'''
Fitnesses
@author: azu
'''
import math
import numpy as np
import random

a = [[-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32,-32,-16,0,16,32], [-32,-32,-32,-32,-32,-16,-16,-16,-16,-16,0,0,0,0,0,16,16,16,16,16,32,32,32,32,32]]

def fitness0(x):
	return ((1-x[0])**4 - (2*x[0]+10)**2)

def fitness1(x):
    return -0.75/(1+x[0]**2)-(0.65*x[0]*math.atan(1/x[0]))+0.65

def fitness2(x):
	return (-4* x[0]**2 - 20*x[0] - 100) + (1 - x[0])**4

def fitness3(x):
	return 3*x[0]**2+ 12/(x[0]**3) - 5

def fitness4(x):
	return 3*x[0]**4 + x[0]**2 - 2*x[0] + 1

def fitness5(x):
	return 10+x[0]**3-2*x[0]-5*(np.finfo(float).eps)**x[0]

def fitness6(x):
	return x[0]**2- 10*(np.finfo(float).eps)**(0.1*x[0])

def fitness7(x):
	return (10*x[0]**3+3*x[0]**2+5)**2

def fitness8(x):
	return 0.5/(math.sqrt(1+x[0]**2)- math.sqrt(1+x[0]**2)*(1-0.5/(1+x[0]**2)))+x[0]

def fitness9(x):
	return (np.finfo(float).eps)**x[0]-x[0]**3

def fitness10(x):
	return (x[0]**2-1)**3-(2*x[0]-5)**4

def fitness11(x):
	return (-4*x[0]**2-20*x[0]-100) + (1-x[0])**4

def fitness12(x):
	return (x[0]**2+(x[1]+1)**2)*(x[0]**2+(x[1]-1)**2)

def fitness13(x):
	return (x[0]**2-x[1])**2+x[1]**2

def fitness14(x):
	return 50*(x[1]-x[0]**2)**2+(2-x[0])**2

def fitness15(x):
	return (x[0]+2*x[1]-7)**2+(2*x[0]+x[1]-5)**2

def fitness16(x):
	return (1.5-x[0]*(1-x[1]))**2+(2.25-x[0]*(1-x[1]**2))**2+(2.625-x[0]*(1-x[1]**3))**2

def	fitness17(x):
	return (10*(x[1]-x[0]**2))**2+(1-x[0])**2+90*(x[3]-x[2]**2)**2+(1-x[2])**2+10*(x[1]+x[3]-2)**2+0.1*(x[1]-x[3])

def fitness18(x):
	return (4-2.1*x[0]**2+(x[0]**4)/3)*x[0]**2+x[0]*x[1]+(-4+4*x[1]**2)*x[1]**2

def fitness19(x):
	return (x[0]+10*x[1])**2+5*(x[2]-x[3])**2+(x[1]-2*x[2])**4+10*(x[0]-x[3])**4

def fitness20(x):
	return x[0]**2+x[1]**2+x[2]**2

def fitness21(x):
	return 100*(x[0]**2-x[1])**2+(1-x[0])**2

def fitness22(x):
	return math.floor(x[0])+math.floor(x[1])+math.floor(x[2])+math.floor(x[3])+math.floor(x[4])

def fitness23(x):
	suma = 0
	for i in range(1,30):
		suma+= (i*x[i-1]**4)
	return suma + random.gauss(0,1)

def fitness24(x):
	superSuma = 0
	for j in range(1,25):
		superSuma += 1/f2(j,x)
	return 1/(1/500 + superSuma)

def f2(j,x):
	suma = 0
	i = 0
	suma+= (x[0]- a[i][j])**6
	i = 1
	suma+= (x[1]- a[i][j])**6
	return j + suma	

def fitness25(x):
	return 0

def fitness26(x):
	return 0

numberOfVariables = {0: 1, 1: 1, 2: 1, 3: 1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:2, 13:2, 14:2, 15:2, 16:2, 
	17:4, 18:2, 19:4, 20:3, 21:2, 22:5, 23:30, 24:2, 25:1, 26:1 }
function = {0: fitness0, 1: fitness1, 2: fitness2, 3: fitness3, 4: fitness4, 5: fitness5, 6:fitness6, 7: fitness7, 
	8: fitness8, 9: fitness9, 10: fitness10, 11: fitness11, 12: fitness12, 13: fitness13, 14: fitness14,
	15: fitness15, 16: fitness16, 17: fitness17, 18: fitness18, 19: fitness19, 20: fitness20, 21: fitness21,
	22: fitness22, 23: fitness23, 24: fitness24, 25: fitness25, 26: fitness26}

maxGenerations = 1000
sigma = [np.float(0) for i in range(0,maxGenerations+1)]
sigma[0] = 10
epsilon = 0.00001
mu = 10
lamb = 10