import RPi.GPIO as GPIO
import time
from time import sleep
from picamera import PiCamera

photoNumber = 1
isCameraInUse = False
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)


GPIO.setmode(GPIO.BCM)
out26 = GPIO.setup(26, GPIO.OUT)
in19 = GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(26, True)

while 1:
    if GPIO.input(19) and not isCameraInUse:
        isCameraInUse = True
        print("BUTTON PRESSED")
        start = time.clock()
        camera.capture('foo' + str(photoNumber) + '.jpg')
        print("TOOK AND SAVED PHOTO IN " + str(time.clock() - start))
        photoNumber += 1
        isCameraInUse = not isCameraInUse

