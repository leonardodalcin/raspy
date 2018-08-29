from datetime import datetime
import cv2
import os

class Image:
	image = None

	def save(self):
		print("Saving photo")
		now = datetime.now()
		dirName = now.strftime("%d-%m-%Y")
		fileName = now.strftime("%X")
		if not os.path.exists(dirName):
			os.makedirs(dirName)
		cv2.imwrite(dirName + "/" + fileName + ".png", self.image)

	def threshold(self):
		return cv2.adaptiveThreshold(self.image, 200,
									 adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
									 thresholdType=cv2.THRESH_BINARY,
									 blockSize=51,
									 C=0)

	def __init__(self, image):
		self.image = image
