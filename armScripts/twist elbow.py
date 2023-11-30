import time
import curses
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    elbowAngle = 0
    handTwistAngle = 0
    stdscr.addstr(0, 0, f"Elbow angle: {elbowAngle}")
    stdscr.addstr(1, 0, f"Hand twist angle: {handTwistAngle}")

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            elbowAngle += 10
        elif key == curses.KEY_DOWN:
            elbowAngle -= 10
        elif key == curses.KEY_LEFT:
            handTwistAngle -= 10
        elif key == curses.KEY_RIGHT:
            handTwistAngle += 10
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
        
        stdscr.refresh()

curses.wrapper(main)
