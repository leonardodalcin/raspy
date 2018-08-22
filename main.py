from IO import IO
import time
IO = IO()

while True:
	IO.getInstance().panServo.rotate(12.5)
	time.sleep(1)
	IO.getInstance().panServo.rotate(0)
	time.sleep(1)
	IO.getInstance().panServo.rotate(7.5)
	time.sleep(1)
