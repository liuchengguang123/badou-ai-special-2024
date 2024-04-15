
import cv2
import numpy as np

photo = "./lenna.png"
#photo = "./lenna.png"
img = cv2.imread(photo, 0)

x = cv2.Sobel(img,cv2.CV_16S,1,0)
y = cv2.Sobel(img,cv2.CV_16S,0,1)
'''
在经过处理后，别忘了用convertScaleAbs()函数将其转回原来的uint8形式。
否则将无法显示图像，而只是一副灰色的窗口。
dst = cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])
其中可选参数alpha是伸缩系数，beta是加到结果上的一个值。结果返回uint8类型的图片。
'''

absX = cv2.convertScaleAbs(x)#计算图像在水平方向（x方向）的一阶导数。参数 1 表示 dx = 1，即对图像应用水平Sobel滤波器来检测水平边缘
absY = cv2.convertScaleAbs(y)#计算图像在垂直方向（y方向）的一阶导数。参数 0 表示 dx = 0，而 1 表示 dy = 1，即对图像应用垂直Sobel滤波器来检测垂直边缘

'''
由于Sobel算子是在两个方向计算的，最后还需要用cv2.addWeighted(...)函数将其组合起来
。其函数原型为：
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
其中alpha是第一幅图片中元素的权重，beta是第二个的权重，
gamma是加到最后结果上的一个值。
'''

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

cv2.imshow("absX", absX)
cv2.imshow("absY", absY)

cv2.imshow("Result", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
# 读取图像并转换为灰度图像
img = cv2.imread(photo, cv2.IMREAD_GRAYSCALE)

# 使用 Sobel 算子进行边缘检测
sobelx = cv2.Sobel(img, cv2.CV_16S, 1, 0)

# 将结果图像转换为 8 位无符号整数类型并显示
sobelx_abs = np.absolute(sobelx)
sobelx_scaled = np.uint8(255 * sobelx_abs / sobelx_abs.max())

cv2.imshow('Original Image', img)
cv2.imshow('Sobel X', sobelx_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""



