from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2



camera = PiCamera()
rawCapture = PiRGBArray(camera)
camera.rotation = 180
camera.capture(rawCapture, format="bgr")
img = rawCapture.array
# 180 degrees
(h, w) = img.shape[:2
                    ]
# calculate the center of the image
center = (w / 2, h / 2)
M = cv2.getRotationMatrix2D(center, 180, 1)

rotated180 = cv2.warpAffine(img, M, (w, h))
cv2.imwrite("test.png", img)