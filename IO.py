import RPi.GPIO as GPIO

PanServoPin = 18
TiltServoPin = 23
PWMFrequency = 50
InitialDutyCycle = 7.5
class Servo:
	pwm = None
	pin = None

	def rotate(self, dutyCycle):
		print("Rotating servo to duty cycle " + str(dutyCycle))
		self.pwm = GPIO.PWM(self.pin, PWMFrequency)
		self.pwm.start(dutyCycle)

	def __init__(self, pin):
		print("Initializing Servo on pin " + str(pin) + " with frequency " + str(PWMFrequency) + "Hz")
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)
		self.rotate(InitialDutyCycle)

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
		print("Initializing IO")
		if IO.__instance != None:
			print("IO was already initialized, throwing exception")
			raise Exception("This class is a singleton!")
		else:
			print("Setting board mode")
			GPIO.setmode(GPIO.BCM)
			print("Creating pan servo on pin " + str(PanServoPin))
			self.panServo = Servo(PanServoPin)
			print("Creating tilt servo on pin " + str(TiltServoPin))
			self.tiltServo = Servo(TiltServoPin)
			IO.__instance = self


