# 모멘트 기반 객체 검출
# 모멘트 : 영상의 형태를 표현하는 일련의 실수값 ,특정 함수 집합과의 상관 관계 형태로 계산

# https://opencv-python.readthedocs.io/en/latest/doc/09.imageThresholding/imageThresholding.html
'''
모양 비교 함수
cv2.matchShapes(contour1, contour2, method, parameter)
contour1 : 첫번째 외곽선 또는 그레이스케일 영상
contour2 : 두번째 외곽선 또는 그레이스케일 영상
method : 비교 방법 저장
    cv2.CONTOURS_MATCH_l1, cv2.CONTOURS_MATCH_l2, cv2.CONTOURS_MATCH_l3
parameter : 0, 사용되지 않음

retval : 두 외곽선 또는 그레이스케일 영상 사이의 거리(distance)

cv2.threshold(img, threshold, value, type_flag)
img : 변환할 이미지
threshold : 스레시 홀딩 임계값
value : 임계값 기준에 만족하는 픽셀에 적용할 값
type_flag : 스레시 홀딩 적용 방법
    THRESH_BINARY : 픽셀 값이 임계값을 넘으면 value로 지정하고, 넘지 못하면 0으로 지정
    THRESH_BINARY_INV : THRESH_BINARY의 반대

cv2.findContours(img, mode, method, contours=None, hierarchy=None, offset=None)
- 외곽선 정보를 검출함
img : 입력 영상
mode : 외곽선 검출 모드
method : 외곽선 근사화 방법
contours : 검출된 외곽선 좌표
hierarchy : 외곽선 계층 정보
offset : 좌표 값 이동 옵셋

RETR_EXTERNAL : 외곽 윤곽선만 검출하고 계층 구조를 구성하지 않음
CHAIN_APPROX_NONE : 윤곽점들의 모든 점을 반환
'''

import sys
import numpy as np
import cv2

obj = cv2.imread('spades.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('symbols.png', cv2.IMREAD_GRAYSCALE)

if src is None or obj is None:
    print('Image load failed!')
    sys.exit()

# 객체 영상 외곽선 검출
_, obj_bin = cv2.threshold(obj, 128, 255, cv2.THRESH_BINARY_INV)
obj_contours, _ = cv2.findContours(obj_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
obj_pts = obj_contours[0]

# 입력 영상 분석
_, src_bin = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 입력 영상의 모든 객체 영역에 대해 처리
for pts in contours:
    if cv2.contourArea(pts) < 1000:
        continue

    rc = cv2.boundingRect(pts)
    cv2.rectangle(dst, rc, (255, 0, 0), 1)

    # 모양 비교
    dist = cv2.matchShapes(obj_pts, pts, cv2.CONTOURS_MATCH_I3, 0)

    cv2.putText(dst, str(round(dist, 4)), (rc[0], rc[1] - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1, cv2.LINE_AA)

    if dist < 0.1:
        cv2.rectangle(dst, rc, (0, 0, 255), 2)

cv2.imshow('obj', obj)
cv2.imshow('dst', dst)
cv2.waitKey(0)