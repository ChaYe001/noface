import os
import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)

facefile = "/home/gubo/1/1/caiji/2/"
successfile = "/home/gubo/8/qingchu/"
successfile1 = "/home/gubo/8/buqingchu/"
piclist = os.listdir(facefile)
successlist = os.listdir(successfile)
a = 0
b = 0
for okname in piclist:
    if okname.endswith('jpg'):

        img = cv2.imread(facefile + okname)
        # sp = img.shape
        # y = sp[0]*0.15
        # #print(y)
        # h = sp[0]*0.70
        # #print(h)
        # x = sp[1] * 0.15
        #
        # w = sp[1] * 0.7
        # img = img[int(y):int(y + h), int(x):int(x + w)]
        img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgMat = np.matrix(img2gray)
        print(imgMat)
        x, y = imgMat.shape
        print(x, y)

        score = 0
        temp = 0


        for i in range(0, (x - 2)):

            for j in range(0, y):
                temp +=1


                score += int(int(imgMat[i + 2, j]) - int(imgMat[i, j])) ** 2
                #score += int(int(imgMat[i , j + 2]) - int(imgMat[i, j])) ** 2
        #print(temp)
        score =  score / 65536
        #score = 300*300*score/65536/temp
        score = round(score, 2)
        print(str(score) + '-' + okname)

        if score >= 35:

            a = a + 1
            #cv2.imwrite(successfile + str(score) + '-' + okname + ".jpg", img)

        else:
            b +=1
            #cv2.imwrite(successfile1 + str(score) + '-' + okname + ".jpg", img)
        print(a, b)
