'''
영상의 잡음
- 영상의 픽셀 값에 추가되는 원치 않는 형태의 신호
- 가우시안 잡음, 소금&후추 잡음
- 미디엄 필터(주변 픽셀의 값들을 정렬하여 그 중앙값으로 픽셀 값을 대체 -> 소금&후추 잡음 제거에 효과적)

    cv2.medianBlur(src, ksize, dst=None)
    ksize : kernel의 크기, 1보다 큰 홀수를 지정
'''
import sys
import numpy as np
import cv2

src = cv2.imread('noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 찾을 수 없습니다')
    sys.exit()

dst = cv2.medianBlur(src, 3)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()