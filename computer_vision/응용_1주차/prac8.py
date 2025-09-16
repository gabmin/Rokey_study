import cv2
import sys
import os


folder = "fig"
path = os.path.join(folder, "dog.bmp")

img = cv2.imread(path, cv2.IMREAD_COLOR)

if img is None:
    print("image read failed")
    sys.exit()

img1 = img
img2 = img.copy()

dog_eye = img[150:250, 250:500]
cv2.circle(dog_eye, (50, 50), 30, (0, 0, 255), 5)
print(dog_eye.shape)

cv2.namedWindow("dog", cv2.WINDOW_AUTOSIZE)

cv2.imshow("dog", img)
cv2.imshow("dog eye", dog_eye)

while True:
    if cv2.waitKey() == 27:
        break

cv2.destroyAllWindows()
