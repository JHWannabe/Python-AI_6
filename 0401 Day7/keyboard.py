'''
문제. cat.bmp 영상을 띄우고 i 또는 I를 누를 경우 영상의 색반전을 보여주는 프로그램을 작성
    keycode = cv2.waitKey()
    i, I
    keycode == ord('i')
'''
import sys
import cv2
import numpy as np

img =cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('파일을 읽을 수 없습니다')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    keycode =cv2.waitKey()
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv2.imshow('image', img)
    elif keycode == 27:
        break

cv2.destroyAllWindows()