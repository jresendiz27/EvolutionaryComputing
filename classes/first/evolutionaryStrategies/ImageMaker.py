__author__ = 'alberto'
# Para poder mostrar en pantalla el proceso
debug = False
#
from pylab import *
from sympy import solve
from sympy.abc import x

from classes.first.evolutionaryStrategies.PureFunctions import function as function_database

# Constant values
RAW_VALUES = True
IMAGE_PATH = './latex/images/'
X_MIN = -127
X_MAX = 127
X_STEP = 0.1
# Image maker function, recevives a key, value arg and creates an image, it returns the image name
def imageMaker(**kwargs):
    # Solution
    x_coordinate = kwargs['point'][0][0]
    y_coordinate = kwargs['point'][1][0]
    try:
        z_coordinate = kwargs['point'][2][0]
    except Exception as e:
        z_coordinate = None
    # Check data types
    if x_coordinate == float('inf') or x_coordinate == float('-inf'):
        return False, None
    if y_coordinate == float('inf') or y_coordinate == float('-inf'):
        return False, None
    if z_coordinate == float('inf') or z_coordinate == float('-inf'):
        return False, None
    # check which type of plot we will use
    if kwargs['number_of_variables'] < 2:
        #Looking for discontinuities in the function given
        discontinuities = sort(solve(function_database[kwargs['function_id']] ,x))
        # pieces from xmin to last discontinuity
        last_b = X_MIN
        for b in discontinuities:
            # check that this discontinuity is inside our range, also make sure it's real
            if b<last_b or b>X_MAX or not(str(b).isdigit):
              continue
            #Generaton a valid range
            xi = np.arange(last_b, b, X_STEP)
            #Removing the last element from the range, is the one we don't desire on the function
            plot(xi[:-1], 1./(xi[:-1]-2),'r-')
            last_b = float(str(b))
        # from last discontinuity to xmax
        xi = np.arange(last_b, X_MAX, X_STEP)
        #plotting the function, removing the first one, it's the one we don't want!
        plot(xi[1:], 1./(xi[1:]-2),'r-')
        points = [kwargs['point'][0], kwargs['point'][1]]
        #plotting the answer
        plt.plot(*zip(points), marker="o")

    if kwargs['number_of_variables'] is 2:
        fig = figure()
        ax = fig.gca(projection='3d')
        X = np.arange(-2, 2, 0.25)
        Y = np.arange(-2, 2, 0.25)
        X, Y = np.meshgrid(X, Y)
        Z = function_database[kwargs['function_id']](X,Y)
        surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                linewidth=0, antialiased=False)
        ax.zaxis.set_major_locator(LinearLocator(10))
    # Trying to save the image
    try:
        #Setting the title of each image
        fig.suptitle('Excersice ' + str(kwargs['name']))
        #Saving the image
        plt.savefig(IMAGE_PATH + str(kwargs['name']) + '.png')
        return True, str(kwargs['name']) + '.png'
    except Exception as e:
        print e
        return False, None