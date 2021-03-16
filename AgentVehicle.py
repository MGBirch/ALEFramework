from ALEFramework.Agent import Agent
import math
class AgentVehicle(Agent):
    """docstring for AgentVehicle."""

    def __init__(self):
        super().__init__()
        self.MAX_SPEED = 6.28
        self.ds = []
        self.dsNames = ['ds_left', 'ds_right', 'ds_left(1)', 'ds_right(1)']

        for i in range(4):
            self.ds.append(self.robot.getDevice(self.dsNames[i]))
            self.ds[i].enable(self.timestep)

        self.w1 = self.robot.getDevice('wheel1')
        self.w2 = self.robot.getDevice('wheel2')
        self.w3 = self.robot.getDevice('wheel3')
        self.w4 = self.robot.getDevice('wheel4')

        for i in range(4):
            self.w1.setPosition(float('inf'))
            self.w2.setPosition(float('inf'))
            self.w3.setPosition(float('inf'))
            self.w4.setPosition(float('inf'))

    def turnLeft(self):
        self.w1.setVelocity(-0.5 * self.MAX_SPEED)
        self.w4.setVelocity(-0.5 * self.MAX_SPEED)
        self.w2.setVelocity(0.5 * self.MAX_SPEED)
        self.w3.setVelocity(0.5 * self.MAX_SPEED)

    def turnRight(self):
        self.w1.setVelocity(0.5 * self.MAX_SPEED)
        self.w4.setVelocity(0.5 * self.MAX_SPEED)
        self.w2.setVelocity(-0.5 * self.MAX_SPEED)
        self.w3.setVelocity(-0.5 * self.MAX_SPEED)

    def moveForward(self):
        self.w1.setVelocity(0.5 * self.MAX_SPEED)
        self.w4.setVelocity(0.5 * self.MAX_SPEED)
        self.w2.setVelocity(0.5 * self.MAX_SPEED)
        self.w3.setVelocity(0.5 * self.MAX_SPEED)

    def turnSlowLeft(self):
        self.w1.setVelocity(0.1 * self.MAX_SPEED)
        self.w4.setVelocity(0.1 * self.MAX_SPEED)
        self.w2.setVelocity(0.3 * self.MAX_SPEED)
        self.w3.setVelocity(0.3 * self.MAX_SPEED)

    def turnSlowRight(self):
        self.w1.setVelocity(0.3 * self.MAX_SPEED)
        self.w4.setVelocity(0.3 * self.MAX_SPEED)
        self.w2.setVelocity(0.1 * self.MAX_SPEED)
        self.w3.setVelocity(0.1 * self.MAX_SPEED)

    def checkObstacle(self):
        dsValues = []
        for i in range(4):
            dsValues.append(self.ds[i].getValue())

        left_obstacle = dsValues[0] < 1000.0  or dsValues[2] < 1000.0
        right_obstacle = dsValues[1] < 1000.0 or dsValues[3] < 1000.0

        if left_obstacle:
            self.turnRight()
            return True
        elif right_obstacle:
            self.turnLeft()
            return True
        else:
            return False

    def checkRecogniseSource(self):
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

            if angle>0.01:
                check = self.checkObstacle()
                if check is False:
                    self.turnSlowRight()
                    return True
            elif angle<-0.01:
                check = self.checkObstacle()
                if check is False:
                    self.turnSlowLeft()
                    return True
            elif angle <= 0.01 and angle >= -0.01:
                check = self.checkObstacle()
                if check is False:
                    self.moveForward()
                    return True
        return False

    def getWheels(self):
        wheels = [self.w1, self.w2, self.w3, self.w4]
        return wheels
