import RPi.GPIO as GPIO

PanServoPin = 18
TiltServoPin = 23
PWMFrequency = 50

class PanServo:
	pwm = None

	def rotate(self, dutyCycle):
		self.pwm.ChangeDutyCycle(dutyCycle)

	def __init__(self):
		GPIO.setup(PanServoPin, GPIO.OUT)
		pwm = GPIO.PWM(PanServoPin, PWMFrequency)

class TiltServo:
	pwm = None

	def rotate(self, dutyCycle):
		self.pwm.ChangeDutyCycle(dutyCycle)

	def __init__(self):
		GPIO.setup(TiltServoPin, GPIO.OUT)
		pwm = GPIO.PWM(PanServoPin, PWMFrequency)



class IO:
	__instance = None
	panServo = None
	tiltServo = None

	@staticmethod
	def getInstance():
		""" Static access method. """
		if IO.__instance == None:
			IO()
		return IO.__instance

	def __init__(self):
		if IO.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			IO.__instance = self
			GPIO.setmode(GPIO.BCM)
			self.panServo = PanServo()
			self.tiltServo = TiltServo()

