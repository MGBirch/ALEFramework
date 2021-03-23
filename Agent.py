from ALEFramework.Entity import Entity
import numpy as np
import random

from controller import DistanceSensor, Motor, Camera, CameraRecognitionObject
class Agent(Entity):
    """docstring for Agent."""

    def __init__(self, mdNames):
        super().__init__()
        self.energy = 10000
        self.isAlive = True
        self.timestep = int(self.robot.getBasicTimeStep())
        self.camera = self.robot.getDevice('camera')
        self.camera.enable(self.timestep)
        self.camera.recognitionEnable(self.timestep)
        self.MAX_SPEED = 10
        self.ds = []
        self.md = []
        self.dsNames = ['ds_left', 'ds_right', 'ds_left(1)', 'ds_right(1)']

        for i in range(4):
            self.ds.append(self.robot.getDevice(self.dsNames[i]))
            self.ds[i].enable(self.timestep)

        self.length = len(self.mdNames)
        for i in range(self.length):
            self.md.append(self.robot.getDevice(self.mdNames[i]))


    def multiMoveMotorPos(self, devices, dPos):
        i = 0
        for device in devices:
            device.setPosition(dPos)
            i=i+1

    def setMultiMotorVel(self, devices, vel):
        i = 0
        for device in devices:
            device.setVelocity(vel*self.MAX_SPEED)
            self.velocity = vel
            i=i+1

    def getEnergy(self):
        return self.energy

        if dist < 0.25:
            bField = self.battery.getField('translation')
            randX = random.uniform(-2.45, 2.45)
            randZ = random.uniform(-2.45, 2.45)

            newPos = [randX,0.05,randX]
            bField.setSFVec3f(newPos)

            self.energy = self.energy + 2000
            if self.energy > 10000:
                self.energy = 10000

    def turnLeft(self, value):
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity((-0.5*value) * self.MAX_SPEED)
            else:
                self.md[i].setVelocity((0.5*value) * self.MAX_SPEED)
            count = count + 1

    def turnRight(self, value):
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity((0.5*value) * self.MAX_SPEED)
            else:
                self.md[i].setVelocity((-0.5*value) * self.MAX_SPEED)
            count = count + 1

    def moveForward(self):
        for i in range(self.length):
                self.md[i].setVelocity(0.5 * self.MAX_SPEED)

    def turnSlowLeft(self, value):
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity((0.1*value) * self.MAX_SPEED)
            else:
                self.md[i].setVelocity((0.3*value) * self.MAX_SPEED)
            count = count + 1

    def turnSlowRight(self, value):
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity((0.3*value) * self.MAX_SPEED)
            else:
                self.md[i].setVelocity((0.1*value) * self.MAX_SPEED)
            count = count + 1

    def checkObstacle(self, turnValue):
        dsValues = []
        for i in range(4):
            dsValues.append(self.ds[i].getValue())

        left_obstacle = dsValues[0] < 1000.0  or dsValues[2] < 1000.0
        right_obstacle = dsValues[1] < 1000.0 or dsValues[3] < 1000.0

        if left_obstacle:
            self.turnRight(turnValue)
            return True
        elif right_obstacle:
            self.turnLeft(turnValue)
            return True
        else:
            return False

    def checkRecogniseSource(self, turnValue):
        currClosest = [1000,100, 1000]
        minDist = float('inf')
        recognisedObj = self.camera.getRecognitionObjects()

        for obj in recognisedObj:
            currObj = obj.get_position()
            distance = math.sqrt(currObj[0]*currObj[0]+currObj[2]*currObj[2])
            if distance < minDist:
                minDist = distance
                currClosest = currObj

        if recognisedObj:
            x = currClosest[0]
            angle = x *minDist

            if angle>0.03:
                check = self.checkObstacle(turnValue)
                if check is False:
                    self.turnSlowRight(turnValue)
                    return True
            elif angle<-0.03:
                check = self.checkObstacle(turnValue)
                if check is False:
                    self.turnSlowLeft(turnValue)
                    return True
            elif angle <= 0.03 and angle >= -0.03:
                check = self.checkObstacle(turnValue)
                if check is False:
                    self.moveForward()
                    return True
        else:
            self.moveForward()
        return False

    def getWheels(self):
        return self.md
