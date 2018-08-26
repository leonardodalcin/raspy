from io import BytesIO
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2

class Camera:
	__instance = None
	piCamera = None

	def takePhoto(self):
		rawCapture = PiRGBArray(self.piCamera)
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
			print("Waiting 0.1 seconds for camera warm up")
			Camera.__instance = self
			while True:
				# do nothing
				lal =1




