import numpy

PI = numpy.pi
numsteps = 3000
max_motor_force = 200
timestep = 1.0 / 480.0

populationSize = 10

numSensorNeurons = 4
numMotorNeurons = 8

target_angles = numpy.linspace(-PI, PI, numsteps)
amplitude, frequency, phaseOffset = PI/4, 20, PI/4
b_amplitude, b_frequency, b_phaseOffset = PI/3, 10, 0
f_amplitude, f_frequency, f_phaseOffset = PI/4, 20, PI/4

b_target_angles = numpy.array([b_amplitude * numpy.sin(b_frequency * i + b_phaseOffset) for i in target_angles])
f_target_angles = numpy.array([f_amplitude * numpy.sin((f_frequency * i + f_phaseOffset)) for i in target_angles])

motorJointRange = 0.3

numberOfGenerations = 10
