#Libraries

#Matplot
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

#Numpy
import numpy.typing as npt

#Class Grapher
class Grapher:

    def __init__(self) -> None:
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(111, projection='3d')
    
    def graph(self, x:npt.ArrayLike, y:npt.ArrayLike, z:npt.ArrayLike, lim:list=[(-5,5),(-5,5),(-1,9)]):
        self.ax1.plot_wireframe(x, y, z)
        self.ax1.set_zlim(lim[2])
        plt.xlim(lim[0])
        plt.ylim(lim[1])
        plt.show()
        return self.ax1