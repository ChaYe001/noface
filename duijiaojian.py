
import os
import cv2
import numpy as np
from BluDetection1 import BlurDetection



facefile = "/home/gubo/1/1/buqingchu/2-buqingchu/"
successfile = "/home/gubo/8/buqingchu/"
successfile1 = "/home/gubo/8/qingchu/"
successfile2 = "/home/gubo/8/0.33/"
successfile3 = "/home/gubo/8/0/"
def blur_detction(testImg):
    tmp = BlurDetection('')
    score = tmp._blurDetection(testImg)
    return score
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
        #img = img[138:138 + 92, 582:582 + 92]
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
        print(sp)
        #print(sp[0])
        y = sp[0]*0.15
        print(y)
        h = sp[0]*0.70
        print(h)
        x = sp[1] * 0.15

        w = sp[1] * 0.7
        testImg = img[int(y):int(y + h), int(x):int(x + w)]
            # img = img[232 : 232+93, 216 :216 + 93]
            # testImg = img
        # cv2.imshow('80',testImg)
        # cv2.waitKey(0)

        #print(sp[0])
            #cal_score = Cal(testImg)
            #print(cal_score)
        score = blur_detction(testImg)

        score = round(score,2)

        defi = 20

        #print(str(score) +'-' + okname)
        cv2.imwrite(successfile + str(score) +'-' + okname, img)


        #score = (("{:0>5d}".format(score)))
        #print(score)

        #value = score/sp[0]*120
        #print(okname, sp[0],score,value)
        #os.rename(facefile + okname , facefile + str(value) + okname + '.jpg')
        #cv2.imwrite(successfile + str(score) +'-'+ str(score1) + '-' +str(score2)  + okname , testImg)
            #print(res_int)
        # os.system(
        #     'mv -f ' + ' ' + facefile + okname + ' ' + successfile + okname +'_' + str(score))