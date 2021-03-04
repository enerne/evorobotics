import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import random
import numpy

PI = numpy.pi

numsteps=1000
#
#
b_amplitude, b_frequency, b_phaseOffset = PI/3, 10, 0
f_amplitude, f_frequency, f_phaseOffset = PI/4, 20, PI/4
target_angles = numpy.linspace(-PI, PI, 1000)
b_target_angles = numpy.array([b_amplitude * numpy.sin(b_frequency * i + b_phaseOffset) for i in target_angles])
f_target_angles = numpy.array([f_amplitude * numpy.sin((f_frequency * i + f_phaseOffset)) for i in target_angles])
numpy.save("data/back_target_angles.npy", b_target_angles)
numpy.save("data/front_target_angles.npy", f_target_angles)

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)



planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate("body.urdf")
p.loadSDF("world.sdf")
backLegSensorValues = numpy.zeros(numsteps)
frontLegSensorValues = numpy.zeros(numsteps)

for i in range(0,numsteps):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # BACK LEG MOTOR
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robot,

        jointName="Torso_BackLeg",

        controlMode=p.POSITION_CONTROL,

        targetPosition=b_target_angles[i],

        maxForce=100)

    # FRONT LEG MOTOR
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robot,

        jointName="Torso_FrontLeg",

        controlMode=p.POSITION_CONTROL,

        targetPosition=f_target_angles[i],

        maxForce=100)

    time.sleep(1.0/240.0)

p.disconnect()
print(backLegSensorValues)
numpy.save("data/backlegtouches.npy", backLegSensorValues)
numpy.save("data/frontlegtouches.npy", frontLegSensorValues)

