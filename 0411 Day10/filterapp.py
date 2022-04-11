'''
카메라 입력 영상에서 얼굴을 검출하여 그래픽을 합성하는 프로그램

구현할 기능
- 카메라 입력 영상에서 얼굴 & 눈 검출하기
- 눈 위치와 맞게 투명한 PNG 파일 합성하기
- 합성된 결과를 동영상으로 저장하기

캐스케이드 분류기 사용
xml : https://github.com/opencv/opencv/tree/master/data/haarcascades
얼굴 검출 xml : haarcascade_frontalface_alt2.xml
눈 검출 xml : haarcascade_eye.xml
'''
import sys
import numpy as np
import cv2

def overlay(img, glasses, pos):
    sx = pos[0]
    ex = pos[0] + glasses.shape[1]
    sy = pos[1]
    ey = pos[1] + glasses.shape[0]

    # 합성할 영역이 입력 영상 크기를 벗어나면 무시
    if sx < 0 or sy < 0 or ex > img.shape[1] or ey > img.shape[0]:
        return

    # img1 : 입력 영상의 부분 영상
    img1 = img[sy:ey, sx:ex] # shape=(h, w, 3)
    # img2 : 안경 영상의 부분 영상
    img2 = glasses[:, :, 0:3] # shape=(h, w, 3)
    alpha = 1. - (glasses[:, :, 3] / 255.) # shape=(h, w)

    # BGR 채널별로 두 부분 영상의 가중합
    img1[..., 0] = (img1[..., 0] * alpha + img2[..., 0] * (1. - alpha)).astype(np.uint8)
    img1[..., 1] = (img1[..., 1] * alpha + img2[..., 1] * (1. - alpha)).astype(np.uint8)
    img1[..., 2] = (img1[..., 2] * alpha + img2[..., 2] * (1. - alpha)).astype(np.uint8)


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('비디오 열기 실패!')
    sys.exit()

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 30, (w, h))

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
eye_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

if face_classifier.empty() or eye_classifier.empty():
    print('xml을 읽을 수 없습니다')
    sys.exit()

glasses = cv2.imread('glasses.png', cv2.IMREAD_UNCHANGED)

if glasses is None:
    print("PNG파일을 읽을 수 없습니다")
    sys.exit()

ew, eh = glasses.shape[:2]
ex1, ey1 = 240, 300
ex2, ey2 = 660, 300

while True:
    ret, frame = cap.read()

    if not ret:
        break

    faces = face_classifier.detectMultiScale(frame, scaleFactor=1.2, minSize=(100, 100), maxSize=(400, 400))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y, w, h), (255, 0, 255), 2)

        faceROI = frame[y:y + h // 2, x:x + w]
        eyes = eye_classifier.detectMultiScale(faceROI)

        if len(eyes) != 2:
            continue

        x1 = x + eyes[0][0] + (eyes[0][2] // 2)
        y1 = x + eyes[0][1] + (eyes[0][3] // 2)
        x2 = x + eyes[1][0] + (eyes[1][2] // 2)
        y2 = x + eyes[1][1] + (eyes[1][3] // 2)

        if x1> x2:
            x1, y1, x2, y2 = x2, y2, x1, y1


        cv2.circle(faceROI, (x1, y1), 5, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.circle(faceROI, (x2, y2), 5, (255, 0, 0), 2, cv2.LINE_AA)

        fx = (x2 - x1) / (ex2 - ex1)
        '''
            interpolation
            cv2.INTER_NEAREST : 최근방 이웃 보간법
            cv2.INTER_LINEAR : 양선형 보간법(2*2 이웃 픽셀 참조)
            cv2.INTER_CUBIC : 3차회선 보간법(4*4 이웃 픽셀 참조)
            cv2.INTER_AREA : 영상 축소시 효과적
        '''
        glasses2 = cv2.resize(glasses, (0,0), fx=fx, fy=fx, interpolation=cv2.INTER_AREA)

        pos = x(x1 - int(ex1 * fx), y1 - int(ey1 * fx))

        overlay(frame, glasses2, pos)

    out.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cap.release()
cv2.destroyAllWindows()