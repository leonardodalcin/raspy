from IO import IO
from Camera import Camera
from IO import Input
from Image import Image
import code

print("Beholder v0.0.1")
IO = IO()

def takePhoto(channel):
    print("CALLING CALLBACK FUNCTION SINCE BUTTON IS PRESSED CHANNEL " + str(channel))
    Image(Camera.takePhoto()).save()

Camera = Camera()

sumitomoInput= Input(24, "Sumitomo", takePhoto)


def repl(IO, Camera, sumitomoInput):
    code.interact(
        local=locals(),
    )

repl(IO, Camera, sumitomoInput)
