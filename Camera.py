from picamera import PiCamera
from picamera.array import PiRGBArray

class Camera:
	__instance = None
	piCamera = None
	isPreviewing = False

	def takePhoto(self):
		print("Taking photo")
		rawCapture = PiRGBArray(self.piCamera)
		self.piCamera.capture(rawCapture, format="bgr")
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
			self.piCamera = PiCamera(resolution=(1920, 1080))
			self.piCamera.rotation = 180
			Camera.__instance = self




