from ALEFramework.Agent import Agent
import math
class AgentLegged(Agent):
    """docstring for AgentVehicle."""

    def __init__(self, mdNames, turnSpeed, forSpeed, objName):
        self.mdNames = mdNames
        self.objName = objName
        self.turnSpeed = turnSpeed
        self.forSpeed = forSpeed
        self.legPos = []
        super().__init__(self.mdNames, self.objName)
        for i in range(self.length):
            self.legPos.append(0)

    def moveForward(self):
        print("forward")
        for i in range(self.length):
            self.md[i].setVelocity(self.forSpeed * self.MAX_SPEED)
            currPos = self.legPos[i]
            self.md[i].setPosition(currPos + 0.1)
            self.legPos[i] = currPos + 0.1

    def turnLeft(self):
        print("left")
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity(self.turnSpeed  * self.MAX_SPEED)

            else:
                self.md[i].setVelocity(self.turnSpeed * self.MAX_SPEED)
                currPos = self.legPos[i]
                self.md[i].setPosition(currPos + 0.1)
                self.legPos[i] = currPos + 0.1
            count = count + 1

    def turnRight(self):
        print("right")
        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                self.md[i].setVelocity(0* self.MAX_SPEED)
                currPos = self.legPos[i]
                self.md[i].setPosition(currPos + 0.1)
                self.legPos[i] = currPos + 0.1
            else:
                self.md[i].setVelocity(self.turnSpeed * self.MAX_SPEED)
            count = count + 1

    def turnSlowLeft(self):
        print("slow left")
        half = self.length/2
        count = 0
        for count in range(self.length):
            if(count<half):
                self.md[count].setVelocity(0.1*self.turnSpeed * self.MAX_SPEED)

            else:
                self.md[count].setVelocity((0.3*self.turnSpeed) * self.MAX_SPEED)
                currPos = self.legPos[count]
                self.md[count].setPosition(currPos + 0.1)
                self.legPos[count] = currPos + 0.1
            count = count + 1

    def turnSlowRight(self):
        print("slow right")
        half = self.length/2
        count = 0
        for count in range(self.length):
            if(count<half):
                self.md[count].setVelocity((0.3*self.turnSpeed) * self.MAX_SPEED)
                currPos = self.legPos[count]
                self.md[count].setPosition(currPos + 0.1)
                self.legPos[count] = currPos + 0.1
            else:
                self.md[count].setVelocity(0.1*self.turnSpeed * self.MAX_SPEED)

            count = count + 1
