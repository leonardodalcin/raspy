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
			self.piCamera.start_preview(fullscreen=False, window=(100, 20, 640, 480))
			print("Waiting 0.1 seconds for camera warm up")
			Camera.__instance = self




