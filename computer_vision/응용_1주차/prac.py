import sys

import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

import cv2

print(cv2.__version__)

folder = "fig"
img1 = Path(folder, "dog.bmp")

img = cv2.imread(img1, flags=cv2.IMREAD_COLOR)

# cv2.imread(filename. flags = None) -> retval
# flags:
# cv2.IMREAD_COLOR: BGR color로 읽기
# cv2.IMREAD_GRAYSCALE: 그레이 color로 읽기
# cv2.IMREAD_UNCHANGED: 파일 속성대로 읽기
# cv2.IMREAD_REDUCED_GRAYSCALE_2
# cv2.IMREAD_REDUCED_COLOR_2

# retval: numpy.ndarray로 반환

if img is None:
    print("image read failed")
    sys.exit()

print("image type =", type(img))
print("image shape =", img.shape)  # (row, column, bgr)
print("image dtype =", img.dtype)

# cv2.namedWindow(winname, flags = None) -> None

# winname: 창 이름
# flags:
# cv2.WINDOW_NORMAL: 영상크기를 창 크기에 맞게 지정
# cv2.WINDOW_AUTOSIZE: 창크기를 영상 크기에 맞게 변경

cv2.namedWindow("dog", flags=cv2.WINDOW_AUTOSIZE)

# cv2.imwrite(filename, mat) -> None
# filename: 저장할 이름
# mat: numpy.ndarray (default = uint8)

# uint16, int32의 경우 255로 나누어서 출력
# float32, float64의 경우 0 ~ 1로 만든 후 행렬값에 255를 곱해서 출력

img_resize = cv2.resize(img, (320, 240))

cv2.imwrite("img_resize.png", img_resize)

cv2.imshow("dog", img)
cv2.imshow("dog2", img_resize)
cv2.waitKey()
cv2.destroyAllWindows()
