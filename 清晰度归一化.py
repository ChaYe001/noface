
import os
import cv2
#import BlurDetection
from BlurDetection import BlurDetection
#from yaw_module import YawDetecction
#from ctypes import *

#load the shared object file
#adder = CDLL('./brenner.so')

#Find sum of integers


facefile = "/home/gubo/未过滤模糊人脸/"
successfile = "/home/gubo/"
def blur_detction(testImg):
    tmp = BlurDetection('')
    score = tmp._blurDetection(testImg)
    return float(score)
piclist = os.listdir(facefile)
successlist = os.listdir(successfile)
# i = 0
def Cal(testImg):
    tmp = Cal('')
    cal_score = tmp.preImgOps(testImg)
    return int(cal_score)

piclist = os.listdir(facefile)
successlist = os.listdir(successfile)
for okname in piclist:
    if okname.endswith('jpg'):
        #print(okname)
        # face_cascade = cv2.CascadeClassifier(
        #     '/home/gubo/WorkSpace/opencv-3.4.2/data/haarcascades/haarcascade_frontalface_alt.xml')
        #
        img = cv2.imread(facefile + okname)
        # #img = cv2.resize(img, (1280, 720))
        #
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转化为灰度图
        # faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # 返回人脸矩形数组
        # if len(faces) == 0:
        #
        #     print('没有人脸')
        #
        # elif len(faces) == 1:
        #     (x, y, w, h) = faces[0]
        #     testImg = img[y:y + h, x:x + w]
        #     #print(x,y,w,h)
        #     print('有人脸')
        sp = img.shape
        #print(sp[0])
            #cal_score = Cal(testImg)
            #print(cal_score)
        score = blur_detction(img)

        value = score/sp[0]/sp[0]
        print(okname, sp[0],score,value)
        os.rename(facefile + okname , facefile + str(int(value*10000)) + '.jpg')
            #print(res_int)
        # os.system(
        #     'mv -f ' + ' ' + facefile + okname + ' ' + successfile + okname +'_' + str(score))