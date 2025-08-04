import cv2

image = cv2.imread("./people.jpg")

# 처리 속도를 높이기 위해서 그레이 스케일로 변경
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(face_path)

# 얼굴 검출 수행
face = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20, 20),
)

# 검출된 얼굴 주변에 사각형 그리기
for x, y, w, h in face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)


cv2.imshow("Loaded image", image)
cv2.waitKey(0)  # 0 은 무한 대기
cv2.destroyAllWindows()
