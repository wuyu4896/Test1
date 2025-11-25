import cv2
# 读取图片
img = cv2.imread("/media/wuyu/Data/日常/2538C8073D539443719C07D9CC3F491F.jpg")
# 转化成灰度图
img0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 保存结果
cv2.imwrite("gray.png",img0)
#-------------------------------------------------

import cv2
import numpy as np

# 创建窗口
cv2.namedWindow('show', cv2.WINDOW_NORMAL)

# 读取图像
img = cv2.imread("/media/wuyu/Data/日常/2538C8073D539443719C07D9CC3F491F.jpg")

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#低阈值
lower = np.array([0, 0, 200])  
#高阈值
upper = np.array([179, 30, 255])  
mask = cv2.inRange(hsv_img, lower, upper)
# 将背景改为黑色
img[mask > 0] = [0, 0, 0]
cv2.imshow('show', img)  
key = cv2.waitKey(0) & 0xFF
if key == ord('q'):
    cv2.destroyAllWindows() 


#--------------------------------------------

import cv2
import numpy as np

img = cv2.imread("/media/wuyu/Data/日常/2538C8073D539443719C07D9CC3F491F.jpg")
# 分离BGR通道
b, g, r = cv2.split(img)

# 单R输出
r_channel = np.zeros_like(img)
r_channel[:, :, 2] = r
# 单g输出
g_channel = np.zeros_like(img)
g_channel[:, :, 1] = g
# 单b输出
b_channel = np.zeros_like(img)
b_channel[:, :, 0] = b

# 保存
cv2.imwrite("r_channel.png", r_channel)
cv2.imwrite("g_channel.png", g_channel)
cv2.imwrite("b_channel.png", b_channel)

#--------------------------------------------------------
import cv2
import numpy as np

# 读取图像
img = cv2.imread("/media/wuyu/Data/日常/2538C8073D539443719C07D9CC3F491F.jpg")

    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 二值化
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    # 膨胀
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=2)
    
    # 找轮廓
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 用红线圈出文字轮廓
    for cnt in contours:
        cv2.drawContours(img, [cnt], -1, (0, 0, 255), 2)  # 红色轮廓
    
    # 保存结果
    cv2.imwrite("huakuang.png", img)


#-----------------------------------------------------------------------------
import cv2
import numpy as np

img = cv2.imread("/media/wuyu/Data/日常/2538C8073D539443719C07D9CC3F491F.jpg")
#获取图像尺寸‌
h, w = img.shape[:2]
# 计算中心
center = (w // 2, h // 2)
# 构造旋转矩阵（向左旋转45°)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
# 旋转
rotated = cv2.warpAffine(img, M, (w, h))
# 保存
cv2.imwrite("xuanzhuan.png", rotated)

