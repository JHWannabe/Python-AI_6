'''
HOG(Histogram of Oriented Gradients) 보행자 검출
- 영상의 지역적 그레디언트 방향 정보를 특징 벡터로 사용
- 2005년 CVPR학회에서 보행자 검출 방법으로 소개되어 널리 사용되기 시작함
- 이후 다양한 객체 인식에서 활용됨

cv2.HOGDescriptor()
cv2.HOGDescriptor_getDefaultPeopleDetector()
retval : 미리 훈련된 특징 벡터. numpy.ndarray, numpy.float32

cv2.HOGDescriptor.detectMultiScale(img, hitThreshold=None, winStride=None, padding=None,
    scale=None, finalThreshold=None, useMeanshiftGrouping=None)
    img : 입력 영상
    hitThreshold : 특징 벡터와 SVM 분류 평면까지의 거리에 대한 임계값
    winStride : 셀 윈도우 이동 크기
    padding : 패딩 크기
    scale : 검색 위도우 크기 확대 비율. 기본값은 1.05
    finalThreshold : 검출 결정을 위한 임계값
    useMeanshiftGrouping : 겹쳐진 검색 윈도우를 합치는 방법 지정 플래그
'''
import cv2
import sys
import numpy as np
import random

cap = cv2.VideoCapture('vtest.avi')

if not cap.isOpened():
    print('동영상을 열 수 없습니다')
    sys.exit()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame = cap.read()

    if not ret:
        break

    detected, _ = hog.detectMultiScale(frame)

    for (x, y, w, h) in detected:
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(frame, (x, y, w, h), c, 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()