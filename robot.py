import pybullet as p
from pyrosim import pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK


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


        # brain stuff
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor_name in self.sensors:
            sensor = self.sensors[sensor_name]
            sensor.Get_Value(t)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            motor = MOTOR(jointName)
            self.motors[jointName] = motor

    def Act(self, t):

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                motor = self.motors[jointName]
                motor.Set_Value(self.robot, desiredAngle)
                print(neuronName, jointName, desiredAngle)
