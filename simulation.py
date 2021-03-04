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
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            #
            # # BACK LEG MOTOR
            # pyrosim.Set_Motor_For_Joint(
            #
            #     bodyIndex=robot,
            #
            #     jointName="Torso_BackLeg",
            #
            #     controlMode=p.POSITION_CONTROL,
            #
            #     targetPosition=c.b_target_angles[i],
            #
            #     maxForce=c.max_motor_force)
            #
            # # FRONT LEG MOTOR
            # pyrosim.Set_Motor_For_Joint(
            #
            #     bodyIndex=robot,
            #
            #     jointName="Torso_FrontLeg",
            #
            #     controlMode=p.POSITION_CONTROL,
            #
            #     targetPosition=c.f_target_angles[i],
            #
            #     maxForce=c.max_motor_force)
            #
            time.sleep(c.timestep)
            pass


def __del__(self):
    p.disconnect()

