from controller import Robot, DistanceSensor, Motor, Camera, CameraRecognitionObject, Supervisor, Node
# create the Robot instance.
robot = Supervisor()
MAX_SPEED = 6.28
energy = 10000

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

battery = robot.getFromDef('battery')

car = robot.getFromDef('car')
batteryPos = battery.getPosition()

w1 = robot.getDevice('leg1')


# set the target position of the wheels
w1.setPosition(float('inf'))


# set velocity of wheels to 0
w1.setVelocity(0.5*MAX_SPEED)

while robot.step(timestep) != -1:
    w1.setVelocity(0.5*MAX_SPEED)