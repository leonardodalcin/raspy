from IO import IO

IO = IO()

while True:
	IO.panServo.rotate(12.5)
	IO.panServo.rotate(0)
	IO.panServo.rotate(7.5)