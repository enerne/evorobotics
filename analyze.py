import matplotlib.pyplot as plt
import numpy

# backsensorvals = numpy.load("data/backlegtouches.npy")
# fronsensorvals = numpy.load("data/frontlegtouches.npy")
# plt.plot(backsensorvals, label="back", linewidth=2.6)
# plt.plot(fronsensorvals, label="front")
# plt.legend()
sine = numpy.load("data/back_target_angles.npy")
sine2 = numpy.load("data/front_target_angles.npy")
plt.plot(sine)
plt.plot(sine2)
plt.show()