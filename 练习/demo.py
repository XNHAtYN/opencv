
import cv2

# 1. 打开电脑默认摄像头
cap = cv2.VideoCapture(0)

# 2. 检查摄像头是否成功打开
if not cap.isOpened():
    print("摄像头打开失败！")
    exit()

print("摄像头启动成功！")
print("按 Q 键退出程序")

# 3. 循环读取摄像头画面
while True:

    ret, frame = cap.read()

    # 检查是否成功读取图像
    if not ret:
        print("读取摄像头画面失败！")
        break

    # 4. 显示摄像头画面
    cv2.imshow("Robot Vision Demo", frame)

    # 5. 按 Q 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 6. 释放摄像头资源
cap.release()

# 7. 关闭所有窗口
cv2.destroyAllWindows()
