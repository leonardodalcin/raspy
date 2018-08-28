from IO import IO
from Camera import Camera
import code

print("Beholder v0.0.1")
print("Initializing IO")
IO = IO()
print("Initializing Camera")
Camera = Camera()

while 1:
	if GPIO.input(19) and not isCameraInUse:
		print("BUTTON PRESSED")
		start = time.clock()
		camera.capture('foo' + str(photoNumber) + '.jpg')
		print("TOOK AND SAVED PHOTO IN " + str(time.clock() - start))
		photoNumber += 1
		isCameraInUse = not isCameraInUse
def repl(IO, Camera):
    code.interact(
        local=locals(),
    )

repl(IO, Camera)