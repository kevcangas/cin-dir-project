#Python
from math import *

#Numpy
import numpy as np

#Own libraries
from classes.grapher import Grapher


#Class Robot
class Robot:

    #Constructor
    def __init__(self, config:list) -> None:
        
        x=[0]
        y=[0]
        z=[0]

        p0=np.transpose(np.array([0,0,0]))

        #[theta, d, a, alpha]
        for slabon in config:
            
            #Parameters of the slabon analyzed
            theta=slabon[0]
            d=slabon[1]
            a=slabon[2]
            alpha=slabon[3]

            #Transformation matrix 
            R=np.array([[cos(theta), -sin(theta)*cos(alpha), sin(theta)*cos(alpha)],
                    [sin(theta), cos(theta)*sin(alpha), -cos(theta)*sin(alpha)],
                    [0, sin(alpha), cos(alpha)]])
            
            dp=np.transpose(np.array([a*cos(theta),a*sin(theta),d]))
            
            #Calculus of the coordenate of the joint
            r=R*p0 + dp

            p0=np.transpose(np.array([r[0][0],r[1][1],r[2][2]]))

            x.append(r[0][0])
            y.append(r[1][1])
            z.append(r[2][2])

        #Saves the points of every joint in a numpy array
        self.x=np.array([x])
        self.y=np.array([y])
        self.z=np.array([z])


    #Shows the robot in a 3dplot  
    def show_robot(self):
        graph_robot = Grapher()
        figure = graph_robot.graph(self.x, self.y, self.z)
        return figure