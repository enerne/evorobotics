import os
from hill_climber import HILL_CLIMBER

# for i in range(5):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")
#

hc = HILL_CLIMBER()
hc.parent.Evaluate("GUI")
hc.Evolve()
hc.Show_Best()