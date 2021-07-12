
import os
import cv2
#import BlurDetection
from BlurDetection import BlurDetection
from yaw_module import YawDetecction
def blur_detction(testImg):
    tmp = BlurDetection('')
    score = tmp.TestBrener(testImg)
    return int(score)
face_cascade = cv2.CascadeClassifier(
     '/home/gubo/WorkSpace/opencv-3.4.2/data/haarcascades/haarcascade_frontalface_alt.xml')

capture = cv2.VideoCapture(0)
while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # 返回人脸矩形数组
    if len(faces) == 0:

        print('there is no face')

    elif len(faces) >= 1:

        for i in range(int(len(faces))):
            (x, y, w, h) = faces[i]
            testImg = frame[y:y + h, x:x + w]
        #print(x,y,w,h)

    # score = blur_detction(testImg)
    # print(score)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

