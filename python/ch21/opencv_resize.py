import cv2

image = cv2.imread("./sample.jpg")
re_image = cv2.resize(image, (800, 600))

h, w = re_image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 45, 1)
rotated = cv2.warpAffine(re_image, M, (w, h))

cv2.imshow("image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
