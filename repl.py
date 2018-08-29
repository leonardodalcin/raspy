from IO import IO
from Camera import Camera
from IO import Input
import RPi.GPIO as GPIO
import time
import code

print("Beholder v0.0.1")
print("Initializing IO")
IO = IO()

print("Initializing Camera")
Camera = Camera()
print("Initializing external signal input")
sumitomoInput= Input(24, "Sumitomo", Camera.takePhoto)
while 1:
    if GPIO.input(24):
        print("BUTTON PRESSED")
        time.sleep(1)

# def repl(IO, Camera, sumitomoInput):
#     code.interact(
#         local=locals(),
#     )
#
# repl(IO, Camera, sumitomoInput)
