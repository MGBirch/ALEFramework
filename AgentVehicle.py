from ALEFramework.Agent import Agent
import math
import numpy as np
class AgentVehicle(Agent):
    """docstring for AgentVehicle."""

    def __init__(self, mdNames):
        self.mdNames = mdNames
        super().__init__(self.mdNames)
        self.battery = self.robot.getFromDef('battery')

    def checkEnergyCollision(self):
        carPos = self.getPosition('car')
        carPos = np.array(carPos)
        batteryPos = self.battery.getPosition()
        batteryPos = np.array(batteryPos)

        dist = np.linalg.norm(carPos - batteryPos)

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
