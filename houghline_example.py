#refereces: t.ly/WRIuY
import sys
import math 
import cv2 as cv
import numpy as np


def main(argv):

    default_file = 'Arla-Standard-Milk_019.jpg'
    print(default_file)
    filename = argv[0] if len(argv) > 0 else default_file

    #load image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)

    #load success check
    if src is None:
        print('Error opening image')
        print('Usage: houghline_example.py'+ default_file)
        return -1

    dst= cv.Canny(src, 50, 200, None, 3)

    #Copy edges to the images that will dispaly the results in BGR
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)

    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            print("pt1 & pt2", pt1, pt2) #좌표확인
            cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
    

    linesP = cv.HoughLinesP(dst, 1, np.pi/180, 50, None, 50, 10)

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            if i%10 == 1:
                print("linesP", linesP[i], l) 
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA) 

    cv.imshow("Source", src)
    cv.imshow("detected lines in red - Standard hough line transform", cdst)
    cv.imshow("detected lines in red - Probabilistic line transform", cdstP)

    cv.waitKey()

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])