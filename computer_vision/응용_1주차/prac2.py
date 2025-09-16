import os
import cv2
import sys

folder = "fig"
path = os.path.join(folder, "autumn.jpg")

img = cv2.imread(path, cv2.IMREAD_REDUCED_COLOR_4)


if img is None:
    print("error")
    sys.exit()

h, w = img.shape[:2]
print(f"Width x Height = {w} x {h}")

# waitKey([, delay]) -> retval
# delay: Delay in milliseconds. 0 is the special value that means "forever"
# cv2.waitKey() -> ASCII code
# retval

cv2.namedWindow("Autumn", flags=cv2.WINDOW_AUTOSIZE)
cv2.imshow("Autumn", img)

while True:
    if cv2.waitKey() == 27:  # ESC
        break

cv2.destroyAllWindows()
