from io import BytesIO
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2

class Camera:
	__instance = None
	piCamera = None

	def takePhoto(self):
		rawCapture = PiRGBArray(self.camera)
		self.piCamera.capture(rawCapture, format="bgr")
		image = rawCapture.array
		cv2.imshow("Image", image)
		cv2.waitKey(0)

	@staticmethod
	def getInstance():
		""" Static access method. """
		if Camera.__instance == None:
			Camera()
		return Camera.__instance

	def __init__(self):
		print("Initializing Camera")
		if Camera.__instance != None:
			print("Camera was already initialized, throwing exception")
			raise Exception("This class is a singleton!")
		else:
			print("Setting PiCamera wrapper")
			self.piCamera = PiCamera()
			print("Starting preview")
			self.piCamera.start_preview()
			print("Waiting 2 seconds for camera warmUp")
			time.sleep(0.1)
			Camera.__instance = self



