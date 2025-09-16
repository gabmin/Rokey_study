import os
from pathlib import Path
import cv2

folder = "fig"

img_list = os.listdir(Path(folder, "images"))

print(img_list)

img_files = []  # list

for i in img_list:
    img_dir = Path(folder, "images", i)  # python string
    img_files.append(img_dir)

print(img_files)

cv2.namedWindow("folder images", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("folder images", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

idx = 0
while True:
    for i in img_files:

        img = cv2.imread(img_files[idx], cv2.IMREAD_COLOR)
        cv2.imshow("folder images", img)

        if cv2.waitKey(3000) == 27:
            break

        idx += 1

        if idx >= len(img_files):
            idx = 0

cv2.destroyAllWindows()
