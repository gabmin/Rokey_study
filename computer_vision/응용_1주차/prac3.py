import os
import sys

import matplotlib.pyplot as plt
import cv2

folder = "fig"
path = os.path.join(folder, "lenna.png")

img = cv2.imread(path, cv2.IMREAD_COLOR)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

if img is None:
    print("No image")
    sys.exit()


plt.figure(figsize=(10, 3))
plt.subplot(141), plt.imshow(img), plt.axis("off"), plt.title("bgr")
plt.subplot(142), plt.imshow(img_rgb), plt.axis("off"), plt.title("rgb")
plt.subplot(143), plt.imshow(img_gray, cmap="gray"), plt.axis("off"), plt.title(
    "gray"
)  # pseudo-color
plt.subplot(144), plt.imshow(img_hsv), plt.axis("off"), plt.title("hsv")

plt.show()
