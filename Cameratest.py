from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2



camera = PiCamera()
rawCapture = PiRGBArray(camera)
camera.rotation = 180
camera.capture(rawCapture, format="bgr")
img = rawCapture.array
cv2.imwrite("test.png", img)