from PIL import Image
import os
import glob

# 이미지가 있는 폴더 경로
path = r'C:\Users\hong0\라이프이노베이션_샘플'

# glob, os 비교
glob_files = glob.glob(path + "\*.jpg")
os_files = os.listdir(path)

print(glob_files)
print(os_files)

# 해상도 조절 후 저장
for image in glob_files:
    image_file = Image.open(image)
    resize_image = image_file.resize((640, 640))
    resize_image.save(image[:-4]+'_resize.jpg')

print('Done.')