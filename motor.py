from pyrosim import pyrosim
import pybullet as p
import constants as c
import numpy

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude, self.frequency, self.offset = c.amplitude, c.frequency, c.phaseOffset

        if self.jointName == "Torso_BackLeg":
            self.frequency *= 0.5

        self.motor_values = numpy.linspace(-numpy.pi, numpy.pi, c.numsteps)
        for i in range(0, c.numsteps):
            self.motor_values[i] = self.amplitude * numpy.sin(
                self.frequency * self.motor_values[i] + self.offset)

        print(self.motor_values)

    def Set_Value(self, robot, i):
        # FRONT LEG MOTOR
        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robot,

            jointName=self.jointName,

            controlMode=p.POSITION_CONTROL,

            targetPosition=self.motor_values[i],

            maxForce=c.max_motor_force)

    def Save_Values(self):
        numpy.save("data/" + self.jointName + "motor.npy", self.motor_values)