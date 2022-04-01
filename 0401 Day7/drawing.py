'''
* 그리기 함수 사용시 주의할 점
    - 그리기 알고리즘을 이용하여 영상의 픽셀 값 자체를 변경
    - 원본 영상이 필요하면 복사본을 만들어서 그리기 & 출력
    - 그레이스케일 영상에는 컬러로 그리기 안 됨
    - cv2.cvtColor() 함수로 BGR 컬러 영상으로 변환한 후 그리기 함수 호출
'''
import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)
'''
    cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
    img : 그림을 그릴 영상
    pt1, pt2 : 직선의 시작점과 끝점, 튜플
    color : 선 색상 또는 밝기
    thickness : 두께(기본값은 1)
    lineType : 선 타입(기본값은 cv2.LINE_8)
    shift : 좌표값의 축소 비율(기본값은 0)
'''
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

'''
    cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None) -> 리턴값 img
    cv2.rectangle(img, rec, color, thickness=None, lineType=None, shift=None) -> 리턴값 img
    img : 그림을 그릴 영상
    pt1, pt2 : 사각형의 두 꼭지점 좌표, 튜플
    rec : 사각형 위치 정보, 튜플
    color : 선 색상 또는 밝기
    thickness : 두께(기본값은 1)
    lineType : 선 타입(기본값은 cv2.LINE_8)
    shift : 좌표값의 축소 비율(기본값은 0)
'''
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 255, 0), -1) # -1을 설정하면 색상을 채움

cv2.circle(img, (300, 100), 30, (255, 255, 0), -1)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3)

text = 'Hello OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
