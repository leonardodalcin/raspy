from IO import IO
from Camera import Camera
import cv2
print("Vision v0.0.1")
print("Initializing IO")
IO = IO()
print("Initializing Camera")
Camera = Camera()
print("Taking sample photo")
img = Camera.takePhoto()
print(img)
cv2.waitKey(0)


