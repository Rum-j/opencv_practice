import sys
import cv2


def vcheck():
    return "hello, openCV" f"{cv2.__version__}"


img = cv2.imread('cat.bmp', flags=cv2.IMREAD_GRAYSCALE)

if img is None:  # 이미지를 불러올 수 없는 경우에 대한 방어
    print('Image load failed')
    sys.exit()

cv2.imwrite('cat_grey.png', img)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE) # default = autosize
cv2.moveWindow('image', 800, 200) # window의 위치 지정
cv2.imshow('image', img)
cv2.waitKey()  # 키보드 입력이 들어올 때까지 기다리기

cv2.destroyAllWindows()  # 기존의 창을 모두 닫기

if __name__ == "__main__":  # pragma: no cover
    ret = vcheck()
    print(ret)