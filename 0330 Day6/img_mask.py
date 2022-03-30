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