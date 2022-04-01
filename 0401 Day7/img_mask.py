'''
ROI
- Region of Interest, 관심 영역
- 영상에서 특정 연산을 수행하고자 하는 임의의 부분 영역

마스크 연산
- OpenCV는 일부 함수에 대해 ROI 연산을 지원
- cv2.CV_8UC1 타입(그레이스케일 영상) = numpy.uint8
- 마스크 영상의 픽셀 값이 0이 아닌 위치에서만 연산이 수행됨
    (보통 마스크 영상으로는 0 또는 255로 구성된 이진 영상(binary image)을 사용

# 컬러영상 cv2.CV_8UC3 타입 = numpy.uint8 (h, w, 3)
'''
import sys
import cv2

src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('파일을 읽어올 수 없습니다')
    sys.exit()
'''
    copyTo(src, mask, dst=None) -> return 값은 dst
    - src : 입력 영상
    - mask : 마스크 영상, 0이 아닌 픽셀에 대해서만 복사 연산
    - dst : 출력 영상, 만약 src와 크기 및 타입이 같은 dst를 입력으로 지정하면 dst를 새로 생성하지 않고 연산
'''
cv2.copyTo(src, mask, dst)

# cv2.imshow('src', src)
# cv2.imshow('mask', mask)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 알파 채널(투명 이미지)을 마스크 영상으로 이용
src = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)

if src is None or logo is None:
    print('파일을 읽어올 수 없습니다')
    sys.exit()

mask = logo[:,:,3]   # mask는 알파 채널로 만든 마스크 영상
logo = logo[:,:,:-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]

cv2.copyTo(logo, mask, crop)

cv2.imshow('src', src)
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()