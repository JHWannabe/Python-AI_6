import sys
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라를 사용할 수 없습니다')
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

'''
동영상 파일의 코덱, 압축방식, 색상, 픽셀 포맷 등
DIVX MPEG-4 코덱
XVID MPEG-4 코덱
FFMPEG MPEG-4 코덱
H.254/AVC 코덱
Motion-JPEG 코덱
'''
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
delay = round(1000 / fps)

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

if not out.isOpened():
    print('파일을 찾을 수 없습니다')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame

    out.write(inversed)

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()