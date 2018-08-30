import RPi.GPIO as GPIO
import time

PanServoPin = 18
TiltServoPin = 23
SumitomoPin = 24
PWMFrequency = 50
InitialDutyCycle = 7.5


class OutputClock:
	pin = None
	frequency = None
	pwm = None
	name = None

	def stop(self):
		self.pwm.stop()

	def __init__(self, pin, name, frequency):
		print("Initializing clock on pin " + str(pin) + " with output frequency of " + str(frequency) + "Hz")
		self.pin = pin
		self.frequency = frequency
		self.name = name
		self.pwm = GPIO.PWM(self.pin, frequency)
		self.pwm.start()


class Input:
	function = None
	pin = None
	name = None

	def __init__(self, pin, name, function):
		print("Initializing Input Listener on pin " + str(pin) + " named: " + name)
		self.pin = pin
		self.name = name
		GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		self.function = function
		GPIO.add_event_detect(pin, GPIO.RISING, callback=self.function, bouncetime=300)


class Servo:
	pwm = None
	pin = None

	def rotate(self, dutyCycle):
		print("Rotating servo to duty cycle " + str(dutyCycle))
		self.pwm = GPIO.PWM(self.pin, PWMFrequency)
		self.pwm.start(dutyCycle)
		time.sleep(0.5)
		self.pwm.stop()

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

	def addEventListner(self, pin, name, function):
		print("Adding event listener named " + name + " on pin " + str(pin))
		return Input(pin, name, function)

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
