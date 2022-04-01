'''
cv2.VideoCapture
- 카메라와 동영상으로부터 프레임(frame)을 받아오는 작업을 VideoCapture로 모두 처리

    cv2.VideoCapture(index, apiPreference=None) -> retval 리턴
    index : camera_id + domain_offset_id
    apiPreference : 선호하는 카메라 처리 방법을 지정
    retval : cv2.VideoCapture 객체

    cv2.VideoCapture.open(index, apiPreference) -> 성공하면 True, 실패하면 False
'''

# 카메라 열기
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라를 사용할 수 없습니다')
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width : ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height : ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame # 반전

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()