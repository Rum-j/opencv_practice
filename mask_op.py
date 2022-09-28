import cv2


# 마스크 영상을 이용한 영상 합성
src = cv2.imread("airplane.bmp", cv2.IMREAD_COLOR)
mask = cv2.imread("mask_plane.bmp", cv2.IMREAD_GRAYSCALE)
dst = cv2.imread("field.bmp", cv2.IMREAD_COLOR)

h, w = src.shape[:2]
crop = dst[0:h, 0:w]  # src, dst가 크기가 다를 경우

cv2.copyTo(src, mask, crop)

cv2.imshow("dst", dst)
cv2.waitKey()

cv2.destroyAllWindows()
