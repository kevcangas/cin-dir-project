import numpy as np

from classes.grapher import Grapher

def run():
    x = np.array([[1,2,3,4,5,6,7,8,9,10]])
    y = np.array([[5,6,7,8,2,5,6,3,7,2]])
    z = np.array([[1,2,6,3,2,7,3,3,7,2]])

    graph = Grapher()
    graph.graph(x, y, z)


if __name__ == '__main__':
    run()