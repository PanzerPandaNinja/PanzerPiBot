import time
import curses
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    shoulderTwist = kit.servo[0]
    shoulderLift = kit.servo[1]
    elbowLift = kit.servo[2]
    elbow = kit.servo[3]
    handTwist = kit.servo[4]
    gripper = kit.servo[5]


    shoulderTwistAngle = 100  
    shoulderLiftAngle = 40 
    elbowAngle = 80
    handTwistAngle = 110
    elbowLiftAngle = 110 
    gripperAngle = 50 


    # Set all joints to their respective angles
    shoulderTwist.angle = shoulderTwistAngle
    old_shoulderTwistAngle = shoulderTwistAngle
    shoulderLift.angle = shoulderLiftAngle
    old_shoulderLiftAngle = shoulderLiftAngle
    elbowLift.angle = elbowLiftAngle
    old_elbowLiftAngle = elbowLiftAngle
    elbow.angle = elbowAngle
    old_elbowAngle = elbowAngle
    handTwist.angle = handTwistAngle
    old_handTwistAngle = handTwistAngle
    gripper.angle = gripperAngle
    old_gripperAngle = gripperAngle



    while True:
        key = stdscr.getch()

        if key == ord("s"):  # Decrease shoulder lift angle
            smoothMove(elbow, old_elbowAngle)

        elif key == ord("q"):
            break

        stdscr.refresh()

def smoothMove(elbow, old_elbowAngle):
    for angle in range(80, 141):  # Loop 
        

        print(f"elbow: {angle}")
        move_servo(elbow, angle, old_elbowAngle)
        old_elbowAngle = angle

        time.sleep(0.04)

    for angle in range(139, 80, -1):  # Loop back 
        print(f"elbow: {angle}")    
        move_servo(elbow, angle, old_elbowAngle)
        old_elbowAngle = angle

        time.sleep(0.04)



def move_servo(joint, new_angle, old_angle):
    if new_angle > old_angle:
        for angle in range(old_angle, new_angle + 1):
            joint.angle = angle
            time.sleep(0.03)
    else:
        for angle in range(old_angle, new_angle - 1, -1):
            joint.angle = angle
            time.sleep(0.03)

curses.wrapper(main)
