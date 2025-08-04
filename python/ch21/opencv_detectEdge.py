import cv2

image = cv2.imread("./sample.jpg")

re_image = cv2.resize(image, (800, 600))

edges = cv2.Canny(re_image, 50, 100)


cv2.imshow("Loaded image", edges)
cv2.waitKey(0)  # 0 은 무한 대기
cv2.destroyAllWindows()
