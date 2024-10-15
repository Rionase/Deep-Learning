import os
import cv2
from PIL import Image

data_dir = 'data'
image_exts = ['jpeg', 'jpg', 'png']

def RemoveDodgyImage() :
    """
    REMOVE DODGY IMAGE

    Open the image and check if the image extention is in jpeg, jpg or png
    If failed to open or not in determined extention, then remove the image
    """

    for image_class in os.listdir(data_dir):
        for image in os.listdir(os.path.join(data_dir, image_class)):
            image_path = os.path.join(data_dir, image_class, image)
            try:
                img = cv2.imread(image_path)
                with Image.open(image_path) as img_file:
                    img_format = img_file.format.lower()
                if img_format not in image_exts:
                    print('Image not in ext list {}'.format(image_path))
                    os.remove(image_path)
            except Exception as e:
                print('Issue with image {}'.format(image_path))
                os.remove(image_path)

    print("LOG : Success Removing Dodgy Image")