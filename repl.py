from IO import IO
from Camera import Camera
from IO import Input
import RPi.GPIO as GPIO
import time
import code

print("Beholder v0.0.1")
IO = IO()

def callbackFunctionTest(channel):
    print("CALLING CALLBACK FUNCTION SINCE BUTTON IS PRESSED CHANNEL " + str(channel))

Camera = Camera()

sumitomoInput= Input(24, "Sumitomo", callbackFunctionTest)


def repl(IO, Camera, sumitomoInput):
    code.interact(
        local=locals(),
    )

repl(IO, Camera, sumitomoInput)
