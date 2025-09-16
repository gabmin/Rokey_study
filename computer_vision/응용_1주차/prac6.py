import cv2
import sys
import os
from pathlib import Path

folder = "fig"
path = os.path.join(folder, "rudolf.png")
img = cv2.imread(path, cv2.IMREAD_COLOR)

if img is None:
    print("image read failed")
    sys.exit()

h, w = img.shape[:2]

print(f"width = {w}, height = {img.shape[0]}")

cx, cy = w // 2, h // 2

print(cx, cy)
print(img[cx, cy])  # [ 14  14 255]

img[cy:600, cx:600] = (125, 44, 66)

cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)

cv2.imshow("image", img)

while True:
    if cv2.waitKey() == 27:
        break

cv2.destroyAllWindows()
