
import os
import cv2
#import BlurDetection
from BlurDetection import BlurDetection

facefile = "/home/gubo/1/1/buqingchu/2-buqingchu/"
successfile = "/home/gubo/8/buqingchu/"
successfile1 = "/home/gubo/8/qingchu/"
successfile2 = "/home/gubo/8/0.33/"
successfile3 = "/home/gubo/8/0/"
def blur_detction(testImg):
    tmp = BlurDetection('')
    score = tmp._Tenengrad(testImg)
    return float(score)
piclist = os.listdir(facefile)
successlist = os.listdir(successfile)
# i = 0


piclist = os.listdir(facefile)
successlist = os.listdir(successfile)
for okname in piclist:
    if okname.endswith('jpg'):

        img = cv2.imread(facefile + okname)

        sp = img.shape
        y = sp[0] * 0.15
        #print(y)
        h = sp[0] * 0.70
        #print(h)
        x = sp[1] * 0.15

        w = sp[1] * 0.7
        testImg = img[int(y):int(y + h), int(x):int(x + w)]
        testImg = cv2.resize(testImg,(80,80),interpolation=cv2.INTER_LINEAR)
        cv2.resize()
        sp = testImg.shape
        #print(sp)
        #print(sp[0])
            #cal_score = Cal(testImg)
            #print(cal_score)
        score = blur_detction(testImg)
        score = round(score, 2)


        # print(str(score) +'-' + okname)
        #cv2.imwrite(successfile + str(score) + '-' + okname, img)
            #print(res_int)
        # os.system(
        #     'mv -f ' + ' ' + facefile + okname + ' ' + successfile + okname +'_' + str(score))