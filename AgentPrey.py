from ALEFramework.Agent import Agent
import math
class AgentPrey(Agent):
    """docstring for AgentVehicle."""

    def __init__(self, mdNames):
        self.mdNames = mdNames
        super().__init__(self.mdNames)


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

            if angle>=-0.01:
                check = self.checkObstacle(turnValue)
                if check is False:
                    self.turnLeft(turnValue)
                    return True
            elif angle<-0.01:
                check = self.checkObstacle(turnValue)
                if check is False:
                    self.turnRight(turnValue)
                    return True
        else:
            self.moveForward()

        return False
