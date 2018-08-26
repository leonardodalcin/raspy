from IO import IO
from Camera import Camera
import time
import cv2
print("Vision v0.0.1")
print("Initializing IO")
IO = IO()
print("Initializing Camera")
Camera = Camera()
print("Taking sample photo")
img = Camera.takePhoto()
print(img)
while True:
	IO.panServo.rotate(12.5)
	IO.tiltServo.rotate(12.5)
	time.sleep(1)
	IO.panServo.rotate(2)
	IO.tiltServo.rotate(2)
	time.sleep(1)
	IO.panServo.rotate(7.5)
	IO.tiltServo.rotate(7.5)
	time.sleep(1)



