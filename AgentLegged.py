from ALEFramework.Agent import Agent
import math
class AgentLegged(Agent):
    """docstring for AgentVehicle."""

    def __init__(self, mdNames, forSpeed, objName):
        self.mdNames = mdNames
        self.objName = objName
        self.forSpeed = forSpeed
        self.legPos = []
        super().__init__(self.mdNames, self.objName)
        for i in range(self.length):
            self.md[i].setVelocity(self.forSpeed * self.MAX_SPEED)
            self.legPos.append(0)

    def moveForward(self):

        for i in range(self.length):
            currPos = self.legPos[i]
            self.md[i].setPosition(currPos + 0.1)
            self.legPos[i] = currPos + 0.1

    def turnLeft(self):

        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                currPos = self.legPos[count]
                self.md[count].setPosition(currPos - 0.1)
                self.legPos[count] = currPos - 0.1
            else:
                currPos = self.legPos[i]
                self.md[i].setPosition(currPos + 0.1)
                self.legPos[i] = currPos + 0.1
            count = count + 1

    def turnRight(self):

        half = self.length/2
        count = 0
        for i in range(self.length):
            if(count<half):
                currPos = self.legPos[i]
                self.md[i].setPosition(currPos + 0.1)
                self.legPos[i] = currPos + 0.1
            else:
                currPos = self.legPos[count]
                self.md[count].setPosition(currPos - 0.1)
                self.legPos[count] = currPos - 0.1
            count = count + 1

    def turnSlowLeft(self):

        half = self.length/2
        count = 0
        for count in range(self.length):
            if(count<half):
                pass
            else:
                currPos = self.legPos[count]
                self.md[count].setPosition(currPos + 0.1)
                self.legPos[count] = currPos + 0.1
            count = count + 1

    def turnSlowRight(self):

        half = self.length/2
        count = 0
        for count in range(self.length):
            if(count<half):
                currPos = self.legPos[count]
                self.md[count].setPosition(currPos + 0.1)
                self.legPos[count] = currPos + 0.1
            else:
                pass
            count = count + 1

    def limbForward90(self, limbName):
        limb = self.robot.getDevice(limbName)
        limb.setPosition(0.5 * math.pi)

    def limbBackwards90(self, limbName):
        limb = self.robot.getDevice(limbName)
        limb.setPosition(-0.5 * math.pi)

    def limbForwardRotation(self, limbName):
        limb = self.robot.getDevice(limbName)
        limb.setPosition(2 * math.pi)

    def limbBackwardRotation(self, limbName):
        limb = self.robot.getDevice(limbName)
        limb.setPosition(-2 * math.pi)

    def limbRotation(self, limbName, rotationAmount):
        limb = self.robot.getDevice(limbName)
        limb.setPosition(rotationAmount)
