import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.OUT)

for i in range(50):
    GPIO.output(26, True)
    time.sleep(1)
    GPIO.output(26, False)
    time.sleep(1)
