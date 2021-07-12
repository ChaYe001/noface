
import os
import cv2
#import BlurDetection
from BlurDetection import BlurDetection
#from yaw_module import YawDetecction
#from ctypes import *

#load the shared object file
#adder = CDLL('./brenner.so')

#Find sum of integers


facefile = "/home/gubo/1/"
# successfile = "/home/gubo/laplas/"
# successfile = "/home/gubo/8/buqingchu/"
# successfile1 = "/home/gubo/8/qingchu/"
# successfile2 = "/home/gubo/8/0.33/"
# successfile3 = "/home/gubo/8/0/"
def blur_detction(testImg):
    tmp = BlurDetection('')
    score1, score2 = tmp._blurDetection(testImg)
    return score1, score2
piclist = os.listdir(facefile)
# successlist = os.listdir(successfile)
# i = 0
def Cal(testImg):
    tmp = Cal('')
    cal_score = tmp.preImgOps(testImg)
    return int(cal_score)

piclist = os.listdir(facefile)
# successlist = os.listdir(successfile)
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
            #             sp = img.shape
            #             #print(sp[0])
            #                 #cal_score = Cal(testImg)
            #                 #print(cal_score)
            #             score = blur_detction(img)
            #
            #             #value = score/sp[0]
            #             #print(okname, sp[0],score,value)
            #             os.rename(facefile + okname , facefile + str(score) + '.jpg')
        sp = img.shape
        # print(sp)
        # print(sp[0])
        # y = sp[0] * 0.15
        y=135
        # print(y)
        # h = sp[0] * 0.70
        h = 169
        # print(h)
        # x = sp[1] * 0.15
        x=101

        # w = sp[1] * 0.7
        w=169
        testImg = img[int(y):int(y + h), int(x):int(x + w)]
            # testImg = img
        cv2.imshow('80',testImg)
        cv2.waitKey(0)

        # print(sp[0])
        # cal_score = Cal(testImg)
        # print(cal_score)
        score1,score2 = blur_detction(testImg)
        score1 = round(score1, 2)
        score2 = round(score2, 2)
        print(score1,score2)

        # value = score/sp[0]*120
        # print(okname, sp[0],score,value)
        # os.rename(facefile + okname , facefile + str(value) + okname + '.jpg')
        #cv2.imwrite(successfile + str(score) + okname, testImg)
        defi = 35

        # if score1 >= defi or score2 >= defi:
        #     #print('a-' + str(score) + '-' + okname)
        #     # cv2.imwrite(successfile1 + str(score1) + '-' + str(score2) + '-' + okname, testImg)
        # # elif score1 < 0.2 * defi or score2 < 0.2 * defi:
        # #     print('b-' + str(score) + '-' + okname)
        # #     cv2.imwrite(successfile + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + okname, testImg)
        # # elif score <= 6:
        # #     print('c-' + str(score) + '-' + okname)
        # #     cv2.imwrite(successfile2 + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + okname, testImg)
        # else:
            #print('d-' + str(score) + '-' + okname)
            # cv2.imwrite(successfile3  + str(score1) + '-' + str(score2) + '-' + okname, testImg)