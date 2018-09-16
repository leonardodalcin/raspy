from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2



camera = PiCamera()
rawCapture = PiRGBArray(camera)
camera.capture(rawCapture, format="bgr")
img = rawCapture.array
# 180 degrees

cv2.imwrite("test.png", rotated180)