__author__ = 'alberto'
# Para poder mostrar en pantalla el proceso
debug = False
#
from pylab import *
from mpl_toolkits.mplot3d import axes3d
#
RAW_VALUES = True
IMAGE_PATH='./latex/images/'
# Image maker function, recevives a key, value arg and creates an image, it returns the image name
def imageMaker(**kwargs):
    fig, false = None, None
    # test space, changing it inside each option
    x = None
    y = None
    z = None
    #Solution
    x_coordinate = kwargs['point'][0][0]
    y_coordinate = kwargs['point'][1][0]
    try:
        z_coordinate = kwargs['point'][2][0]
    except Exception as e:
        z_coordinate = None
    #Check data types
    if x_coordinate == float('inf') or x_coordinate == float('-inf'):
        return False,None
    if y_coordinate == float('inf') or y_coordinate == float('-inf'):
        return False,None
    if z_coordinate == float('inf') or z_coordinate == float('-inf'):
        return False,None
    #check which type of plot we will use
    if kwargs['number_of_variables'] < 2:
        fig, axes = plt.subplots()
        #generating a valid range for the solution
        # using the solution as the "origin" of the plot
        x = linspace(x_coordinate - 1000, x_coordinate + 1000, 100)
        y = [kwargs['func']([x[index]]) for index in range(0, len(x))]
        #plotting the function
        axes.plot(x, y, 'r')
        axes.set_xlabel('X')
        axes.set_ylabel('Y')
        #plotting the answer
        axes.scatter(kwargs['point'][0], kwargs['point'][1], marker="o")

    if kwargs['number_of_variables'] is 2:
        fig = plt.figure(figsize=(8, 6))
        axes = fig.add_subplot(1, 1, 1, projection='3d')
        #p = axes.plot_wireframe(x, y, z, rstride=4, cstride=4)
        x_linspace = linspace(x_coordinate - 1000, x_coordinate + 1000, 100)
        y_linspace = linspace(y_coordinate - 1000, y_coordinate + 1000, 100)
        x,y = np.meshgrid(x_linspace,y_linspace)
        z = [kwargs['func']([x_linspace[index], y_linspace[index]]) for index in range(0, len(x_linspace))]
        #plotting the surface
        axes.plot_wireframe(x, y, z,rstride=4, cstride=4)
        axes.set_xlabel('X')
        axes.set_ylabel('Y')
        axes.set_zlabel('Z')
        #plotting the answer
        axes.scatter(kwargs['point'][0], kwargs['point'][1], kwargs['point'][2], marker="o")
    #Trying to save the image
    try:
        #Setting the title of each image
        fig.suptitle('Excersice ' + str(kwargs['name']))
        #Saving the image
        plt.savefig(IMAGE_PATH + str(kwargs['name']) + '.png')
        return True, str(kwargs['name']) + '.png'
    except Exception as e:
        print e
        return False, None


#print ( imageMaker(numberOfVariables=3, name=2, point=([1.670688642854871],[104.04328898820108], [21076.99139832839]), function=13))