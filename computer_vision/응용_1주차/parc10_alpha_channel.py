import cv2
import sys
from pathlib import Path

folder = "fig"

src = cv2.imread(Path(folder, "sunglass.png"), cv2.IMREAD_UNCHANGED)
dst = cv2.imread(Path(folder, "dog.bmp"), cv2.IMREAD_COLOR)

if src is None:
    print("Images read failed")
    sys.exit()

mask = src[:, :, -1]  # mask
sunglass = src[:, :, :-1]  # bgr

dog_eye = dst[150:250, 250:500]

h, w = dog_eye.shape[:2]
src = cv2.resize(src, (w, h))

cv2.copyTo(sunglass, mask, dog_eye)

cv2.imshow("src", src)
cv2.imshow("mask", mask)
cv2.imshow("sunglass", dst)

cv2.waitKey()
cv2.destroyAllWindows()
