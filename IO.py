import RPi.GPIO as GPIO

PanServoPin = 18
TiltServoPin = 23
PWMFrequency = 50

class Servo:
	pwm = None

	def rotate(self, dutyCycle):
		self.pwm.ChangeDutyCycle(dutyCycle)

	def __init__(self, pin):
		GPIO.setup(pin, GPIO.OUT)
		self.pwm = GPIO.PWM(pin, PWMFrequency)

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
			GPIO.setmode(GPIO.BCM)
			self.panServo = Servo(PanServoPin)
			self.tiltServo = Servo(TiltServoPin)
			IO.__instance = self


