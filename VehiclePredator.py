from ALEFramework.AgentVehicle import AgentVehicle
import math
import numpy as np
class Predator(AgentVehicle):
    """docstring for AgentVehicle."""

    def __init__(self, mdNames, turnSpeed, forSpeed, objName, preyName):
        self.preyName = preyName
        self.mdNames = mdNames
        self.objName = objName
        self.turnSpeed = turnSpeed
        self.forSpeed = forSpeed
        self.FOCUS_ANGLE = 0.3
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
        if angle < -FOCUS_ANGLE:
            check = self.checkObstacle()
            if check is False:
                self.turnSlowLeft()

        elif angle > FOCUS_ANGLE:
            check = self.checkObstacle()
            if check is False:
                self.turnSlowRight()

        elif angle <= FOCUS_ANGLE and angle >= -FOCUS_ANGLE:
            check = self.checkObstacle()
            if check is False:
                self.moveForward()

    def setFocusAngle(self, angle):
        FOCUS_ANGLE = angle
