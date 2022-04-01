import sys
import numpy as np
import cv2

oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img,(oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y

img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
'''
마우스 이벤트 처리 함수(콜백 함수) 형식
onMouse(event, x, y, flags, param)
event : 마우스 이벤트 종류
x : 마우스 이벤트가 발생한 x좌표
y : 마우스 이벤트가 발생한 y좌표
flags : 마우스 이벤트 발생시 상태
param : cv2.setMouseCallback() 함수에서 설정한 데이터
'''
cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()