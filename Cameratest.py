from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.capture('foo.jpg')