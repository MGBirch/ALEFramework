from ALEFramework.Agent import Agent
import math
import numpy as np
class AgentVehicle(Agent):
    """docstring for AgentVehicle."""

    def __init__(self, mdNames, turnSpeed, forSpeed, objName):
        self.mdNames = mdNames
        self.objName = objName
        self.turnSpeed = turnSpeed
        self.forSpeed = forSpeed
        super().__init__(self.mdNames, self.objName)


    def moveForward(self):
        for i in range(self.length):
                self.md[i].setVelocity(self.forSpeed * self.MAX_SPEED)

    def moveBackward(self):
        for i in range(self.length):
                self.md[i].setVelocity(self.forSpeed * self.LOW_SPEED)

    def turnSlowLeft(self):
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity((0.1*self.turnSpeed) * self.MAX_SPEED)
            else:
                self.md[i].setVelocity((0.3*self.turnSpeed) * self.MAX_SPEED)
            count = count + 1

    def turnSlowRight(self):
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity((0.3*self.turnSpeed) * self.MAX_SPEED)
            else:
                self.md[i].setVelocity((0.1*self.turnSpeed) * self.MAX_SPEED)
            count = count + 1

    def turnLeft(self):
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity(self.turnSpeed* self.LOW_SPEED)
            else:
                self.md[i].setVelocity(self.turnSpeed * self.MAX_SPEED)
            count = count + 1

    def turnRight(self):
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity(self.turnSpeed * self.MAX_SPEED)
            else:
                self.md[i].setVelocity(self.turnSpeed * self.LOW_SPEED)
            count = count + 1

    def setWheelSpeed(self, wheelName, velocity):
        limb = self.robot.getDevice(wheelName)
        limb.setVelocity(velocity)
