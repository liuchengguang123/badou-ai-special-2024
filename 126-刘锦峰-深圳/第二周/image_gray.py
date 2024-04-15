"""
彩色图像的灰度化、二值化
"""
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

photo = "./Japan's surrender.webp"
img = cv2.imread(photo)
h,w = img.shape[:2]
img_gray = np.zeros([h,w],img.dtype)                   #创建一张和当前图片大小一样的单通道图片
for i in range(h):
    for j in range(w):
        m = img[i,j]  #获取当前坐标BRG值
        img_gray = int(m[0]*0.11 + m[1]*0.59 + m[2]*0.3) #m[0~2]分别对应像素点的BRG值，根据公式 gray = R0.3+G0.59+B0.11计算灰度值
print(m)
print(img_gray)
cv2.imshow("image show gray",img_gray)


#将图像分成表格形式显示
plt.subplot(221)  #第一个子图
img = plt.imread(photo)
plt.imshow(img)
print(img)

# 灰度化
img_gray = rgb2gray(img) #值为0~1
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img_gray = img
plt.subplot(222)
plt.imshow(img_gray,cmap='gray')
print(img_gray)
#二值化

img_binary = np.where(img_gray >= 0.5, 1, 0) #np.where 里面是一个布尔变换，将灰度图像二值化，像素值大于或小于0.5进行黑白赋值
print(img_binary)

plt.subplot(223)
plt.imshow(img_binary,cmap='gray')
plt.show()

# 二值化
# h, w = img_gray.shape
# for i in range(h):
#     for j in range(w):
#         if (img_gray[i, j] <= 0.5):
#             img_gray[i, j] = 0
#         else:
#             img_gray[i, j] = 1