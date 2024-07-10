#呼叫圖片
# import cv2

# img = cv2.imread("c:/Users/User/Desktop/vsgit/FristProject/colorcolor.jpg")
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)   #圖片縮放
# cv2.imshow("img", img)
# cv2.waitKey(0)  #圖片停留

#----------------------------------------------------------------------------------------
# import cv2

# # 打開攝影機（默認攝影機索引為0）
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("無法打開攝影機")
#     exit()

# while True:
#     #ret取得影片的下一偵，frame如果有成功取得下一偵就回傳
#     ret, frame = cap.read()

#     if not ret:
#         print("無法接收幀（stream end?）")
#         break

#     # 顯示幀
#     cv2.imshow('camera', frame)

#     # 按 'q' 鍵退出循環
#     if cv2.waitKey(1) == ord('q'):
#         break

# # 釋放攝影機並關閉所有OpenCV視窗
# cap.release()
# cv2.destroyAllWindows()
#-------------------------------------------------------------------------------------
import cv2
import numpy as np
import random

cv2.imread("c:/Users/User/Desktop/vsgit/FristProject/colorcolor.jpg")
img = np.empty((300, 300, 3), np.uint8)     #uint整數，8bit

for row in range(300):
    for col in range(300):
        img[row][col]=[random.randint(0,255), random.randint(0,255), random.randint(0,255)]

cv2.imshow("img", img)
cv2.waitKey(0)

