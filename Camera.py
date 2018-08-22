from io import BytesIO
from picamera import PiCamera
from PIL import Image

class Camera:
	__instance = None
	piCamera = None

	def takePhoto(self):
		# Create the in-memory stream
		stream = BytesIO()
		self.piCamera.capture(stream, format='jpeg')
		# "Rewind" the stream to the beginning so we can read its content
		stream.seek(0)
		return Image.open(stream)

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
			Camera.__instance = self



