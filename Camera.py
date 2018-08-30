from picamera import PiCamera
from picamera.array import PiRGBArray
from datetime import datetime
import cv2
import os

class Camera:
	__instance = None
	piCamera = None
	isPreviewing = False

	def save(self):
		print("Saving photo")
		now = datetime.now()
		dirName = now.strftime("%d-%m-%Y")
		fileName = now.strftime("%X")
		if not os.path.exists(dirName):
			os.makedirs(dirName)
		cv2.imwrite(dirName + "/" + fileName + ".png", self.image)

	def takePhoto(self):
		print("Taking photo")
		rawCapture = PiRGBArray(self.piCamera)
		self.piCamera.capture(rawCapture, format="bgr")
		self.save(rawCapture.array)
		return rawCapture.array

	def togglePreview(self):
		print("Toggling preview")

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




