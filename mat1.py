
import os
import cv2
import numpy as np
facefile = "/home/gubo/8/1/"
successfile = "/home/gubo/8/buqingchu/"
successfile1 = "/home/gubo/8/qingchu/"
successfile2 = "/home/gubo/8/0.33/"
successfile3 = "/home/gubo/8/0/"
piclist = os.listdir(facefile)
successlist = os.listdir(successfile)
i = 0
j = 0
k = 0
l = 0
m = 0
for okname in piclist:
    if okname.endswith('jpg'):

        img = cv2.imread(facefile + okname)
        img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sp = img2gray.shape
        # print(sp)
        # print(sp[0])
        y = sp[0] * 0.15
        # print(y)
        h = sp[0] * 0.70
        # print(h)
        x = sp[1] * 0.15

        w = sp[1] * 0.7
        testImg = img2gray[int(y):int(y + h), int(x):int(x + w)]
          # 将图片压缩为单通道的灰度图

        imgMat = np.matrix(testImg)
        x, y = imgMat.shape
        #print(imgMat)
        shift = int(x / 55)
        if shift == 0:
            shift = 1

        #print(shift)
        #
        score1 = 0
        score2 = 0
        tmp = 0
        for i in range(0, (x - shift), shift):

            for j in range(0, y - shift, shift):
                # print(i)
                # print(shift)
                # print(imgMat[i+shift,j])
                # print(imgMat[i,j])
                # print(imgMat[i,j+shift])
                # score += (imgMat[i+shift, j] - imgMat[i, j]) ** 2 #hang -
                score1 += int(int(imgMat[i + shift, j]) - int(imgMat[i, j])) ** 2
                score2 += int(int(imgMat[i, j + shift]) - int(imgMat[i, j])) ** 2

                tmp = tmp + 1
        score1 = 10000 * score1 / tmp / 65536
        score1 = round(score1,2)
        #print(score1)
        # score1 = (("{:0>5d}".format(score1)))
        score2 = 10000 * score2 / tmp / 65536
        score2 = round(score2,2)
        score = np.var([score1, score2])
        score = round(score, 2)
        score3 = np.average(imgMat)
        defi = 35
            # if score1>=0.4*defi and score2>=0.228*defi:
            #
            #
            #     print('a-' +str(score) + '-' + str(score1) + '-' + str(score2) +'-' + okname)
            #     cv2.imwrite(successfile1 + str(score) + '-' + str(score1) + '-' + str(score2) +'-'  + okname, img)
            # elif score1<0.14*defi or score2<0.14*defi:
            #
            #
            #     print('b-' + str(score) + '-' + str(score1) + '-' + str(score2) +'-' + okname)
            #     cv2.imwrite(successfile + str(score) + '-' + str(score1) + '-' + str(score2) +'-'  + okname, img)
            # elif score3 <120:
            #     if score <=6:
            #
            #
            #
            #         print('c-' + str(score) + '-' + str(score1) + '-' + str(score2) +'-' + okname)
            #         cv2.imwrite(successfile2 + str(score) + '-' + str(score1) + '-' + str(score2) +'-' + okname, img)
            #     else:
            #
            #         print('d-' + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + okname)
            #         cv2.imwrite(successfile3 + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + okname, img)
            #
            #
            # else:
            #     m +=1
            #     print('a+' + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + okname)
            #     cv2.imwrite(successfile1 + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + okname, img)


        # if score > 120:
        #     #a = np.var(imgMat)
        print(score3)
        #     cv2.imwrite(successfile + str(score) + '-'+ str(score1) + '-' + str(score2) + '-' + ".jpg", img2gray)