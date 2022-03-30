import cv2

'''
    ndim : 차원 수 = len(img.shape)
    shape : 각 차원의 크기. (h, w) 또는 (h, w, 3)
    size : 전체 원소 개수
    dtype : 원소의 데이터 타입
'''


img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

print('type(img1):', type(img1))
print('img1.shape:', img1.shape)
print('img2.shape:', img2.shape)
print('img2.dtype:', img2.dtype)

h, w = img2.shape[: 2]
print('img2 size: {} * {}'.format(w, h))

if len(img1.shape) == 2:
    print('그레이스케일 이미지')
elif len(img1.shape) == 3:
    print('RGB컬러 스케일 이미지')

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.waitKey()
#
# img1[30, 30] = 255
# img2[40, 60] = (0, 0, 255)

img1[:, :] = 255
img2[:, :] = (0, 0, 255)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()