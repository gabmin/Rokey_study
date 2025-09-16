import numpy as np
import cv2

img = np.ones((600, 400, 3), dtype="uint8") * 255
img2 = np.zeros((600, 400, 3), dtype="uint8")
img3 = np.full((600, 400, 3), (255, 0, 255), np.uint8)

cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)


cv2.waitKey()
cv2.destroyAllWindows()
