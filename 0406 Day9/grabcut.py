'''
그랩컷(GrabCut)
- 그래프 컷(graph cut)기반 영역 분할 알고리즘
- 영상의 픽셀을 그래프 정점으로 간주하고 픽셀들을 두 개의 그룹으로 나누는 최적의 컷을 찾는 방식
그랩컷 영상 분할 동작 방식
- 사각형 지정 자동 분할
- 사용자가 지정한 전경/배경 정보를 활용하여 영상 분할

    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterCount, mode=None)
    img : 입력 영상(8비트 3채널)
    mask : 입출력 마스크
        cv2.GC_BGD(0), cv2.GC_FGD(1), cv2.GC_PR_BGD(2), cv2.GC_PR_FGD(3)
    rect : ROI 영역. cv2.GC_INIT_WITH_RECT 모드에서만 사용됨
    bgdModel : 임시 배경 모델 행렬
    fgdModel : 임시 전경 모델 행렬
    iterCount : 결과 생성을 위한 반복 횟수
    mode : cv2.GC_ 시작하는 모드 상수. 보통 cv2.GC_INIT_WITH_RECT 모드로 초기화
        GC_INIT_WITH_MASK 모드로 업데이트 함
'''
import sys
import numpy as np
import cv2

src = cv2.imread('nemo.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

rc = cv2.selectROI(src)
mask = np.zeros(src.shape[:2], np.uint8)

cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

# 0: cv2.GC_BGD, 2: cv2.GC_PR_BGD
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
dst = src * mask2[:, :, np.newaxis]

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()


