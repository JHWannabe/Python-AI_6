'''
템플릿 매칭
- 입력 영상에서 템플릿 영상과 일치하는 부분을 찾는 기법
- 템플릿: 찾는 대상이 되는 작은 영상. 패치(patch)

    cv2.matchTemplate(image, templ, method, result=None, mask=None)
    image : 입력 영상, 8비트 또는 32비트
    templ : 템플릿 영상, image보다 같거나 작은 크기, 같은 타임
    method : 비교 방법. cv2.TM_ 시작하는 플래그 지정
        TM_SQDIFF : Sum of squared difference, 완전히 같으면 0, 다르면 값이 커짐
        TM_CCORR : (Cross) Correlation, 같으면 큰 값, 다르면 작은 값
        TM_CCOEFF : 평균 보정 후 Correlation 연산
        TM_CCOEFF_NORMED : 완전히 일치하면 1, 역일치하면 -1, 연관성이 없으면 0
    result : 비교 결과 행렬
        numpy.ndarray
        dtype: numpy.float32
        image 크기가 W*H, templ 크기가 w*h 이면
        result는 (W-w+1) * (H-h+1)
'''

import sys
import numpy as np
import cv2

src = cv2.imread('circuit.bmp', cv2.IMREAD_GRAYSCALE)
templ = cv2.imread('crystal.bmp', cv2.IMREAD_GRAYSCALE)

if src is None or templ is None:
    print('영상을 읽을 수 없습니다')
    sys.exit()

noise = np.zeros(src.shape, np.int32)
cv2.randn(noise, 50, 10)
src = cv2.add(src, noise, dtype=cv2.CV_8UC3) # 입력 영상 밝기 증가, 잡음을 추가

res = cv2.matchTemplate(src, templ, cv2.TM_CCOEFF_NORMED)
res_norm = cv2.normalize(res, None, 0, 266, cv2.NORM_MINMAX, cv2.CV_8U)

_, maxv, _, maxloc = cv2.minMaxLoc(res)
print('maxv:', maxv)
print('maxloc:', maxloc)

th, tw = templ.shape[:2]
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
cv2.rectangle(dst, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)

cv2.imshow('res_norm', res_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()