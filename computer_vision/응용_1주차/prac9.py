import cv2
import sys
from pathlib import Path


folder = "fig"

src = cv2.imread(Path(folder, "airplane.bmp"), cv2.IMREAD_COLOR)
mask = cv2.imread(Path(folder, "mask_plane.bmp"), cv2.IMREAD_GRAYSCALE)
dst = cv2.imread(Path(folder, "beach.bmp"))

h, w = src.shape[:2]

dsp_crop = dst[100 : 100 + h, 400 : 400 + w]


if src is None or mask is None or dst is None:
    print("Images read failed")
    sys.exit()

cv2.copyTo(src, mask, dsp_crop)

cv2.namedWindow("dst", cv2.WINDOW_NORMAL)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()
