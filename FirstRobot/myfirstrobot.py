from controller import Robot, DistanceSensor, Motor

# create the Robot instance.
robot = Robot()
MAX_SPEED = 6.28
energy = 100

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

# set the target position of the motors
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# set velocity of motor to 0
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

ps = []
psNames = [
    'ps0', 'ps1'
]

for i in range(2):
        ps.append(robot.getDevice(psNames[i]))
        ps[i].enable(timestep)

while robot.step(timestep) != -1:
    
    psValues = []
    for i in range(2):
        psValues.append(ps[i].getValue())
    
    right_obstacle = psValues[0] > 77.0 
    left_obstacle = psValues[1] > 77.0 0
    
    leftSpeed = 0.5 * MAX_SPEED
    rightSpeed = 0.5 * MAX_SPEED
    
    if left_obstacle:
        #turn the robot to the right
        leftSpeed = 0.5 * MAX_SPEED
        rightSpeed = -0.5 * MAX_SPEED
        print("left")
        
    elif right_obstacle:
        #turn the robot to the left
        leftSpeed = -0.5 * MAX_SPEED
        rightSpeed = 0.5 * MAX_SPEED
        print("right")
        
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)
    pass
    