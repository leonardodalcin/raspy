import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
out26 = GPIO.setup(26, GPIO.OUT)
in19 = GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(26, True)

while 1:
    print(GPIO.input(19))
    if GPIO.input(19):
        print("BUTTON PRESSED")

    time.sleep(0.5)
