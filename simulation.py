from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import time


class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT(2,2, solutionID)
        self.Run()

    def Run(self):
        for i in range(0, c.numsteps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            # time.sleep(c.timestep)

    def Get_Fitness(self):
        self.robot.Get_Fitness()


def __del__(self):
    p.disconnect()

