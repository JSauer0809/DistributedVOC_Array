import matplotlib.pyplot as plt
import matplotlib.animation as animation
import qwiic_sgp40
import qwiic
import numpy as np
my_sgp40 = qwiic_sgp40.QwiicSGP40()
test = qwiic.QwiicTCA9548A()

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((5, -5), 0.75, fc='y')
patch2 = plt.Circle((5, -5), 0.75, fc='k')


def init():
    patch.center = (2, 2)
    ax.add_patch(patch)
    patch2.center = (6, 6)
    ax.add_patch(patch2)
    return patch, patch2,

def animate(i):
    #x, y = patch.center
    #x = 5 + 3 * np.sin(np.radians(i))
    #y = 5 + 3 * np.cos(np.radians(i))
    #patch.center = (x, y)
    test.enable_channels([0])
    VocIntensity = ((30000/my_sgp40.measure_raw())-1)*80
    test.disable_channels([0])
    patch.radius = VocIntensity/2
    
    test.enable_channels([7])
    VocIntensity = ((30000/my_sgp40.measure_raw())-1)*80
    test.disable_channels([7])
    patch2.radius = VocIntensity/2
    return patch, patch2,

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)

plt.show()

