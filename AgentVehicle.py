
class AgentVehicle(Agent):
    """docstring for AgentVehicle."""

    def __init__(self, robot):
        super().__init__(pos, robot)
        MAX_SPEED = 6.28
        self.ds = []
        dsNames = ['ds_left', 'ds_right', 'ds_left(1)', 'ds_right(1)']

        for i in range(4):
                self.ds.append(robot.getDevice(dsNames[i]))
                self.ds[i].enable(timestep)

        self.w1 = robot.getDevice('wheel1')
        self.w2 = robot.getDevice('wheel2')
        self.w3 = robot.getDevice('wheel3')
        self.w4 = robot.getDevice('wheel4')

    def turnLeft(self):
        self.w1.setVelocity(-0.5 * MAX_SPEED)
        self.w4.setVelocity(-0.5 * MAX_SPEED)
        self.w2.setVelocity(0.5 * MAX_SPEED)
        self.w3.setVelocity(0.5 * MAX_SPEED)

    def turnRight(self):
        self.w1.setVelocity(0.5 * MAX_SPEED)
        self.w4.setVelocity(0.5 * MAX_SPEED)
        self.w2.setVelocity(-0.5 * MAX_SPEED)
        self.w3.setVelocity(-0.5 * MAX_SPEED)

    def moveForward(self):
        self.w1.setVelocity(0.5 * MAX_SPEED)
        self.w4.setVelocity(0.5 * MAX_SPEED)
        self.w2.setVelocity(0.5 * MAX_SPEED)
        self.w3.setVelocity(0.5 * MAX_SPEED)

    def ifObstacle(self):
        dsValues = []
        for i in range(4):
            dsValues.append(ds[i].getValue())

        left_obstacle = dsValues[0] < 1000.0  or dsValues[2] < 1000.0
        right_obstacle = dsValues[1] < 1000.0 or dsValues[3] < 1000.0

        if left_obstacle:
            self.turnLeft()
            return True
        elif right_obstacle:
            self.turnRight()
            return True
        else:
            returnFalse

    def ifRecogniseSource(self):
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
                self.turnRight()
                return True
            elif angle<-0.01:
                self.turnLeft()
                return True
            elif angle <= 0.01 and angle >= -0.01:
                self.moveForward()
                return True
        return False
