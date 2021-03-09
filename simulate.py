import pybullet as p
import pybullet_data
import Pyrosim.pyrosim as pyrosim
import time
import random
import numpy
import constants as c
from simulation import SIMULATION
#
# PI = numpy.pi
#
#
# numpy.save("data/back_target_angles.npy", c.b_target_angles)
# numpy.save("data/front_target_angles.npy", c.f_target_angles)
#

#

# Pyrosim.Prepare_To_Simulate("body.urdf")
# p.loadSDF("world.sdf")
# backLegSensorValues = numpy.zeros(c.numsteps)
# frontLegSensorValues = numpy.zeros(c.numsteps)
#

# p.disconnect()
# print(backLegSensorValues)
# numpy.save("data/backlegtouches.npy", backLegSensorValues)
# numpy.save("data/frontlegtouches.npy", frontLegSensorValues)
#
simulation = SIMULATION()