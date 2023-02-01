import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def main():
    global x, p, i, d, e, fig, ax, ser, line1, line2, line3, line4
    ser = serial.Serial('/dev/tty.usbmodem1302', 115200)
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    x = []
    p = []
    i = []
    d = []
    e = []
    ax.set_ylim(-1023, 1023)
    
    line1, = ax.plot(x, p, color='blue')
    line2, = ax.plot(x, i, color='red')
    line3, = ax.plot(x, d, color='green')
    line4, = ax.plot(x, e, color='yellow')
    
    anim = FuncAnimation(fig, update, interval=10, blit=True)
    
    plt.show()
       

def update(num):
    global p, i, d, e
    nums = []
    x.append(num)
    serialline = ser.readline()
    serialline =  serialline.strip()
    stringinserial = serialline.decode()
    
    words = stringinserial.split(" ")
    for word in words:
        if isfloat(word):
            nums.append(float(word))
    print(nums)
    if nums != None:
        p.append(nums[0])
        i.append(nums[1])
        d.append(nums[2])
        e.append(nums[3])
    line1.set_data(x, p)
    line2.set_data(x, i)
    line3.set_data(x, d)
    line4.set_data(x, e)
    if len(x) > 1 : ax.set_xlim(x[len(x)-1]-50, x[len(x) - 1])
    fig.canvas.draw()
    return line1, line2, line3, line4
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
if __name__ == "__main__": main()