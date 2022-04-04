'''
1. 두 개의 동영상을 동시에 열기
2. 첫 번째 동영상의 마지막 N개 프레임과 두 번째 동영상의 처음 N개 프레임을 합성
3. 합성된 영상을 동영상으로 저장하기
'''

import cv2
import numpy as np
import sys

cap1 = cv2.VideoCapture('video1.mp4')
cap2 = cv2.VideoCapture('video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('비디오를 읽어올 수 없습니다')
    sys.exit()

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)
print('frame_cnt1', frame_cnt1)
print('frame_cnt2', frame_cnt2)
print('fps', fps)

delay = round(1000/fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))

for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()

    if not ret1:
        print('frame read error!')
        sys.exit()

    out.write(frame1)
    print('.', end='')

    cv2.imshow('output', frame1)
    cv2.waitKey(delay)

for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print('frame read error!')
        sys.exit()

    dx = int(w / effect_frames) * i

    frame = np.zeros((h, w, 3), dtype=np.uint8)
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    frame[:, dx:w, :] = frame1[:, dx:w, :]

    out.write(frame)
    print('.', end='')

    cv2.imshow('output', frame)
    cv2.waitKey(delay)

for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        print('frame read error!')
        sys.exit()

    out.write(frame2)
    print('.', end = '')

    cv2.imshow('output', frame2)
    cv2.waitKey(delay)



cap1.release()
cap2.release()
cv2.destroyAllWindows()