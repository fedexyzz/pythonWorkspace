from rocketClass import Rocket
import matplotlib.pyplot as plt

rockets = []
rockets.append(Rocket())
rockets.append(Rocket(0,2))
rockets.append(Rocket(1,4))
rockets.append(Rocket(2,6))
rockets.append(Rocket(3,7))
rockets.append(Rocket(5,9))
rockets.append(Rocket(8,15))

for index, rocket in enumerate(rockets):
    print("Rocket %d is at (%d,%d)." % (index, rocket.x, rocket.y))
    plt.plot(rocket.x, rocket.y, 'ro', linewidth = 2, linestyle = 'dashed', markersize = 12)
