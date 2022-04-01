'''
연산시간 측정법
- 컴퓨터 비전은 대용량 데이터를 다루고, 일련의 과정을 통해 최종 결과를 얻으므로 매 단계에서 연산 시간을 측정하여 관리할 필요가 있음
'''

import sys
import time
import numpy as np
import cv2

img = cv2.imread('hongkong.jpg')

tm = cv2.TickMeter()
'''
tm: cv2.TickMeter 객체
start() : 시간 측정 시작
stop() : 시간 측정 끝
reset() : 시간 측정 초기화
getTimeMilli() : 측정 시간을 밀리 초 단위로 변환

'''
tm.reset()
tm.start()
t1 = time.time()

# Canny() : 외곽선 검출 함수
edge = cv2.Canny(img, 50, 150)

tm.stop()
print('time : ',(time.time() - t1) * 1000)
print('time : {}ms.'.format(tm.getTimeMilli()))