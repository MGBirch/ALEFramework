from ALEFramework.AgentLegged import AgentLegged
import math
import numpy as np
class Predator(AgentVehicle, AgentLegged):
    """docstring for AgentVehicle."""

    def __init__(self, mdNames, turnSpeed, forSpeed, objName, preyName):
        self.preyName = preyName
        self.mdNames = mdNames
        self.objName = objName
        self.turnSpeed = turnSpeed
        self.forSpeed = forSpeed
        super().__init__(self.mdNames, self.turnSpeed, self.forSpeed, self.objName)
        self.moveForward()

    def predBehaviour(self):
        self.checkEnergyCollision(self.preyName)
        self.moveForward()
        isObstacle = self.checkObstacle()
        if isObstacle:
            self.avoidObstacle(isObstacle)

        angle = self.checkRecogniseSource()


        self.chase(angle)

    def chase(self, angle):
        if angle < -0.1:
            check = self.checkObstacle()
            if check is False:
                self.turnSlowLeft()

        elif angle > 0.1:
            check = self.checkObstacle()
            if check is False:
                self.turnSlowRight()

        elif angle <= 0.1 and angle >= -0.1:
            check = self.checkObstacle()
            if check is False:
                self.moveForward()
