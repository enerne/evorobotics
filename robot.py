import pybullet as p
from pyrosim import pyrosim

from sensor import SENSOR
from motor import MOTOR


class ROBOT:
    def __init__(self, s=2, m=2):

        self.motors = {}
        self.sensors = {}
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor_name in self.sensors:
            sensor = self.sensors[sensor_name]
            sensor.Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            motor = MOTOR(jointName)
            self.motors[jointName] = motor

    def Act(self, t):
        for joint_name in self.motors:
            motor = self.motors[joint_name]
            motor.Set_Value(self.robot, t)