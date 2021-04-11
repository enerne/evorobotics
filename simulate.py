import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import random
import numpy
import constants as c
from simulation import SIMULATION
import sys
#
# PI = numpy.pi
#
#
# numpy.save("data/back_target_angles.npy", c.b_target_angles)
# numpy.save("data/front_target_angles.npy", c.f_target_angles)
#

#

# pyrosim.Prepare_To_Simulate("body.urdf")
# p.loadSDF("world.sdf")

#

# p.disconnect()
# print(backLegSensorValues)
# numpy.save("data/backlegtouches.npy", backLegSensorValues)
# numpy.save("data/frontlegtouches.npy", frontLegSensorValues)
#

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Get_Fitness()