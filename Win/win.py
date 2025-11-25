#import cv2
#import numpy as np

# # 创建窗口
#cv2.namedWindow('show', cv2.WINDOW_NORMAL)

# # 读取图像


# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# lower = np.array([0, 0, 200])  
# upper = np.array([179, 30, 255])  
# mask = cv2.inRange(hsv_img, lower, upper)
# # 将背景改为黑色
# img[mask > 0] = [0, 0, 0]
# cv2.imshow('show', img)  
# key = cv2.waitKey(0) & 0xFF
# if key == ord('q'):
#     cv2.destroyAllWindows() 

import cv2
import numpy as np

# 读取图像
img = cv2.imread("/media/wuyu/Data/日常/2538C8073D539443719C07D9CC3F491F.jpg")

if img is not None:
    # 将图像从BGR颜色空间转换为灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 二值化（文字部分设为白色）
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    # 膨胀操作（让文字轮廓更完整）
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=2)
    
    # 找轮廓
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 用红线圈出文字轮廓
    for cnt in contours:
        cv2.drawContours(img, [cnt], -1, (0, 0, 255), 2)  # 红色轮廓
    
    # 保存结果
    cv2.imwrite("text_contour_result.png", img)
else:
    print("Error: Could not read the image.")
