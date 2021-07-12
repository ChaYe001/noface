
import os
import cv2
import time
#import BlurDetection
from BlurDetection import BlurDetection
from yaw_module import YawDetecction
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 / 符号
    path = path.rstrip("/")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')

        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')

        return False

def yaw_detction(testImg):
    #if len(faces) > 0:
    tmp = YawDetecction()
    ret, pitch, yaw, roll= tmp.yaw_detect(testImg)
    #cv2.imshow(testImg)
    if ret == True:
        return int(yaw)
    else:
        return 10000

def blur_detction(testImg):
    #if len(faces) >0:#
        #img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2) #绘制矩形
        # j=j+1#统计
        #print(faces[0])

    tmp = BlurDetection('')
    score = tmp.TestBrener(testImg)
    return int(score)
    #cv2.imwrite('/home/gubo/WorkSpace/face/1face/df_' + str(float('%.2f'% score)) + '.jpg', testImg)

def spiltMoreface():

    if sp[0] < 720:
        os.system('mv -f '+ ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/moreface/littleface/' + imagename)
    if sp == (720, 1280, 3):
        os.system('mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/moreface/' + imagename)
    if sp[0] > 720:
        os.system('mv -f ' + ' ' + facefile +imagename + ' ' + '/home/gubo/WorkSpace/face/moreface/bigpic/' + imagename)

def spiltNoface():

    if sp[0] < 720:
        os.system('mv -f '+ ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/noface/littleface/' + imagename)
    if sp == (720, 1280, 3):
        os.system('mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/noface/' + newname)
    if sp[0] > 720:
        os.system('mv -f ' + ' ' + facefile +imagename + ' ' + '/home/gubo/WorkSpace/face/noface/bigpic/' + '_' + newname)

def spiltPosface(score,yaw):

    print(score)
    print(yaw)
    if sp[0] < 720:
        os.system(
            'mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/Posface/littleface/' + str(score) + '_' + str(yaw) + '_' + imagename)
    if sp == (720, 1280, 3):
        os.system('mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/Posface/' +str(score)+'_' + str(yaw) + '_' + imagename)
    if sp[0] > 720:
        os.system('mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/Posface/bigpic/' + str(score) + '_' + str(yaw) + '_' + imagename)

def spiltNegyawface():

    if sp[0] < 720:
        os.system(
            'mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/Negyawface/littleface/' + imagename)
    if sp == (720, 1280, 3):
        os.system('mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/Negyawface/' + imagename)
    if sp[0] > 720:
        os.system('mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/Negyawface/bigpic/' + imagename)
def spiltNegBluface():

    if sp[0] < 720:
        os.system(
            'mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/NegBluface/littleface/' + str(score)+'_'+ imagename)
    if sp == (720, 1280, 3):
        os.system('mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/NegBluface/' + str(score)+ '_' +imagename)
    if sp[0] > 720:
        os.system('mv -f ' + ' ' + facefile + imagename + ' ' + '/home/gubo/WorkSpace/face/NegBluface/bigpic/' + imagename)

facefile = "/home/gubo/WorkSpace/2.blu/noface/littleface/"##分类前的样本目录
face_a_file = '/home/gubo/WorkSpace/face'##
face_1_file = '/home/gubo/WorkSpace/face' + str(int(time.time()))
noface_littlefacefile = '/home/gubo/WorkSpace/face/noface/littleface'
noface_bigpicfile = '/home/gubo/WorkSpace/face/noface/bigpic'
Posface_littlefacefile = '/home/gubo/WorkSpace/face/Posface/littleface'
Posface_bigpicfile = '/home/gubo/WorkSpace/face/Posface/bigpic'
Negyawface_littlefacefile = '/home/gubo/WorkSpace/face/Negyawface/littleface'
Negyawface_bigpicfile = '/home/gubo/WorkSpace/face/Negyawface/bigpic'
NegBluface_littlefacefile = '/home/gubo/WorkSpace/face/NegBluface/littleface'
NegBluface_bigpicfile = '/home/gubo/WorkSpace/face/NegBluface/bigpic'
moreface_littlefacefile = '/home/gubo/WorkSpace/face/moreface/littleface'
moreface_bigpicfile = '/home/gubo/WorkSpace/face/moreface/bigpic'
mkdir(noface_littlefacefile)
mkdir(noface_bigpicfile)
mkdir(Posface_bigpicfile)
mkdir(Posface_littlefacefile)
mkdir(NegBluface_bigpicfile)
mkdir(NegBluface_littlefacefile)
mkdir(Negyawface_bigpicfile)
mkdir(Negyawface_littlefacefile)
mkdir(moreface_bigpicfile)
mkdir(moreface_littlefacefile)
# names = []
# for root, dirs, files in os.walk(facefile):  # 此处有bug  如果调试的数据还放在这里，将会递归的遍历所有文件
#     for file in files:
#          if file.endswith('jpg'):
#             names.append(str(file))
piclist = os.listdir(facefile)
i = 0
for imagename in piclist:

    # picname = pic.split('.')[0]
    # print(pic)
    # picpath = os.path.join(facefile, pic)
    # imagename = (picname + '.jpg')
    newname = (("{:0>5d}".format(i)) + '.jpg')
    #print(imagename)
    i=i+1
    #cv2.imshow(facefile + imagename)
    img=cv2.imread(facefile + imagename)
    sp = img.shape
    score = blur_detction(img)
    yaw = yaw_detction(img)
    if score < 35:

        spiltNegBluface()

        continue
    spiltPosface(score, yaw)
    # if img is None:  # 判断读入的img是否为空，为空就继续下一轮循环
    #     continue
    # sp = img.shape
    # face_cascade = cv2.CascadeClassifier('/home/gubo/WorkSpace/opencv-3.4.2/data/haarcascades/haarcascade_frontalface_alt.xml')
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转化为灰度图
    # faces = face_cascade.detectMultiScale(gray, 1.3, 5) # 返回人脸矩形数组
    # if len(faces) == 0:
    #
    #     spiltNoface()
    #
    # elif len(faces)==1:
    #     (x, y, w, h) = faces[0]
    #     testImg = img[y :y + h + 3, x :x + w + 3]
    #     #print(score, imagename)
    #     score = blur_detction(testImg)
    #
    #     if score < 25 :
    #
    #         spiltNegBluface()
    #
    #         continue
    #
    #     yaw = yaw_detction(testImg)
    #     # if abs(yaw) > 30:
    #     #
    #     #     spiltNegyawface()
    #     #
    #     #     continue
    #
    #
    #     spiltPosface(score,yaw)
    #
    # else:
    #     spiltMoreface()


        #img = cv2.resize(img,(1280,720))

    print(i)
os.rename(face_a_file, face_1_file)
    #cv2.imshow("show" , img )
#cv2.waitKey(0)
