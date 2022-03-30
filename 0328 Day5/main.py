import cv2
import sys

'''
    영상(image)
    - 픽셀(pixel)이 바둑판 모양의 격자에 나열되어 있는 형태(2차원 행렬)
    - 픽셀(pixel) : 영상의 기본 단위
    
    그레이스케일(grayscale)
    - 흑백 사진처럼 색상 정보가 없이 오직 밝기 정보만으로 구성된 영상
    - 밝기 정보를 256단계로 표현(0~255)
    - 8bit = lbyte 사용
    - Python(numpy.uint8)
    - 가로크기 * 세로크기 bytes
    
    255 255 255 230 240 255 ...
    
    트루컬러(truecolor)
    - 컬러 사진처럼 색상 정보를 가지고 있어서 다양한 색상을 표현할 수 있는 영상
    - Red, Green, Blue 색 성분을 256단계로 표현 -> 256**3
    - 3bytes
    - python(튜플, numpy.ndarray)
    - 가로크기 * 세로크기 * 3 bytes
    
    (255, 255, 255) (255, 255, 255) (255, 255, 255) ...
'''

# 컨트롤 + 쉬프트 + F10
print('OpenCV version : ', cv2.__version__)

cat = cv2.imread('cat.bmp')

if cat is None:
    print('파일을 찾을 수 없습니다.')
    sys.exit()

cv2.namedWindow("image")
cv2.imshow('image', cat)
cv2.waitKey()
cv2.destroyWindow()