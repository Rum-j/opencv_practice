import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)

cv2.line(
    img,
    (
        50,
        50,
    ),
    (200, 50),
    (100, 100, 0),
    5,
)
cv2.line(
    img,
    (
        50,
        60,
    ),
    (150, 160),
    (100, 100, 0),
)


# 내부를 채우는 사각형
cv2.rectangle(img, (70, 220), (180, 280), (0, 220, 0), -1)

# polygon

pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2, lineType=cv2.LINE_AA)

#text
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
