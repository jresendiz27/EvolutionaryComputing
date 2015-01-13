__author__ = 'alberto'
# Para poder mostrar en pantalla el proceso
debug = False
#
from pylab import *
from mpl_toolkits.mplot3d import axes3d
#
RAW_VALUES = True
IMAGE_PATH = './latex/images/'
NUMBER_OF_SAMPLES = 170
X_RANGE = 27
Y_RANGE = 500
# Image maker function, recevives a key, value arg and creates an image, it returns the image name
def imageMaker(**kwargs):
    fig, axes = None, None
    # test space, changing it inside each option
    x = None
    y = None
    z = None
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
        # fig, axes = plt.subplots()
        #generating a valid range for the solution
        # using the solution as the "origin" of the plot
        x = np.arange(x_coordinate - X_RANGE, x_coordinate + X_RANGE, 0.5)
        y = np.asarray([kwargs['func']([x[index]]) for index in range(0, len(x))])
        #plotting the function
        mask = np.abs(y) > 500
        y[mask] = np.nan
        points = [kwargs['point'][0], kwargs['point'][1]]
        plt.plot(x, y)
        plt.plot(*zip(points), marker="o")
        plt.xlim(x_coordinate - X_RANGE, x_coordinate + X_RANGE)
        plt.ylim(y_coordinate - Y_RANGE, y_coordinate + Y_RANGE)
        #plotting the answer
    """
    if kwargs['number_of_variables'] is 2:
        fig = plt.figure()
        axes = fig.add_subplot(1, 1, 1, projection='3d')
        #p = axes.plot_wireframe(x, y, z, rstride=4, cstride=4)
        x_linspace = linspace(x_coordinate - X_RANGE, x_coordinate + X_RANGE, NUMBER_OF_SAMPLES)
        y_linspace = linspace(y_coordinate - X_RANGE, y_coordinate + X_RANGE, NUMBER_OF_SAMPLES)
        x, y = np.meshgrid(x_linspace, y_linspace)
        z = [kwargs['func']([x_linspace[index], y_linspace[index]]) for index in range(0, len(x_linspace))]
        #plotting the surface
        axes.plot_wireframe(x, y, z, rstride=4, cstride=4)
        axes.set_xlabel('X')
        axes.set_ylabel('Y')
        axes.set_zlabel('Z')
        #plotting the answer
        #axes.scatter(kwargs['point'][0], kwargs['point'][1], kwargs['point'][2], marker="o")
        """
    # Trying to save the image
    try:
        #Setting the title of each image
        #fig.suptitle('Excersice ' + str(kwargs['name']))
        #Saving the image
        plt.savefig(IMAGE_PATH + str(kwargs['name']) + '.png')
        return True, str(kwargs['name']) + '.png'
    except Exception as e:
        print e
        return False, None