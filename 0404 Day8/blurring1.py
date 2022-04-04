'''
필터링
- 영상에서 필요한 정보만 통과시키고 원치 않는 정보는 걸러내는 작업
- 주파수 공간에서의 필터링, 공간적 필터링

공간적 필터링
- 영상의 픽셀 값을 직접 이용하는 필터링 방법
- 주로 마스크(mask) 연산을 이용함
    (마스크=커널(kernel))
- 마스크의 형태와 값에 따라 필터의 역할이 결정됨
    * 영상 부드럽게
    * 영상 날카롭게
    * 에지(edge) 검출
    * 잡음(noise) 제거

    cv2.filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None)
    src : 입력 영상
    ddepth : 출력 영상 데이터 타입
    kernel : 필터 마스크 행렬
    dst : 출력 영상
    anchor : 고정점 위치
    delta : 추가적으로 더할 값
    borderType : 가장자리 픽셀 확장 방식

    평균 값 필터
    - 영상의 특정 좌표 값을 주변 픽셀 값들의 산술 평균으로 설정
    - 픽셀들 간의 그레이스케일 값 변화가 줄어들어 날카로운 에지가 무뎌지고 영상에 있는 잡음의 영향이 사라지는 효과
'''

import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 읽어올 수 없습니다')
    sys.exit()

# kernel = np.ones((3, 3), dtype=np.float64) / 9
# dst = cv2.filter2D(src, -1, kernel)

dst = cv2.blur(src, (3,3))


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()