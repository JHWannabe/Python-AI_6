'''
필터 카메라 만들기
1. 카메라로 내 영상 불러오기
2. 다양한 필터를 적용, 스페이스 바를 누를 때마다 모드 변경
(27 = 종료, ord(' ') = 모드 변경)

'''
import sys
import numpy as np
import cv2

def cartoon_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w//2, h//2))
    
    # bilateralFilter : 양방향 필터링
    # 에지 보전 잡음 제거 필터의 하나
    # cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None)
    # d : 필터링에 사용될 이웃 픽셀의 거리(지름), -1를 입력하면 sigmaSpace 값에 의해 자동 결정됨
    # sigmaColor : 색 공간에서 필터의 표준 편차
    # sigmaSpace : 좌표 공간에서 필터의 표준 편차
    blr = cv2.bilateralFilter(img2, -1, 20, 7)
    edge = 255 - cv2.Canny(img2, 80, 120)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    # bitwise_and : 비트 and 연산
    dst = cv2.bitwise_and(blr, edge)
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)

    return dst

def pencil_sketch(img):
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     blr = cv2.GaussianBlur(gray, (0, 0), 3)
     dst = cv2.divide(gray, blr, scale=255)
     return dst

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('비디오 열기 실패!')
    sys.exit()

cam_mode = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if cam_mode == 1:
        frame = cartoon_filter(frame)
    elif cam_mode == 2:
        frame = pencil_sketch(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == ord(' '):
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0

cap.release()
cv2.destroyAllWindows()
