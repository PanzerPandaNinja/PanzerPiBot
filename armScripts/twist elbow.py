import time
import curses
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    elbowAngle = 0
    servo4Angle = 0
    stdscr.addstr(0, 0, f"Elbow Angle: {elbowAngle}")
    stdscr.addstr(1, 0, f"Servo 4 Angle: {servo4Angle}")

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            elbowAngle += 10
        elif key == curses.KEY_DOWN:
            elbowAngle -= 10
        elif key == curses.KEY_LEFT:
            servo4Angle -= 10
        elif key == curses.KEY_RIGHT:
            servo4Angle += 10
        elif key == ord("q"):
            break

        stdscr.clear()
        
        if 0 < elbowAngle < 180:
            stdscr.addstr(0, 0, f"Elbow Angle: {elbowAngle}")
            kit.servo[3].angle = elbowAngle        
        else:
            stdscr.addstr(0, 0, f"Elbow Angle out of range! Angle: {elbowAngle}")
        
        if 0 < servo4Angle < 180:
            stdscr.addstr(1, 0, f"Servo 4 Angle: {servo4Angle}")
            kit.servo[4].angle = servo4Angle        
        else:
            stdscr.addstr(1, 0, f"Servo 4 Angle out of range! Angle: {servo4Angle}")
        
        stdscr.refresh()

curses.wrapper(main)
