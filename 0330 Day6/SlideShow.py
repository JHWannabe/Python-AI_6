# 이미지 슬라이드 쇼 만들기
# https://wallpaperscraft.com/catalog/nature/1920x1080
import os
import glob
import sys
import cv2

img_files = glob.glob('.\\images\\*.jpg')

if not img_files:
    print('파일을 읽을 수 없습니다.')
    sys.exit()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print('이미지 로드 실패!')
        break

    cv2.imshow('image', img)
    if cv2.waitKey(2000) >= 0:
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()