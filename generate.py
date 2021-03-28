import pyrosim.pyrosim as p


def Create_World():
    p.Start_SDF("world.sdf")
    length = 1
    width = 2
    height = 3
    p.Send_Cube(name="Box", pos=[5, 5, 1.5], size=[length, width, height])
    p.End()


def Generate_Body():
    p.Start_URDF("body.urdf")
    p.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
    p.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="-0.5 0 1")
    p.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1])
    p.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="0.5 0 1")
    p.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1])
    p.End()


def Generate_Brain():
    p.Start_NeuralNetwork("brain.nndf")

    p.Send_Sensor_Neuron(name=0, linkName="Torso")
    p.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    p.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    p.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    p.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")


    p.End()


if __name__ == "__main__":
    Create_World()
    Generate_Body()
    Generate_Brain()