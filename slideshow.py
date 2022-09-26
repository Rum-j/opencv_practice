from glob import glob
import os
import glob
import cv2 


file_list = os.listdir('./')
# OS로 불러오기 
# img_files = [file for file in file_list if file.endswith('.jpg')]

# glob으로 불러오기 
img_files = glob.glob('./*.png') # 특정 패턴의 문자열로 되어있는 file name을 불러오기
if not img_files: # if empty folder
    print('there are no png files')
    sys.exit()

for f in img_files:
    print(f)


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN,
                      cv2.WINDOW_FULLSCREEN)

cnt = len(img_files) # 이미지 개수만큼 순환
idx = 0
while True:
    img = cv2.imread(img_files[idx])
    cv2.imshow('image', img)
    if cv2.waitKey(1000) == 27: # 1초 기다리기, 하지만 esc 누르면 루프 그만
        break
    idx += 1
    if idx >= cnt:
        idx =0 # initialize


cv2.destroyAllWindows()