
from microbit import *
from DeviceClass import Device
import math
import radio


#pin0 = left motor f
#pin1 = right motor f
#pin8 = left motor b
#pin12 = right motor b
#one r of wheel = 19 cm 


def main():
    device = Device(ShowOnDisplay=True)
    radio.config(group=1)
    radio.on()
    kp, ki, kd, setpoint = 0.0, 0.0, 0.0, 0.0
    while True:
        msg = radio.receive()
        #print(radio.receive())
        #print(msg)
        if msg != None:
            floatnum = getfloatfromstring(msg)
            if floatnum != None:
                kp = floatnum[0]
                ki = floatnum[1]
                kd = floatnum[2]
                setpoint = floatnum[3]
        sleep(100)
        device.balance(kp, ki, kd, setpoint)
        values = str(device.porportioal) + ' ' + str(device.integral) + ' ' + str(device.derivative) + ' ' + str(device.error)
        sleep(10)
        radio.send(values)
             
def getfloatfromstring(s):
    numlist = []
    words = s.split(" ")

    for word in words:
        numlist.append(float(word))
    return numlist
        #try:
            #num = float(word)
            #return num
        #except ValueError:
            #continue
    #return None
    
if __name__ == "__main__":
    main()
