from ALEFramework.AgentLegged import AgentLegged
import math
import numpy as np
import time
class LeggedPrey(AgentLegged):
    """docstring for LeggedPrey."""

    def __init__(self, mdNames, forSpeed, objName, food):
        self.food = food
        self.mdNames = mdNames
        self.objName = objName
        self.forSpeed = forSpeed
        self.isRunning = False
        super().__init__(self.mdNames, self.forSpeed, self.objName)
        self.moveForward()

    def preyBehaviour(self):
        self.checkEnergyCollision(self.food)
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


    def run(self, angle):

        if angle < -1:
            check = self.checkObstacle()
            if check is False:
                self.turnRight()

        elif angle > 1:
            check = self.checkObstacle()
            if check is False:
                self.turnLeft()

        elif angle <= 1 and angle >= -1:
            check = self.checkObstacle()
            if check is False:
                self.turnLeft()
            else:
                self.avoidObstacle(check)
