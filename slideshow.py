from glob import glob
import os
import glob


file_list = os.listdir('./')
# OS로 불러오기 
# img_files = [file for file in file_list if file.endswith('.jpg')]

# glob으로 불러오기 
img_files = glob.glob('./*.png') # 특정 패턴의 문자열로 되어있는 file name을 불러오기

for f in img_files:
    print(f)