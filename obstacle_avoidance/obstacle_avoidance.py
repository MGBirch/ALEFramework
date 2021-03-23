import cv2
import numpy as np
import math
import random

from controller import Robot, DistanceSensor, Motor, Camera, CameraRecognitionObject, Supervisor, Node
# create the Robot instance.
robot = Supervisor()
MAX_SPEED = 6.28
energy = 10000

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

battery = robot.getFromDef('battery')

car = robot.getFromDef('car')
batteryPos = battery.getPosition()

w1 = robot.getDevice('leg1')
w2 = robot.getDevice('leg2')
w3 = robot.getDevice('leg3')
w4 = robot.getDevice('leg4')

# set the target position of the wheels
w1.setPosition(180/math.pi)
w2.setPosition(90/math.pi)
w3.setPosition(270/math.pi)
w4.setPosition(0/math.pi)

# set velocity of wheels to 0
w1.setVelocity(3)
w2.setVelocity(3)
w3.setVelocity(3.0)
w4.setVelocity(3.0)

ds = []
dsNames = [
    'ds_left', 'ds_right', 'ds_left(1)', 'ds_right(1)'
]

for i in range(4):
        ds.append(robot.getDevice(dsNames[i]))
        ds[i].enable(timestep)

camera = robot.getDevice('camera')
camera.enable(timestep)
camera.recognitionEnable(timestep)

while robot.step(timestep) != -1:

    if energy !=0:

        carPos = car.getPosition()
        carPos = np.array(carPos)
        batteryPos = battery.getPosition()
        batteryPos = np.array(batteryPos)

        dist = np.linalg.norm(carPos - batteryPos)


        if dist < 0.25:
            bField = battery.getField('translation')
            randX = random.uniform(-2.45, 2.45)
            randZ = random.uniform(-2.45, 2.45)

            newPos = [randX,0.05,randX]
            bField.setSFVec3f(newPos)

            energy = energy + 400
            if energy > 10000:
                energy = 10000


        dsValues = []
        for i in range(4):
            dsValues.append(ds[i].getValue())


        left_obstacle = dsValues[0] < 1000.0  or dsValues[2] < 1000.0
        right_obstacle = dsValues[1] < 1000.0 or dsValues[3] < 1000.0

        leftSpeed = 0.5 * MAX_SPEED
        rightSpeed = 0.5 * MAX_SPEED

        if energy < 10000:
            recognisedObj = camera.getRecognitionObjects()

            currClosest = [1000,100, 1000]
            minDist = float('inf')

            for obj in recognisedObj:
                currObj = obj.get_position()
                currOrientation = obj.get_orientation()
                distance = math.sqrt(currObj[0]*currObj[0]+currObj[2]*currObj[2])
                if distance < minDist:
                    minDist = distance
                    currClosest = currObj
                    orientation = currOrientation




            if recognisedObj:

                x = currClosest[0]

                angle = x *minDist

                if angle>0.01:
                    leftSpeed = 0.3 * MAX_SPEED
                    rightSpeed = 0.1 * MAX_SPEED

                elif left_obstacle:
                    #turn the robot to the right
                    leftSpeed = 0.5 * MAX_SPEED
                    rightSpeed = -0.5 * MAX_SPEED
                elif right_obstacle:
                    #turn the robot to the left
                    leftSpeed = -0.5 * MAX_SPEED
                    rightSpeed = 0.5 * MAX_SPEED
                elif angle<-0.01:
                    leftSpeed = 0.1 * MAX_SPEED
                    rightSpeed = 0.3 * MAX_SPEED
                elif angle <= 0.01 and angle >= -0.01:
                   leftSpeed = 0.5 * MAX_SPEED
                   rightSpeed = 0.5 * MAX_SPEED



        if left_obstacle:

            #turn the robot to the right
            leftSpeed = 0.5 * MAX_SPEED
            rightSpeed = -0.5 * MAX_SPEED


        elif right_obstacle:

            #turn the robot to the left
            leftSpeed = -0.5 * MAX_SPEED
            rightSpeed = 0.5 * MAX_SPEED

        energy = energy - 1
    else:
        w1.setVelocity(0)
        w4.setVelocity(0)
        w2.setVelocity(0)
        w3.setVelocity(0)
    pass
