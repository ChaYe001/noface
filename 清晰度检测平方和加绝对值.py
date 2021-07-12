
import os
import cv2
import numpy as np
from BlurDetection import BlurDetection



facefile = "/home/gubo/1/1/caiji/buqingchu/"
successfile = "/home/gubo/8/buqingchu/"
successfile1 = "/home/gubo/8/qingchu/"
successfile2 = "/home/gubo/8/0.33/"
successfile3 = "/home/gubo/8/0/"
def blur_detction(testImg):
    tmp = BlurDetection('')
    score1,score2 = tmp._blurDetection(testImg)
    return score1,score2
piclist = os.listdir(facefile)
successlist = os.listdir(successfile)
# i = 0
def Cal(testImg):
    tmp = Cal('')
    cal_score = tmp.preImgOps(testImg)
    return int(cal_score)

piclist = os.listdir(facefile)
successlist = os.listdir(successfile)
a = 0
b = 0
c = 0
for okname in piclist:
    if okname.endswith('jpg'):

        img = cv2.imread(facefile + okname)
        sp = img.shape
        if sp[0] >= 80:
            # print(sp)
            # print(sp[0])
            y = sp[0] * 0.15
            # print(y)
            h = sp[0] * 0.70
            # print(h)
            x = sp[1] * 0.15

            w = sp[1] * 0.7
            testImg = img[int(y):int(y + h), int(x):int(x + w)]


        score1,score2 = blur_detction(testImg)
        score1 = round(score1, 2)
        score2 = round(score2, 2)

        score = np.var([score1, score2])
        score = round(score, 2)


        if score1 >= 10 and score2 >=8:
            a +=1
            cv2.imwrite(successfile + str(score1) + '-' + str(score2) + '-' + okname + ".jpg", img)
            # else:
            #     a +=1
            #     #cv2.imwrite(successfile1 + str(score1) + '-' + str(score2) + '-' + okname + ".jpg", img)
        elif score <=6:

            #print('k: ' + str(k))
            c +=1
            print('c-' + str(score) + '-' + str(score1) + '-' + str(score2) +'-' + okname)
            cv2.imwrite(successfile2 + str(score) + '-' + str(score1) + '-' + str(score2) +'-' + okname, img)
        else:
            #print('l: ' + str(l))
            print('d-' + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + okname)
            #cv2.imwrite(successfile3 + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + okname, img)
            b +=1
            #cv2.imwrite(successfile3 + str(score1) + '-' + str(score2) + '-' + okname + ".jpg", img)

    print(a + c,b)


