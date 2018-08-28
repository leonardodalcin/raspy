from io import BytesIO
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
from datetime import datetime
import cv2
import os

class Camera:
	__instance = None
	piCamera = None
	isPreviewing = False
	def savePhoto(self, image):
		print("Saving photo")
		now = datetime.now()
		dirName = now.strftime("%x")
		fileName = now.strftime("%X")
		if not os.path.exists(dirName):
			os.makedirs(dirName)
		cv2.imwrite(image, dirName + fileName)

	def takePhoto(self):
		rawCapture = PiRGBArray(self.piCamera)
		self.piCamera.capture(rawCapture, format="bgr")
		return rawCapture.array

	def togglePreview(self):
		if self.isPreviewing:
			self.piCamera.stop_preview()
		else:
			self.piCamera.start_preview(fullscreen=False, window=(100, 20, 640, 480))
		self.isPreviewing = not self.isPreviewing

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
			self.piCamera.rotation = 180
			Camera.__instance = self




