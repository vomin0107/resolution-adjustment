from PIL import Image
import os
import glob

# 이미지가 있는 폴더 경로
path = r'C:\Users\hong0\PycharmProjects\image-classify-annotate\images/'
test_path = path + 'test/'
train_path = path + 'train/'
test_resized_path = test_path + 'resized/'
train_resized_path = train_path + 'resized/'

# resize 목표 해상도
size = (300, 300)

# glob, os 비교
test_files = glob.glob(test_path + "*.jpg") # absolute path
train_files = glob.glob(train_path + "*.jpg")
# os_files = os.listdir(path) # relative path


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def display_progress(tot, idx):
    # os.system('cls')
    percent = int(100 * idx / tot)
    percent_anti = 100 - percent
    percent_err = 50 - int(percent_anti/2) - int(percent/2)

    percent_str = str(percent) + '% ['
    for i in range(int(percent/2)):
        percent_str += '#'
    for j in range(int(percent_anti/2)):
        percent_str += '-'
    if percent_err > 0:
        for k in range(percent_err):
            percent_str += '-'
    percent_str += ']'
    print(percent_str)


def main():
    index = 0
    total = len(test_files) + len(train_files)

    create_folder(test_resized_path)
    create_folder(train_resized_path)

    # 해상도 조절 후 저장
    display_progress(total, index)
    for test_image in test_files:
        image_file = Image.open(test_image)
        resize_image = image_file.resize(size)
        resize_image.save(test_resized_path + test_image.split('test\\')[1][:-4]+'_resized.jpg')
        index += 1
        display_progress(total, index)

    for train_image in train_files:
        image_file = Image.open(train_image)
        resize_image = image_file.resize(size)
        resize_image.save(train_resized_path + train_image.split('train\\')[1][:-4]+'_resized.jpg')
        index += 1
        display_progress(total, index)

    print('Done.')


if __name__ == '__main__':
    main()
