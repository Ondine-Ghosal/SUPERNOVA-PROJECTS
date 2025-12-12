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
    #Forge, Who lived here, 
    gyro_straight(740)
    left_turn(-35, thresh = 20)
    gyro_reverse(15)
    right_turn(20)
    gyro_reverse(115)
    right_turn(25)
    wait(100)
    left_attachment.run_angle(300,-605,)
    gyro_straight(90)
    wait(100)
    left_attachment.run_angle(500, 900)
    gyro_reverse(60)
    left_turn(45)
    gyro_straight(700)

    '''wait(50)
    gyro_reverse(20)
    right_turn(55, tspeed=300)
    gyro_straight(280)
    right_turn(45)'''

def mission_2():
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
    

def mission_3():
    left_attachment.run_angle(700,-200, wait=False)
    gyro_straight(200)
    left_turn(-50, thresh =5, tspeed=500)
    gyro_straight(230)
    left_attachment.run_angle(700,-300)
    robot.turn(-10)
    gyro_reverse(300)
    gyro_straight(5)
    left_attachment.run_angle(700,500)
    left_attachment.run_angle(700, 500, wait=False)
    gyro_straight(10)
    left_turn(-90)
    gyro_straight(100)
    right_turn(85)
    gyro_straight(150)
    gyro_reverse(900, speed=800)

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
    gyro_straight(500, speed=300)
    gyro_reverse(500, speed=300)
def mission_6():
    # Map Reveal
    gyro_straight(630, speed=400)
    gyro_reverse(100, speed=500)
    gyro_straight(125)
    left_turn(-37, thresh=4, tspeed= 500)
    gyro_straight(165, speed=400)
    wait(100)
    gyro_reverse(10)
    right_attachment.run_angle(500, -1000)
    gyro_reverse(130, speed=1000)
    right_turn(55, thresh=10)
    gyro_reverse(700, speed=800)

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