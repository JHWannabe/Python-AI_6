'''
가우시안 필터

* 평균값 필터에 의한 블러링의 단점
    - 필터링 대상 위치에서 가까이 있는 픽셀과 멀리 있는 픽셀이 모두 같은 가중치를 사용하여 평균을 계산
    - 멀리 있는 픽셀의 영향을 많이 받을 수 있음

    cv2.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)

    src : 입력 영상, 각 채널 별로 처리됨
    ksize : 가우시안 커널 크기. (0, 0)을 지정하면 sigma값에 의해 자동 결정됨
    sigmaX : x 방향의 sigma
    sigmaY : y 방향의 sigma, 0이면 sigmaX와 같에 설정
    borderType : 가장자리 픽셀 확장 방식
    dst : 출력 영상, src와 같은 크기 같은 타입
'''

import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2.GaussianBlur(src, (0, 0), 3)
dst2 = cv2.blur(src, (7, 7))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()