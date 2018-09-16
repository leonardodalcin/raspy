from datetime import datetime
from matplotlib import pyplot as plt
import cv2
import os

class Image:
	image = None

	def show(self):
		plt.imshow(self.image, cmap="gray", interpolation='bicubic')
		plt.show()
		return self


	def save(self):
		print("Saving photo")
		now = datetime.now()
		dirName = now.strftime("%d-%m-%Y")
		fileName = now.strftime("%X")
		if not os.path.exists(dirName):
			os.makedirs(dirName)
		cv2.imwrite(dirName + "/" + fileName + ".png", self.image)
		return self


	def threshold(self):
		return cv2.adaptiveThreshold(self.image, 200,
									 adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
									 thresholdType=cv2.THRESH_BINARY,
									 blockSize=51,
									 C=0)

	def rotate(self, degrees):
		(height, width) = self.image.shape[:2]
		center = (height / 2, width / 2)
		rotationMatrix = cv2.getRotationMatrix2D(center, degrees, scale=1)
		self.image = cv2.warpAffine(self.image, rotationMatrix, (width, height))
		return self

	def __init__(self, image=None, path=None):
		if (path):
			self.image = cv2.imread(path, 0)
		else:
			self.image = image
