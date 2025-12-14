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

def mission_2(): 
    #Forge, Who lived here, 
    gyro_straight(720)
    while hub.imu.heading() < 35:
        robot.drive(0, 600)
    robot.stop()
    left_turn(-80, tspeed= 700, thresh = 30)
    robot.straight(-200)

    right_turn(42)
    gyro_straight(150)
    right_attachment.run_angle(500, -300)
    gyro_reverse(100)
    right_turn(40, thresh = 20)
    gyro_reverse(260)
    left_turn(-80, thresh=10, tspeed=700)
    gyro_reverse(1300, speed=1000)
    

    '''wait(50)
    gyro_reverse(20)
    right_turn(55, tspeed=300)
    gyro_straight(280)
    right_turn(45)'''

def mission_3():
    #Silo, whats on sale
    robot.reset()
    right_attachment.run_angle(500, 220, wait=False)
    left_attachment.run_angle(500, 220, wait=True)

    gyro_straight(330)
    for i in range(0, 4):
        right_attachment.run_angle(600, -200, wait=False)
        left_attachment.run_angle(600, -200, wait=True)
        right_attachment.run_angle(600, 200, wait=False)
        left_attachment.run_angle(600, 200, wait=True)

    gyro_reverse(300)
    

def mission_1():
    gyro_straight(200)
    left_turn(-45, tspeed=200)
    left_attachment.run_angle(700,-200)
    gyro_straight(230)
    left_attachment.run_angle(700,-300)
    right_turn(7,thresh=3, tspeed=700)
    gyro_reverse(300)
    gyro_straight(3)
    left_attachment.run_angle(700,500)
    left_attachment.run_angle(700, 700, wait=False)
    gyro_straight(17)
    left_turn(-90)
    gyro_straight(110)
    right_turn(88)
    gyro_straight(80)
    gyro_reverse(200, speed=800)
    left_turn(-45)
    gyro_reverse(600, speed=2000)
    # left_attachment.run_angle(1000, 500, wait=False)
    # right_attachment.run_angle(1000, -500, wait=False)
    # gyro_straight(210)
    # left_turn(-45)
    # gyro_straight(135)
    # right_attachment.run_angle(500, -500, wait=False)
    # left_attachment.run_angle(1000, -500, wait=True)
    # left_attachment.run_angle(1000, 1000)
    # gyro_reverse(500)
    # gyro_straight(10)
    # right_attachment.run_angle(1000, 1500)
    # gyro_reverse(500)

def mission_4():
    left_attachment.run_angle(500, -500, wait=False)
    gyro_straight(800)
    left_turn(-90, thresh=10)
    gyro_straight(60)
    left_turn(-40, thresh= 15)
    right_attachment.run_angle(-1000, 4000)
    right_turn(20, thresh = 5)
    gyro_reverse(100)
    left_attachment.run_angle(300, 510, wait=False)
    right_turn(145)
    gyro_straight(139)
    #Start Statue Rebuild
    gyro_straight(20)
    right_turn(30, thresh = 10, tspeed=700)
    left_attachment.run_angle(900,-700)
    gyro_reverse(100)
    left_turn(-62)
    gyro_straight(350, speed=900)
    left_turn(-62)
    gyro_straight(350, speed=900, wait=False)


# left_attachment.run_angle(500, 500, wait=False)
# gyro_straight(800)
# left_turn(-90, thresh=10)
# gyro_straight(50)
# left_turn(-30, thresh= 15)
# right_attachment.run_angle(-1000, 4000)
#     #Angler Artifacts complete
# right_turn(10, thresh = 5)
# gyro_reverse(100)
# left_attachment.run_angle(-300, 500, wait=False)
# right_turn(50)
# gyro_straight(135)
#     #Start Statue Rebuild
# left_attachment.run_angle(500, 1000, wait=False)
# right_turn(20, tspeed=500, thresh=5)
# wait(250)
# gyro_reverse(100)
# left_turn(-60)
# gyro_straight(500, speed=99999)
# left_turn(-35, tspeed=1000, thresh=20)
# gyro_straight(250, speed=99999)


def mission_5():
    # Salvage Operation
    gyro_straight(500, speed=300)
    gyro_reverse(1200, speed=300)
def mission_6():
    # Map Reveal
    gyro_straight(615, speed=400)
    gyro_reverse(100, speed=400)
    gyro_straight(170)
    left_turn(-40, thresh=4, tspeed= 500)
    gyro_straight(165, speed=400)
    wait(100)
    gyro_reverse(10)
    right_attachment.run_angle(500, -1000)
    gyro_straight(30)
    gyro_reverse(180, speed=1000)
    right_turn(55, thresh=10)
    gyro_reverse(1700, speed=800)

def mission_7():
    # Mineshaft Explorer, Statue Rebuild
    gyro_straight(500)
    right_turn(47)
    gyro_straight(260)
    left_turn(-10)
    gyro_reverse(30)
    right_attachment.run_angle(900, 700)
    gyro_reverse(800, speed=900)
def mission_8():
    gyro_straight(370, speed=400)
    right_turn(-9, thresh=3)
    gyro_straight(20, speed=400)
    gyro_reverse(270, speed=550)

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



