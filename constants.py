import numpy

PI = numpy.pi
numsteps = 1000
max_motor_force = 100
timestep = 1.0 / 240.0

target_angles = numpy.linspace(-PI, PI, numsteps)
amplitude, frequency, phaseOffset = PI/4, 20, PI/4
b_amplitude, b_frequency, b_phaseOffset = PI/3, 10, 0
f_amplitude, f_frequency, f_phaseOffset = PI/4, 20, PI/4

b_target_angles = numpy.array([b_amplitude * numpy.sin(b_frequency * i + b_phaseOffset) for i in target_angles])
f_target_angles = numpy.array([f_amplitude * numpy.sin((f_frequency * i + f_phaseOffset)) for i in target_angles])
