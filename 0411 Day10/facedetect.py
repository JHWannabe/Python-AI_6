'''
캐스케이드 분류기: 얼굴 검출

Viola - Jones 얼굴 검출기
- Positive 영상(얼굴 영상)과 Negative 영상(얼굴이 아닌 영상)을 훈련하여 빠르고 정확하게 얼굴 영역을 검출
- 기존에 있는 것보다 15배 빠르게 동작

캐스케이드 분류기(Cascade classifier)
- 일반적인 영상에는 얼굴이 한 두개 있을 뿐, 나머지 영역은 대부분 non-face 영역
- Non-face 영역을 빠르게 skip하도록 다단계 검사 수행

    영상 -> 1단계(특징 1개 사용) -> 2단계(특징 5개 사용) -> 3단계(특징 20개 사용) .. 얼굴 분류
    https://github.com/opencv/opencv/tree/master/data/haarcascades
    cv2.CascadeClassifier(filename)
    filename : xml 파일 이름
    retval : 성공하면 True, 실패하면 False

    cv2.CascadeClassifier.detectMultiScale(image, scaleFactor=None, minNeighbors=None, flags=None, minSize=None, maxSize=None)
    image : 입력 영상
    scaleFactor : 영상 축소 비율, 기본값 1:1
    minneighbors : 얼마나 많은 이웃 사각형이 검출되어야 최종 검출 영역으로 설정할지를 지정, 기본값은 3
    flags : 사용되지 않음
    minSize : 최소 객체 크기 (w,h) 튜플
    maxSize : 최대 객체 크기 (w,h) 튜플
    result : 검출된 객체의 사각형 정보(x, y, w, h)를 담은 numpy.ndarray shape
'''
import cv2

src = cv2.imread('lenna.bmp')
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = classifier.detectMultiScale(src)
for (x, y, w, h) in faces:
    face_img = src[y:y+h, x:x+w]
    cv2.rectangle(src, (x, y, w, h), (255, 0, 255), 2)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()