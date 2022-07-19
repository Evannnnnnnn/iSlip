import datetime as dt
import time

import matplotlib; matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure for plotting
import serial

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
y1s = []
y2s = []




def animate(i, xs, y1s, y2s):
    # Read temperature (Celsius) from TMP102
    ser = serial.Serial()
    ser.port = 'COM6'
    ser.baudrate = 9600
    time.sleep(0.1)
    ser.open()

    pressure1 = int(ser.readline())
    pressure2 = int(ser.readline())

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    y1s.append(pressure1)
    print(y1s)
    y2s.append(pressure2)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    y1s = y1s[-20:]
    y2s = y2s[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, y1s)
    ax.plot(xs, y2s)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Pressure applied (Front vs. Back)')
    plt.ylabel('Pressure (N)')


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, y1s, y2s), interval=10)
plt.show()
