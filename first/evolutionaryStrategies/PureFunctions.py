__author__ = 'alberto'

import numpy

def fitness0(x):
	return ((1-x)**4 - (2*x+10)**2)

def fitness1(x):
    return -0.75/(1+x**2)-(0.65*x*numpy.atan(1/x))+0.65

def fitness2(x):
	return (-4* x**2 - 20*x - 100) + (1 - x)**4

def fitness3(x):
	return 3*x**2+ 12/(x**3) - 5

def fitness4(x):
	return 3*x**4 + x**2 - 2*x + 1

def fitness5(x):
	return 10+x**3-2*x-5*(numpy.finfo(float).eps)**x

def fitness6(x):
	return x**2- 10*(numpy.finfo(float).eps)**(0.1*x)

def fitness7(x):
	return (10*x**3+3*x**2+5)**2

def fitness8(x):
	return 0.5/numpy.sqrt(1+(x**2)) - numpy.sqrt(1+(x**2))*(1-(0.5/(1+(x**2)))) + x

def fitness9(x):
	return (numpy.finfo(float).eps)**x-x**3

def fitness10(x):
	return (x**2-1)**3-(2*x-5)**4

def fitness11(x):
	return (-4*x**2-20*x-100) + (1-x)**4

def fitness12(x,y):
	return (x**2+(y+1)**2)*(x**2+(y-1)**2)

def fitness13(x,y):
	return (x**2-y)**2+y**2

def fitness14(x,y):
	return 50*(y-x**2)**2+(2-x)**2

def fitness15(x,y):
	return (x+2*y-7)**2+(2*x+y-5)**2

def fitness16(x,y):
	return (1.5-x*(1-y))**2+(2.25-x*(1-y**2))**2+(2.625-x*(1-y**3))**2

function = {0: fitness0, 1: fitness1, 2: fitness2, 3: fitness3, 4: fitness4, 5: fitness5, 6:fitness6, 7: fitness7,
	8: fitness8, 9: fitness9, 10: fitness10, 11: fitness11, 12: fitness12, 13: fitness13, 14: fitness14,
	15: fitness15, 16: fitness16}