import pybullet as p
from pyrosim import pyrosim

from sensor import SENSOR


class ROBOT:
    def __init__(self, s=2, m=2):

        self.motors = {}
        self.sensors = {}
        self.robot = p.loadURDF("body.urdf")
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
