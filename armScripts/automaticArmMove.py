import time
import curses
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    elbowAngle = 80
    handTwistAngle = 110
    shoulderTwistAngle = 100  
    shoulderLiftAngle = 40 
    elbowLiftAngle = 110 
    gripperAngle = 50 

    old_elbowAngle = 0
    old_handTwistAngle = 0
    old_shoulderTwistAngle = 0
    old_shoulderLiftAngle = 0
    old_elbowLiftAngle = 0
    old_gripperAngle = 0


    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            handTwistAngle -= 10
        elif key == curses.KEY_DOWN:
            handTwistAngle += 10
        elif key == curses.KEY_LEFT:
            elbowAngle += 10
        elif key == curses.KEY_RIGHT:
            elbowAngle -= 10
            

        elif key == ord("s"):  # Decrease shoulder lift angle
            smoothMove()

        elif key == ord("q"):
            break

        stdscr.refresh()

def smoothMove():
    for angle in range(80, 141):  # Loop 
        armTwist = angle
        armAngle = angle
        print(f"armTwist: {armTwist}, armAngle: {armAngle}")
        kit.servo[3].angle = armAngle
        kit.servo[5].angle = armTwist
        kit.servo[2].angle = armAngle
        kit.servo[1].angle = armTwist

        time.sleep(0.04)

    for angle in range(139, 80, -1):  # Loop back 
        armTwist = angle
        armAngle = angle
        print(f"armTwist: {armTwist}, armAngle: {armAngle}")
        kit.servo[3].angle = armAngle
        kit.servo[5].angle = armTwist
        kit.servo[2].angle = armAngle
        kit.servo[1].angle = armTwist

        time.sleep(0.04)



def move_servo(servoNr, new_angle, old_angle):
    if new_angle > old_angle:
        for angle in range(old_angle, new_angle + 1):
            kit.servo[servoNr].angle = angle
            time.sleep(0.04)
    else:
        for angle in range(old_angle, new_angle - 1, -1):
            kit.servo[servoNr].angle = angle
            time.sleep(0.04)

curses.wrapper(main)
