import sys
from PIL import Image
import imagehash
import cv2
import matplotlib.pyplot as plt

DOODLENUM = 1000

if __name__ == "__main__":
    label = sys.argv[1]
    photo_filename = sys.argv[2]
    doodle_foldername = sys.argv[3]

    # resize photo
    photo = cv2.imread(photo_filename,0)
    photo_resize = cv2.resize(photo, (256, 256), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(photo_filename, photo_resize)

    # find similar doodle
    photo_hash = imagehash.average_hash(Image.open(photo_filename))
    min_dist = float('inf')
    for i in range(DOODLENUM):
        doodle_hash = imagehash.average_hash(Image.open(doodle_foldername+str(i)+'.png'))
        dist = photo_hash - doodle_hash
        if min_dist > dist:
            min_dist = dist
            min_idx = i
    print(min_dist)
    print(doodle_foldername+str(min_idx)+'.png')

    # input original image
    img_orig = cv2.imread(doodle_foldername+str(min_idx)+'.png',0)

    # resize image: 256*256
    width = 128
    height = 256
    img_resize = cv2.resize(img_orig, (width,height), interpolation=cv2.INTER_CUBIC)

    # save resize image
    cv2.imwrite(photo_filename, img_resize)

    plt.imshow(img_resize,cmap = 'gray')
    plt.show()




