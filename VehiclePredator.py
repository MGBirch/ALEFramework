from ALEFramework.AgentVehicle import AgentVehicle
import math
import numpy as np
class VehiclePredator(AgentVehicle):
    """docstring for VehiclePredator."""

    def __init__(self, mdNames, turnSpeed, forSpeed, objName):
        self.mdNames = mdNames
        self.objName = objName
        self.turnSpeed = turnSpeed
        self.forSpeed = forSpeed
        self.FOCUS_ANGLE = 0.3
        super().__init__(self.mdNames, self.turnSpeed, self.forSpeed, self.objName)
        self.moveForward()

    def predBehaviour(self):
        self.moveForward()
        isObstacle = self.checkObstacle()
        if isObstacle:
            self.avoidObstacle(isObstacle)

        angle = self.checkRecogniseSource()


        self.chase(angle)

    def chase(self, angle):
        if angle < -self.FOCUS_ANGLE:
            check = self.checkObstacle()
            if check is False:
                self.turnSlowLeft()

        elif angle > self.FOCUS_ANGLE:
            check = self.checkObstacle()
            if check is False:
                self.turnSlowRight()

        elif angle <= self.FOCUS_ANGLE and angle >= -self.FOCUS_ANGLE:
            check = self.checkObstacle()
            if check is False:
                self.moveForward()

    def setFocusAngle(self, angle):
        self.FOCUS_ANGLE = angle
