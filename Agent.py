from ALEFramework.Entity import Entity
import numpy as np
import random

from controller import DistanceSensor, Motor, Camera, CameraRecognitionObject
class Agent(Entity):
    """docstring for Agent."""

    def __init__(self):
        super().__init__()
        self.energy = 10000
        self.isAlive = True
        self.battery = self.robot.getFromDef('battery')
        self.timestep = int(self.robot.getBasicTimeStep())
        self.camera = self.robot.getDevice('camera')
        self.camera.enable(self.timestep)
        self.camera.recognitionEnable(self.timestep)


    def multiMoveMotorPos(self, devices, dPos):
        i = 0
        for device in devices:
            device.setPosition(dPos)
            i=i+1

    def setMultiMotorVel(self, devices, vel):
        i = 0
        for device in devices:
            device.setVelocity(vel)
            i=i+1

    def getEnergy(self):
        return self.energy

    def checkEnergyCollision(self):
        carPos = self.getPosition('car')
        carPos = np.array(carPos)
        batteryPos = self.battery.getPosition()
        batteryPos = np.array(batteryPos)

        dist = np.linalg.norm(carPos - batteryPos)


        if dist < 0.25:
            bField = self.battery.getField('translation')
            randX = random.uniform(-2.45, 2.45)
            randZ = random.uniform(-2.45, 2.45)

            newPos = [randX,0.05,randX]
            bField.setSFVec3f(newPos)

            self.energy = self.energy + 2000
            if self.energy > 10000:
                self.energy = 10000
