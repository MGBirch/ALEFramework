import numpy as np
import math
import random

from controller import DistanceSensor, Motor, Camera, CameraRecognitionObject, Supervisor
class Agent(object):
    """docstring for Agent."""

    def __init__(self, mdNames, objName):
        super().__init__()
        self.robot = Supervisor()
        self.objName = objName
        self.energy = 10000
        self.timestep = int(self.robot.getBasicTimeStep())
        self.camera = self.robot.getDevice('camera')
        self.camera.enable(self.timestep)
        self.camera.recognitionEnable(self.timestep)
        self.MAX_SPEED = 10
        self.LOW_SPEED = -10
        self.MAX_ENERGY = 10000
        self.consumptionEnergy = 2000
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
        for device in devices:
            device.setPosition(dPos)

    def setMultiMotorVel(self, devices, vel):
        for device in devices:
            device.setVelocity(vel*self.MAX_SPEED)
            self.velocity = vel

    def getEnergy(self):
        return self.energy

    def setEnergy(self, energy):
        self.energy = energy

    def eat(self, prey):
        prey = prey
        pField = prey.getField('translation')
        randX = random.uniform(-2.45, 2.45)
        randZ = random.uniform(-2.45, 2.45)

        newPos = [randX,0.05,randZ]
        pField.setSFVec3f(newPos)

        self.energy = self.energy + self.consumptionEnergy
        if self.energy > self.MAX_ENERGY:
            self.energy = self.MAX_ENERGY

    def checkEnergyCollision(self, preyName):
        if preyName:
            objPos = self.getPosition(self.objName)
            objPos = np.array(objPos)
            objPos = np.array(objPos)
            for i in preyName:
                self.prey = self.robot.getFromDef(i)
                preyPos = self.prey.getPosition()
                preyPos = self.prey.getPosition()
                preyPos = np.array(preyPos)

                dist = np.linalg.norm(objPos - preyPos)

                if dist < 0.4:
                    return self.prey
        else:
            return False



    def getPosition(self, name):
        thing = self.robot.getFromDef(name)
        pos = thing.getPosition()
        return pos

    def checkObstacle(self):
        dsValues = []
        for i in range(4):
            dsValues.append(self.ds[i].getValue())

        left_obstacle = dsValues[0] < 1000.0  or dsValues[2] < 1000.0
        right_obstacle = dsValues[1] < 1000.0 or dsValues[3] < 1000.0

        if left_obstacle:

            return 1
        elif right_obstacle:

            return 2
        else:
            return False

    def checkRecogniseSource(self):
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
            return angle
        else:
            return False

        return False

    def getMotorDevices(self):
        return self.md

    def avoidObstacle(self, value):
        if value == 1:
            self.turnRight()
        elif value == 2:
            self.turnLeft()

    def setMaxEnergy(self, energy):
        self.MAX_ENERGY = energy

    def setConsumptionEnergy(self, energy):
        self.consumptionEnergy = energy
