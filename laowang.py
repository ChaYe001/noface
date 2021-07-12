
import os
import cv2
#import BlurDetection
from BlurDetection import BlurDetection
from yaw_module import YawDetecction

facefile = "/home/gubo/laowang/"
successfile = "/home/gubo/laowang/"
def blur_detction(testImg):
    tmp = BlurDetection('')
    score = tmp.TestBrener(testImg)
    return int(score)
piclist = os.listdir(facefile)
successlist = os.listdir(successfile)
# i = 0
for okname in piclist:
    if okname.endswith('jpg'):
        print(okname)
        # face_cascade = cv2.CascadeClassifier(
        #     '/home/gubo/WorkSpace/opencv-3.4.2/data/haarcascades/haarcascade_frontalface_alt.xml')
        img = cv2.imread(facefile + okname)
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转化为灰度图
            # faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # 返回人脸矩形数组
            # if len(faces) == 0:
            #
            #     spiltNoface()
            #
            # elif len(faces) == 1:
            #     (x, y, w, h) = faces[0]
        sp = img.shape
        print(sp)
        testImg = img[]
        cv2.imwrite('234.j108:720, 344:956pg',testImgd)

        score = blur_detction(testImg)
        print(score)
    # os.system(
    #     'mv -f ' + ' ' + facefile + okname + ' ' + successfile + okname +'_' + str(score))