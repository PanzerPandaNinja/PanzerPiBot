import time
import curses
from adafruit_servokit import ServoKit


kit = ServoKit(channels=16)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    # define servos

    shoulderTwist = kit.servo[0]
    shoulderLift = kit.servo[1]
    elbowLift = kit.servo[2]
    elbow = kit.servo[3]
    handTwist = kit.servo[4]
    gripper = kit.servo[5]

    elbowAngle = 80
    handTwistAngle = 110
    shoulderTwistAngle = 100  
    shoulderLiftAngle = 40 
    elbowLiftAngle = 110 
    gripperAngle = 50 

    old_elbowAngle = 80
    old_handTwistAngle = 110
    old_shoulderTwistAngle = 100
    old_shoulderLiftAngle = 40
    old_elbowLiftAngle = 110
    old_gripperAngle = 50

    stdscr.addstr(0, 0, f"Elbow angle: {elbowAngle}")
    stdscr.addstr(1, 0, f"Hand twist angle: {handTwistAngle}")
    stdscr.addstr(2, 0, f"Shoulder twist angle: {shoulderTwistAngle}")  
    stdscr.addstr(3, 0, f"Shoulder lift angle: {shoulderLiftAngle}")  # Display shoulder lift angle
    stdscr.addstr(4, 0, f"Elbow lift angle: {elbowLiftAngle}")  # Display elbow lift angle
    stdscr.addstr(5, 0, f"Gripper angle: {gripperAngle}")  # Display gripper angle


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
            
        elif key == ord("d"):  # Decrease shoulder twist angle
            shoulderTwistAngle -= 10
        elif key == ord("a"):  # Increase shoulder twist angle
            shoulderTwistAngle += 10
        elif key == ord("w"):  # Increase shoulder lift angle
            shoulderLiftAngle += 10
        elif key == ord("s"):  # Decrease shoulder lift angle
            shoulderLiftAngle -= 10
        elif key == ord("r"):  # Increase elbow lift angle
            elbowLiftAngle += 10
        elif key == ord("f"):  # Decrease elbow lift angle
            elbowLiftAngle -= 10
        elif key == ord("z"):  # Increase gripper angle
            gripperAngle += 10
        elif key == ord("x"):  # Decrease gripper angle
            gripperAngle -= 10
        elif key == ord("q"):
            break

        stdscr.clear()
        
        if 0 < elbowAngle < 180:
            stdscr.addstr(0, 0, f"Elbow Angle: {elbowAngle}")
            #elbow.angle = elbowAngle
            move_servo(elbow, elbowAngle, old_elbowAngle)
            old_elbowAngle=elbowAngle
        else:
            stdscr.addstr(0, 0, f"Elbow angle out of range! Angle: {elbowAngle}")
        
        if 0 < handTwistAngle < 180:
            stdscr.addstr(1, 0, f"Hand twist Angle: {handTwistAngle}")
            #handTwist.angle = handTwistAngle
            move_servo(handTwist, handTwistAngle, old_handTwistAngle)
            old_handTwistAngle=handTwistAngle
        else:
            stdscr.addstr(1, 0, f"Hand twist angle out of range! Angle: {handTwistAngle}")

        if 0 < shoulderTwistAngle < 180:  # Set shoulder twist angle
            stdscr.addstr(2, 0, f"Shoulder twist angle: {shoulderTwistAngle}")
            #shoulderTwist.angle = shoulderTwistAngle
            move_servo(shoulderTwist, shoulderTwistAngle, old_shoulderTwistAngle)
            old_shoulderTwistAngle=shoulderTwistAngle
        else:
            stdscr.addstr(2, 0, f"Shoulder twist angle out of range! Angle: {shoulderTwistAngle}")

        if 0 < shoulderLiftAngle < 180:  # Set shoulder lift angle
            stdscr.addstr(3, 0, f"Shoulder lift angle: {shoulderLiftAngle}")
            #shoulderLift.angle = shoulderLiftAngle
            move_servo(shoulderLift, shoulderLiftAngle, old_shoulderLiftAngle)
            old_shoulderLiftAngle=shoulderLiftAngle
        else:
            stdscr.addstr(3, 0, f"Shoulder lift angle out of range! Angle: {shoulderLiftAngle}")

        if 0 < elbowLiftAngle < 180:  # Set elbow lift angle
            stdscr.addstr(4, 0, f"Elbow lift angle: {elbowLiftAngle}")
            #elbowLift.angle = elbowLiftAngle
            move_servo(elbowLift, elbowLiftAngle, old_elbowLiftAngle)
            old_elbowLiftAngle=elbowLiftAngle
        else:
            stdscr.addstr(4, 0, f"Elbow lift angle out of range! Angle: {elbowLiftAngle}")

        if 0 < gripperAngle < 180:  # Set gripper angle
            stdscr.addstr(5, 0, f"Gripper angle: {gripperAngle}")
            #kit.servo[5].angle = gripperAngle
            move_servo(gripper, gripperAngle, old_gripperAngle)
            old_gripperAngle=gripperAngle

        else:
            stdscr.addstr(5, 0, f"Gripper angle out of range! Angle: {gripperAngle}")

        stdscr.refresh()



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
