from IO import IO
from Camera import Camera
from IO import Input
from IO import OutputClock
from Image import Image
import code

print("Beholder v0.0.1")
IO = IO()
Camera = Camera()


def takePhoto():
	Image(Camera.takePhoto()).rotate(90).save()

sumitomoInput = Input(24, "Sumitomo", takePhoto)
clockTestOutput = OutputClock(25, "Fake Signal", 0.1)


def repl(IO, Camera, takePhoto):
	code.interact(
		local=locals(),
	)


repl(IO, Camera, takePhoto)
