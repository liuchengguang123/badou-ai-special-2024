import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
直方图均衡化
"""
photo = "./Japan's surrender.webp"
#photo = "./lenna.png"

img = cv2.imread(photo,1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("img_gray",gray)

#灰度图像直方均衡化
dst = cv2.equalizeHist(gray)
#cv2.imshow("equalizeHist",dst)

#显示灰度直方图

hist = cv2.calcHist([dst],[0],None,[256],[0,256])
plt.figure()
plt.hist(dst.ravel(), 256)
plt.show()

cv2.imshow("Histogram Equalization1", np.hstack([gray, dst]))
#cv2.waitKey(0)

# 彩色图像直方图均衡化
img = cv2.imread(photo)

# 彩色图像均衡化,需要分解通道 对每一个通道均衡化
(b, g, r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
# 合并每一个通道
result = cv2.merge((bH, gH, rH))
cv2.imshow("Histogram Equalization2", np.hstack([img, result]))

cv2.waitKey(0)