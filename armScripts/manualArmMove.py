import time
import curses
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    elbowAngle = 70
    handTwistAngle = 80
    shoulderTwistAngle = 100  
    shoulderLiftAngle = 40 
    elbowLiftAngle = 120 
    gripperAngle = 60 

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
            kit.servo[3].angle = elbowAngle        
        else:
            stdscr.addstr(0, 0, f"Elbow angle out of range! Angle: {elbowAngle}")
        
        if 0 < handTwistAngle < 180:
            stdscr.addstr(1, 0, f"Hand twist Angle: {handTwistAngle}")
            kit.servo[4].angle = handTwistAngle        
        else:
            stdscr.addstr(1, 0, f"Hand twist angle out of range! Angle: {handTwistAngle}")

        if 0 < shoulderTwistAngle < 180:  # Set shoulder twist angle
            stdscr.addstr(2, 0, f"Shoulder twist angle: {shoulderTwistAngle}")
            kit.servo[0].angle = shoulderTwistAngle
        else:
            stdscr.addstr(2, 0, f"Shoulder twist angle out of range! Angle: {shoulderTwistAngle}")

        if 0 < shoulderLiftAngle < 180:  # Set shoulder lift angle
            stdscr.addstr(3, 0, f"Shoulder lift angle: {shoulderLiftAngle}")
            kit.servo[1].angle = shoulderLiftAngle
        else:
            stdscr.addstr(3, 0, f"Shoulder lift angle out of range! Angle: {shoulderLiftAngle}")

        if 0 < elbowLiftAngle < 180:  # Set elbow lift angle
            stdscr.addstr(4, 0, f"Elbow lift angle: {elbowLiftAngle}")
            kit.servo[2].angle = elbowLiftAngle
        else:
            stdscr.addstr(4, 0, f"Elbow lift angle out of range! Angle: {elbowLiftAngle}")

        if 0 < gripperAngle < 180:  # Set gripper angle
            stdscr.addstr(5, 0, f"Gripper angle: {gripperAngle}")
            kit.servo[5].angle = gripperAngle
        else:
            stdscr.addstr(5, 0, f"Gripper angle out of range! Angle: {gripperAngle}")

        stdscr.refresh()

        
curses.wrapper(main)
