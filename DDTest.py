
#!/usr/bin/env python3

from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep
import .contour.py

#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_DRIVE_LEFT =   8	# ENA - H-Bridge enable pin
FORWARD_LEFT_PIN = 20	# IN1 - Forward Drive
REVERSE_LEFT_PIN = 21	# IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT =   9  # ENB - H-Bridge enable pin
FORWARD_RIGHT_PIN = 5	# IN1 - Forward Drive
REVERSE_RIGHT_PIN = 6	# IN2 - Reverse Drive

STANDBY_PIN =       27  # High enables moving

# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)

# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)
forwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)
standby = PWMOutputDevice(STANDBY_PIN)

def allStop():
	forwardLeft.value = False
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = False
	driveLeft.value = 0
	driveRight.value = 0

def forwardDrive():
	print("going forward")
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.7
	driveRight.value = 0.7

def reverseDrive():
	print("going backwards")
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0

def spinLeft():
	print("spin left")
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 1.0
	driveRight.value = 1.0

def SpinRight():
	print("spin right")
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0

def forwardTurnLeft():
	print("forward turn left")
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.2
	driveRight.value = 0.8

def forwardTurnRight():
	print("forward turn right")
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.8
	driveRight.value = 0.2

def reverseTurnLeft():
	print("reverse turn left")
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.2
	driveRight.value = 0.8

def reverseTurnRight():
	print("reverse turn right")
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.8
	driveRight.value = 0.2

def updatePWM(right, left):
	driveLeft.value = left;
	driveRight.value = right;

def main():
	left = 0.5
	right =0.5
	forwardDrive()
	Kp = 1.0
	while(1)
	{
		ratio = contour()
		left += ratio*Kp
		right += -ratio*kp
		updatePWM(right, left)
	}


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
