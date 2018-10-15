import os
from _10_16.ImageViewer.config import imageDir, extension


def get_paths():
    img_paths = []
    for path_img in imageDir:
        for i in os.listdir(path_img):
            Image = os.path.join(path_img, i)
            ext = Image.split('.')[::-1][0].upper()
            if ext in extension:
                img_paths.append(Image)
    return img_paths
