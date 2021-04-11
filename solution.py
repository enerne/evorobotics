import os
import numpy
import pyrosim.pyrosim as p
import random
import time


class SOLUTION:
    def __init__(self, id):
        self.myID = id
        self.weights = numpy.random.random(size=(3,2))
        self.weights = self.weights * 2 - 1

    def Start_Simulation(self, dOrG):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("python3 simulate.py " + dOrG + " " + str(self.myID) + " 2&>1 &")


    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        with open(fitnessFileName, "r") as infile:
            self.fitness = float(infile.read().rstrip())
        os.system("rm " + fitnessFileName)

    def Evaluate(self, dOrG):
        self.Start_Simulation(dOrG)
        self.Wait_For_Simulation_To_End()


    def Create_World(self):
        p.Start_SDF("world.sdf")
        length = 1
        width = 2
        height = 3
        p.Send_Cube(name="Box", pos=[5, 5, 1.5], size=[length, width, height])
        p.End()

    def Create_Body(self):
        p.Start_URDF("body.urdf")
        p.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
        p.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="-0.5 0 1")
        p.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        p.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="0.5 0 1")
        p.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
        p.End()

    def Create_Brain(self):
        p.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        p.Send_Sensor_Neuron(name=0, linkName="Torso")
        p.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        p.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        p.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        p.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # when both are -1, they should return to stable
        # when they both touch the ground, back leg should move (slower?) than front leg
        # when only one is touching the ground, it should move slower than the one in the air

        for currentRow in range(3):
            for currentColumn in range(2):
                p.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3,
                               weight=self.weights[currentRow][currentColumn])

        # p.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=1.5)
        # p.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-0.2)
        #

        p.End()

    def Mutate(self):
        row = random.randint(0,2)
        col = random.randint(0,1)
        self.weights[row, col] = random.random() * 2 - 1

    def Set_ID(self, id):
        self.myID = id