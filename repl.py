from IO import IO
from Camera import Camera
import code

print("Beholder v0.0.1")
print("Initializing IO")
IO = IO()
print("Initializing Camera")
Camera = Camera()

def repl(IO, Camera):
    code.interact(
        local=locals(),
    )

repl(IO, Camera)