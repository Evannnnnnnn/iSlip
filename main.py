import datetime as dt
import time

import matplotlib; matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import serial

import threading

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def openSerial():
    global xs, y1s, y2s
    xs = []
    y1s = []
    y2s = []
    ser = serial.Serial()
    ser.port = 'COM6'
    ser.baudrate = 9600
    time.sleep(2)
    ser.open()
    while True:
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


def animate(i):
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
t = threading.Thread(target=openSerial, daemon=True)
t.start()
time.sleep(2)
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
