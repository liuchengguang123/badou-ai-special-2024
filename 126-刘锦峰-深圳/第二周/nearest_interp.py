"""
图片插值
"""
import cv2
import numpy as np


def function(img, h, w):
    height, width, channels = img.shape
    emptyimage = np.zeros((h, w, channels), dtype=np.uint8)
    sh = h / height
    sw = w / width

    for i in range(h):
        for j in range(w):
            x = int(i / sh + 0.5)
            y = int(j / sw + 0.5)
            emptyimage[i, j] = img[x, y]

    return emptyimage


photo = "Japan's surrender.webp"  # 请替换为实际的图像文件路径
img = cv2.imread(photo)

if img is None:
    print("无法加载图像")
else:
    h = 800
    w = 800
    zoom = function(img, h, w)
    print(zoom.shape)
    cv2.imshow("nearest interp", zoom)
    cv2.imshow("image", img)
    cv2.waitKey(0)
