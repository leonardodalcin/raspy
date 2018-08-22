from IO import IO
from Camera import Camera
print("Vision v0.0.1")
print("Initializing IO")
IO = IO()
print("Initializing Camera")
Camera = Camera()
print("Taking sample photo")
img = Camera.takePhoto()
print(img)

