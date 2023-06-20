#Libraries
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy.typing as npt
import numpy as np


#Class Grapher
class Grapher:

    def __init__(self) -> None:
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(111, projection='3d')
    
    def graph(self, x:npt.ArrayLike, y:npt.ArrayLike, z:npt.ArrayLike):
        self.ax1.plot_wireframe(x, y, z)
        plt.show()