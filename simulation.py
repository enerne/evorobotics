from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT(2,2)
        self.Run()

    def Run(self):
        for i in range(0, c.numsteps):
            print(i)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)

            time.sleep(c.timestep)


def __del__(self):
    p.disconnect()

