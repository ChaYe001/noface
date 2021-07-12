import os
import cv2
#import BlurDetection
#from BlurDetection import BlurDetection
# def getListFiles(path):
#     ret = []
#     for root, dirs, files in os.walk(path):
#         for filespath in files:
#             ret.append(os.path.join(root,filespath))
#     return ret
# ret = getListFiles("/home/gubo/WorkSpace/face/image/")
def spiltpic():
    if len(faces) == 0 and sp != (720, 1280, 3):
        os.system('mv -f '+ ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/0face/littleface/littleface' + imagename)
    if len(faces) == 0 and sp == (720, 1280, 3):
        os.system('mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/0face/' + imagename)

    if len(faces) == 1 and sp != (720, 1280, 3):
        os.system('mv -f '+ ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/1face/littleface/littleface' + imagename)
    if len(faces) == 1 and sp == (720, 1280, 3):
        os.system('mv -f '+ ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/1face/' + imagename)

    if len(faces) >= 1 and sp != (720, 1280, 3):
        os.system('mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/moreface/littleface/littleface' + imagename)
    if len(faces) >= 1 and sp == (720, 1280, 3):
        os.system('mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/moreface/' + imagename)
# def dfscore():
#     tmp = BlurDetection('')
#     score = tmp.TestBrener(testImg)
#     cv2.imwrite('/home/gubo/WorkSpace/face/1face/df_' + str(float('%.2f' % score)) + '.jpg', testImg)
#     print(score, imagename)
facefile = "/home/gubo/WorkSpace/noface/image/recordf/"
piclist = os.listdir(facefile)
i = 0
for pic in piclist:
    #pass
    #print (imagename)
    picname = pic.split('.')[0]
    picpath = os.path.join(facefile, pic)
    imagename = (picname + '.jpg')
    img=cv2.imread(facefile +　imagename)
    print(imagename)
    i = i + 1
    #print(img)
    if img is None:  # 判断读入的img是否为空，为空就继续下一轮循环
        continue
    sp = img.shape


    #print(sp)

    face_cascade = cv2.CascadeClassifier('/home/gubo/WorkSpace/opencv-3.4.2/data/haarcascades/haarcascade_frontalface_alt.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转化为灰度图
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # 返回人脸矩形数组

    # if len(faces) >0:#判断人脸不为空
    #     (x, y, w, h) = faces[0]
    #     testImg = img[y-3:y+h+3,x-3:x+w+3]
    spiltpic()


    #cv2.imshow("show" , img )
#cv2.waitKey(0)
