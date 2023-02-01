# Imports go at the top
from microbit import *
import radio
def main():
    radio.config(group=1)
    radio.on()

    mode = 1
    setpoint = 106.2
    kp = 0.0
    ki = 0.0
    kd = 0.0
    p, i, d = 0.0, 0.0, 0.0
    floatlist = [0, 0, 0, 0]

    while True:
        if button_a.was_pressed():
            if mode == 1 : kp += 0.5
            elif mode == 2 : ki += 0.005
            elif mode == 3 : kd += 0.05
        if button_b.was_pressed():
            if mode == 1 : kp -= 0.5
            elif mode == 2 : ki -= 0.005
            elif mode == 3 : kd -= 0.05
        if pin_logo.is_touched():
            if mode == 3 : mode = 1
            else: mode += 1
        if mode == 1 : display.show('p')
        elif mode == 2 : display.show('i')
        elif mode == 3 : display.show('d')
        msg = str(kp) + " " + str(ki) +" " + str(kd) + " " + str(setpoint)
        radio.send(msg)
        pid = radio.receive()
        if pid != None:
            floatlist = extract_float_from_string(pid)
            print(str(floatlist[0]) + " " + str(floatlist[1]) + " " + str(floatlist[2]) + " " + str(floatlist[3]))
        sleep(10)
        
def extract_float_from_string(s):
    numlist = []
    words = s.split(" ")

    for word in words:
        numlist.append(float(word))
    
    return numlist


if __name__ == '__main__' : main()