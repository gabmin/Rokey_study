import cv2

image = cv2.imread("./sample.jpg")

re_image = cv2.resize(image, (800, 600))

blur = cv2.GaussianBlur(re_image, (25, 25), 0)


cv2.imshow("Loaded image", blur)
cv2.waitKey(0)  # 0 은 무한 대기
cv2.destroyAllWindows()
