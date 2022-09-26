import sys
import cv2

def load_image(name): # str
    ch2_path = '/Users/krc/Documents/opencv/ch02/'
    img1 = cv2.imread(ch2_path+name, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(ch2_path+name, cv2.IMREAD_COLOR)

    if img1 is None or img2 is None:
        print('image load fail')
        sys.exit()


    print(type(img1)) # numpy.ndarray
    print(img1.shape, img2.shape)
    print(img1.dtype, img2.dtype)

    h, w = img1.shape # 크기 불러오기
    print('w * h = {} * {}'.format(w,h))

    h, w = img2.shape[:2] # 2차원 이상이기때문에 슬라이스
    print('w * h = {} * {}'.format(w,h))

    if img1.ndim == 2: 
        print('img1 is a grayscale image')

    cv2.imshow('image1', img1)
    cv2.imshow('image2', img2)
    cv2.waitKey()
    cv2.destroyAllWindows() 



def pixel_value(name, x, y): #str, int, int
    ch2_path = '/Users/krc/Documents/opencv/ch02/'
    img1 = cv2.imread(ch2_path+name, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(ch2_path+name, cv2.IMREAD_COLOR)

    # pixel value - gray image
    p1 = img1[y, x]
    print('grayscale:', p1)

    # color image 
    p2 = img2[y, x]
    print('color values:', p2)


    # image can be modified
    # img2[:230, :230] = [120,120,120]

