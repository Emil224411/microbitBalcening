from microbit import *
import math

class Device:
    def __init__(self, ShowOnDisplay):
        self.leftmotor = motor("leftmotor")
        self.rightmotor = motor("rightmotor")
        
        self.porportioal = 0
        self.integral = 0
        self.derivative = 0

        self.stoped = True
        self.ShowOnDisplay = ShowOnDisplay
        self.setpoint = 0
        self.preverror = 0
        self.results = 0
        self.error = 0

    def pause(self):
        print("Paused presse button b to start again")
        self.updateAngel(False)
        self.leftmotor.stop()
        self.rightmotor.stop()
        sleep(1000)
        
    
    def updateAngel(self, ShowOnDisplay):
        y, z = accelerometer.get_y(), accelerometer.get_z()
        self.angel = math.degrees(math.atan2(y, z))
        if self.angel > 107 and ShowOnDisplay: display.show(Image.ARROW_N)
        elif self.angel < 107 and ShowOnDisplay: display.show(Image.ARROW_S)

    def pid(self, kp, ki, kd, setpoint):
        self.updateAngel(self.ShowOnDisplay)

        self.error = setpoint - self.angel
        self.porportioal = self.error * kp
        self.integral += self.error * ki
            
        self.derivative = (self.error - self.preverror) * kd
        self.preverror = self.error

        self.results = self.porportioal + self.integral + self.derivative
        if self.results > 1023 : self.results = 1023
        elif self.results < -1023 : self.results = 1023
        if self.angel > 170 or self.angel < 15: 
            self.results = 0
            #print("cant save it")

    def balance(self, kp, ki, kd, setpoint):
        self.pid(kp, ki, kd, setpoint)
        
        if self.results < 0: 
            self.moveall("b", abs(self.results))
            self.stoped = False
        
        elif self.results > 0: 
            self.moveall("f", abs(self.results))
            self.stoped = False

    def moveall(self, d, speed):
        if d == "f":
            self.leftmotor.move(d, speed)
            self.rightmotor.move(d, speed)

        elif d == "b":
            self.leftmotor.move(d, speed)
            self.rightmotor.move(d, speed)
    
    def stopall(self):
        self.leftmotor.stop
        self.rightmotor.stop
        self.stoped = True

class motor:
    def __init__(self, name):
        self.name = name
        if self.name == "leftmotor":
            self.p0 = pin0
            self.p1 = pin8
        elif self.name == "rightmotor":
            self.p0 = pin1
            self.p1 = pin12

    def move(self, d, speed):
        if d == "f":
            self.p0.write_analog(speed)
            self.p1.write_analog(0)
        elif d == "b":
            self.p0.write_analog(0)
            self.p1.write_analog(speed)
    
    def stop(self):
        self.p0.write_analog(0)
        self.p1.write_analog(0)
