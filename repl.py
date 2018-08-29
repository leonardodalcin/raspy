from IO import IO
from Camera import Camera
from IO import Input
import code

print("Beholder v0.0.1")
print("Initializing IO")
IO = IO()

print("Initializing Camera")
Camera = Camera()
print("Initializing external signal input")
sumitomoInput= Input(19, "Sumitomo", Camera.takePhoto)

def repl(IO, Camera, sumitomoInput):
    code.interact(
        local=locals(),
    )

repl(IO, Camera, sumitomoInput)