import cv2
from Image import Image
img = Image(cv2.imread("mold-example.jpg", 0))
cv2.imshow("test1",img.image)

cv2.imshow("test",img.threshold())
cv2.waitKey(0)
