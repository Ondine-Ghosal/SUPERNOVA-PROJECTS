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

def gyro_straight(distance, speed=300, thresh= 0):
    robot.reset()
    hub.imu.reset_heading(0)
    while robot.distance() < distance:
        error = hub.imu.heading()
        if error > thresh or error < 0 - thresh:
            robot.drive(speed, 6 * (0 - error))
        wait(10)
    robot.stop()

def gyro_reverse(distance, speed=300, thresh= 0):
    robot.reset()
    hub.imu.reset_heading(0)
    while 0 - robot.distance() < distance:
        error = hub.imu.heading()
        if error > thresh or error < 0 - thresh:
            robot.drive(0-speed, 6 * (0 - error))


        wait(10)
    robot.stop()



#gyro_reverse(100)

def mission_1(): 
    # What's on sale tip the scale
    gyro_straight(200)
    left_turn(-46)
    gyro_straight(200)
    left_attachment.run_angle(700, -500)
    gyro_reverse(10)
    # right_turn(5, thresh =1)
    gyro_reverse(300, speed=200)
    left_attachment.run_angle(700, 300, wait = False)
    gyro_straight(20)
    gyro_reverse(100)
    left_turn(-45, thresh = 2)
    gyro_straight(420)
    right_turn(80, thresh = 2)
    gyro_straight(70)
    gyro_reverse(70, speed=200)
    right_turn(100, thresh = 5, tspeed=500)
    gyro_straight(500, speed=1000)

def mission_2(): 
    print("to be done")
    # Forge, Who Lived Here, Heavy Lifting
    # TO BE DONE
def mission_3():
    #Silo, whats on sale
    right_attachment.run_angle(500, 120, wait=False)
    left_attachment.run_angle(500, 120, wait=True)

    gyro_straight(400)
    for i in range(0, 4):
        right_attachment.run_angle(500, -120, wait=False)
        left_attachment.run_angle(500, -120, wait=True)
        right_attachment.run_angle(500, 120, wait=False)
        left_attachment.run_angle(500, 120, wait=True)

    gyro_reverse(20)
    left_turn(-60)
    gyro_straight(200)
    left_turn(-160)
    gyro_straight(500, speed=1000)

def mission_4():
    # Angler Artifacts
    gyro_straight(800)
    left_turn(-90, thresh=10)
    gyro_straight(50)
    left_turn(-30, thresh= 15)
    right_attachment.run_time(2000, 4000)
    right_turn(10, tspeed=500, thresh = 2)
    gyro_reverse(100)
    left_turn(-100, thresh = 10)
    gyro_reverse(1000, speed=1000)
def mission_5():
    # Salvage Operation
    gyro_straight(630, 200)
    right_attachment.run_angle(700, -300)
    right_attachment.run_angle(700, 300)
    robot.drive()
def mission_6():
    # Map Reveal
    gyro_straight(235)
    left_turn(-90)
    gyro_straight(615)

    left_turn(-50)
    gyro_straight(300, speed=200)
    gyro_reverse(25, speed=200)
    right_attachment.run_angle(500, 1000,wait=False)
    gyro_straight(35, speed=400)
    gyro_reverse(50)
    right_turn(80, thresh=30)
    gyro_reverse(900, speed=700)

def mission_7():
    # Mineshaft Explorer, Statue Rebuild
    left_attachment.run_angle(700, 50, wait=False)
    gyro_straight(790)
    right_turn(90)
    gyro_straight(110)
    right_turn(51)
# gyro_reverse(20)
    left_attachment.run_angle(900,-330)
    gyro_straight(90)
    left_attachment.run_angle(900,150)
    wait(500)
    left_turn(-23, thresh = 5, tspeed=400)
    left_attachment.run_angle(900,150)
    gyro_reverse(230)
    left_attachment.run_angle(700,-250)
    left_turn(-45, thresh = 5)
    left_attachment.run_angle(700,600)
    gyro_reverse(100)
    right_turn(100, thresh =10, tspeed=500)
    gyro_straight(700, speed=1200)
def mission_8():
    gyro_straight(210)
    right_turn(45)
    gyro_straight(200)
    gyro_reverse(200)
cm = 0
def make_decision():
    global cm
    print(cm)
    exec(f"mission_{cm}()")

while True:
    pressed = hub.buttons.pressed()
    hub.display.char(str(cm))
    if Button.LEFT in pressed:
        cm -= 1
        if cm > 9 or cm < 0: cm = 0
    if Button.RIGHT in pressed:
        cm += 1
        if cm > 9 or cm < 0: cm = 0
    if Button.BLUETOOTH in pressed:
        make_decision()
    wait(150)



