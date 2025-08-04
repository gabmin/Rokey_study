import cv2

image = cv2.imread("./sample.jpg")

re_image = cv2.resize(image, (800, 600))

colored_image = cv2.cvtColor(re_image, cv2.COLOR_BGR2RGB)

cv2.imshow("Loaded image", colored_image)
cv2.waitKey(0)  # 0 은 무한 대기
cv2.destroyAllWindows()
