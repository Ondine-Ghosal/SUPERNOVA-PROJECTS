from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
d_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

def forward(speed):
    while True:
        d_base.drive(speed, 2 * (0 - hub.imu.heading()))
        print(hub.imu.heading())

def right_turn(angle):
    print(hub.imu.heading())
    hub.imu.reset_heading(0)
    while True:
        d_base.drive(0, 2 * (angle - hub.imu.heading()))
        if hub.imu.heading() != angle:
            wait(50)
        d_base.stop()
    print(hub.imu.heading())

def left_turn(angle):
    print(hub.imu.heading())
    hub.imu.reset_heading(0)
    a = -1 * angle
    while True:
        d_base.drive(0, 2 * (a - hub.imu.heading()))
        if hub.imu.heading != a:
            wait(50)
        d_base.stop()
    print(hub.imu.heading())

left_turn(90)
