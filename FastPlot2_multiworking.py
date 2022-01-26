#This program is designed for a raspberry PI, connected through an 8 channel I2C multiplexer (TCA9548A) to 8 SGP40 VOC sensors. 
#It simulataneously plots 8 time series of VOC intensity data from the sensors using blitting to keep the refresh rate on the console quick. 
import matplotlib.pyplot as plt #import plotting library
import matplotlib.animation as animation #import animation library
import qwiic_sgp40 #import SGP40 VOC Sensor Library
import qwiic #import library for I2C functions
my_sgp40 = qwiic_sgp40.QwiicSGP40() 
test = qwiic.QwiicTCA9548A()
# Parameters
x_len = 200         # Number of points to display
y_range = [25000, 34000]  # Range of possible Y values to display

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, 200)) #generate x axis for plot
ys = [0] * x_len #generate 8 arrays of x_length filled with 0 
ys2 = [0] * x_len
ys3 = [0] * x_len
ys4 = [0] * x_len
ys5 = [0] * x_len
ys6 = [0] * x_len
ys7 = [0] * x_len
ys8 = [0] * x_len

ax.set_ylim(y_range) #Set range of yaxis

# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)
line2, = ax.plot(xs, ys2)
line3, = ax.plot(xs, ys3)
line4, = ax.plot(xs, ys4)
line5, = ax.plot(xs, ys5)
line6, = ax.plot(xs, ys6)
line7, = ax.plot(xs, ys7)
line8, = ax.plot(xs, ys8)

# Add labels
plt.title('VOC Intensity')
plt.xlabel('Samples')
plt.ylabel('Raw Signal (counts)')

# This function is called periodically from FuncAnimation
def animate(i, ys, ys2, ys3, ys4, ys5, ys6, ys7, ys8):

    # Read raw VOC signal from SGP40
    test.enable_channels([0])
    VocIntensity = my_sgp40.measure_raw()
    test.disable_channels([0])
    test.enable_channels([1])
    VocIntensity2 = my_sgp40.measure_raw()
    test.disable_channels([1])
    test.enable_channels([2])
    VocIntensity3 = my_sgp40.measure_raw()
    test.disable_channels([2])
    test.enable_channels([3])
    VocIntensity4 = my_sgp40.measure_raw()
    test.disable_channels([3])
    test.enable_channels([4])
    VocIntensity5 = my_sgp40.measure_raw()
    test.disable_channels([4])
    test.enable_channels([5])
    VocIntensity6 = my_sgp40.measure_raw()
    test.disable_channels([5])
    test.enable_channels([6])
    VocIntensity7 = my_sgp40.measure_raw()
    test.disable_channels([6])
    test.enable_channels([7])
    VocIntensity8 = my_sgp40.measure_raw()
    test.disable_channels([7])
    
    print(VocIntensity, VocIntensity2, VocIntensity3, VocIntensity4, VocIntensity5, VocIntensity6, VocIntensity7, VocIntensity8)

    # Add y to list
    ys.append(VocIntensity)
    ys2.append(VocIntensity2)
    ys3.append(VocIntensity3)
    ys4.append(VocIntensity4)
    ys5.append(VocIntensity5)
    ys6.append(VocIntensity6)
    ys7.append(VocIntensity7)
    ys8.append(VocIntensity8)
    
    # Limit y list to set number of items
    ys = ys[-x_len:]
    ys2 = ys2[-x_len:]
    ys3 = ys3[-x_len:]
    ys4 = ys4[-x_len:]
    ys5 = ys5[-x_len:]
    ys6 = ys6[-x_len:]
    ys7 = ys6[-x_len:]
    ys8 = ys6[-x_len:]
    
    # Update line with new Y values
    line.set_ydata(ys)
    line2.set_ydata(ys2)
    line3.set_ydata(ys3)
    line4.set_ydata(ys4)
    line5.set_ydata(ys5)
    line6.set_ydata(ys6)
    line6.set_ydata(ys7)
    line6.set_ydata(ys8)
    
    return line, line2, line3, line4, line5, line6, line7, line8,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,ys2,ys3,ys4,ys5,ys6,ys7,ys8),
    interval=50,
    blit=True)
plt.show()
