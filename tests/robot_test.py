from math import pi

from classes.robot import Robot

def run():
    config=[[0,1,0,0],
            [0,0,1,0],
            [0,1,0,0]]
    
    robot_1 = Robot(config)
    robot_1.show_robot()


if __name__ == '__main__':
    run()