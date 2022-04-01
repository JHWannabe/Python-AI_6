'''
트랙바
- 프로그램 동작 중 사용자가 지정한 범위 안의 값을 선택할 수 있는 컨트롤
- OpenCV에서 제공하는 그래픽 사용자 인터페이스
'''

import numpy as np
import cv2

def on_level_change(pos):
    value = pos * 8
    if value >= 255:
        value = 255
    img[:] = value
    cv2.imshow('image', img)

img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')

'''
cv2.createTrackbar(trackbarName, windowName, value, count, onChange)
trackbarName : 트랙바 이름
windowName : 트랙바를 생성할 창 이름
value : 트랙바 위치 초기값
count : 트랙바 최대값, 최소값은 항상 0
onChange : 트랙바의 위치가 변경될 때마다 호출할 콜백함수 이름
'''
cv2.createTrackbar('level', 'image', 0, 32, on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()