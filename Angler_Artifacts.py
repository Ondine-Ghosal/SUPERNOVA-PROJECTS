from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE)




right_motor = Motor(Port.E,Direction.CLOCKWISE)

right_attachment = Motor(Port.B)
left_attachment = Motor(Port.F)

robot = DriveBase(left_motor,right_motor, 56, 110)

def right_turn(angle, tspeed=350, thresh= 0.5):
    hub.imu.reset_heading(0)
    wait(100)
    while True:
        speed = angle - hub.imu.heading()
        robot.drive(0, speed * tspeed/100)
        if speed < thresh and speed > 0 - thresh:
            break
        wait(50)
    robot.stop()

def left_turn(angle, tspeed=350, thresh= 1):
    hub.imu.reset_heading(0)
    wait(100)
    while True: 
        heading = hub.imu.heading()
        speed = angle - heading
        robot.drive(0, speed * tspeed/100)  # Same as right_turn, but uses 'turned'
        if speed < thresh and speed > 0-thresh:
            break
        wait(50)
    robot.stop()

def gyro_straight(distance, speed=300):
    robot.reset()
    hub.imu.reset_heading(0)
    while robot.distance() < distance:
        error = hub.imu.heading()
        robot.drive(speed, 6 * (0 - error))
        wait(10)
    robot.stop()

def gyro_reverse(distance, speed=300):
    robot.reset()
    hub.imu.reset_heading(0)
    while 0 - robot.distance() < distance:
        error = hub.imu.heading()
        robot.drive(0-speed, 6 * (0 - error))


        wait(10)
    robot.stop()


# gyro_straight(800)
# left_turn(-90)
# gyro_straight(100)
# robot.turn(-20)
# right_attachment.run_time(2000000, 9000)
# right_turn(15,thresh=5)
# gyro_reverse(50)
# left_turn(-87)
# gyro_straight(120)
# left_turn(-90)
# gyro_straight(15)
# left_attachment.run_angle(-700,1000)
# wait(100)
# gyro_reverse(50)
# left_turn(-90)
# gyro_reverse(500, speed=700)
# right_turn(45, thresh=1)
# gyro_reverse(200)

#robot.turn(-50, wait=False)
#right_attachment.run_time(1000,4000)  

# gyro_straight(915)
# right_turn(87)
# gyro_straight(120)
# robot.turn(-30, wait=False)
# right_attachment.run_time(1300,5000)  
# right_turn(12, thresh= 5)
# gyro_reverse(400)
# left_attachment.run_angle(500, -500)
# left_turn(-90, tspeed=500)
# left_attachment.run_angle(500, -100)
# left_attachment.run_angle(500, 700)
# right_turn(90)
# gyro_straight(200)
# left_turn(-90)

gyro_straight(800)
left_turn(-90, thresh=10)
gyro_straight(50)
left_turn(-30, thresh= 15)
right_attachment.run_time(2000, 4000)
right_turn(10, tspeed=500, thresh = 2)
gyro_reverse(100)
left_turn(-100, thresh = 10)
gyro_reverse(1000, speed=1000)
