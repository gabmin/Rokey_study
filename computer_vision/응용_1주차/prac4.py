from urllib import request
import numpy as np
import cv2

url = "https://image.artbox.co.kr/upload/C00001/goods/800_800/179/241101006087179.jpg?s=/goods/org/179/241101006087179.jpg"
# url = "https://i.ytimg.com/vi/VCUT4Hqy5lA/maxresdefault.jpg"
source = request.urlopen(url).read()  # bytes
# print(type(source))
# print(source)

image = np.array(bytearray(source), dtype=np.uint8)
print("image shape = ", image.shape)  # (101968,)

image = cv2.imdecode(image, cv2.IMREAD_COLOR)
cv2.imwrite("Charistmas.png", image)

# cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img", image)

cv2.waitKey()
cv2.destroyAllWindows()
