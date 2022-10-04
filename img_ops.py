import numpy as np
import cv2


ch2_path = "/Users/krc/Documents/opencv/ch02/"
# 영상의 생성, 복사, 부분 추출
# create images
def create_4(x, y):  # int int
    img1 = np.empty((x, y), dtype=np.uint8)
    img2 = np.zeros((x, y, 3), dtype=np.uint8)
    img3 = np.ones((x, y, 3), dtype=np.uint8) * 110
    img4 = np.full((x, y), 128, dtype=np.uint8)

    cv2.imshow("image1", img1)
    cv2.imshow("image2", img2)
    cv2.imshow("image3", img3)
    cv2.imshow("image4", img4)
    cv2.waitKey()

    cv2.destroyAllWindows()


# copy images
img5 = cv2.imread(ch2_path + "HappyFish.jpg")
print(img5.shape)

img6 = img5  # 이름만 다른 복사, 참조
img7 = img5.copy()  # 새로운 복사본 생성, 메모리를 새롭게 할당
img5[50:150, :100] = (0, 0, 0)


cv2.imshow("fish", img5)
cv2.imshow("copy", img6)
cv2.imshow("copied by function", img7)


# 부분 영상 추출

img6 = img5[:, :].copy()
cv2.circle(img6, (100, 100), 20, (0, 120, 120), 2)

cv2.imshow("circle", img6)

cv2.waitKey()
cv2.destroyAllWindows()
