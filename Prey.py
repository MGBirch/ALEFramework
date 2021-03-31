from ALEFramework.AgentVehicle import AgentVehicle
import math
import numpy as np
import time
class Prey(AgentVehicle, AgentLegged):
    """docstring for AgentVehicle."""

    def __init__(self, mdNames, turnSpeed, forSpeed, objName):
        self.mdNames = mdNames
        self.objName = objName
        self.turnSpeed = turnSpeed
        self.forSpeed = forSpeed
        self.isRunning = False
        super().__init__(self.mdNames, self.turnSpeed, self.forSpeed, self.objName)
        self.moveForward()

    def preyBehaviour(self):

        isObstacle = self.checkObstacle()
        angle = self.checkRecogniseSource()
        if angle:
            isRunning = True
        else:
            isRunning = False

        if isRunning:
            self.run(angle)
        elif isObstacle:
            self.avoidObstacle(isObstacle)
        else:
            self.moveForward()

        self.checkEnergyCollision()

    def run(self, angle):

        if angle < -1:
            check = self.checkObstacle()
            if check is False:
                print("right")
                self.turnRight()

        elif angle > 1:
            check = self.checkObstacle()
            if check is False:
                print("left")
                self.turnLeft()

        elif angle <= 1 and angle >= -1:
            check = self.checkObstacle()
            if check is False:
                self.turnLeft()
            else:
                self.avoidObstacle(check)
