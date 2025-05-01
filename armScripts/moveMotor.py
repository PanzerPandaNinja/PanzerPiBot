from dcmotor import DCMotor

motor = DCMotor(pina=8, pinb=9, freq=50, fast=True)

motor.speed(-50)  # Set speed (range: -100 to 100)
sleep(2)  # Wait for 2 seconds
motor.stop()  # Stop the motor
