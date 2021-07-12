import os
import sys
#import popen2
import sqlite3
import os
from PIL import Image
import matplotlib.pyplot as plt
import time
i = 0#不在库初始值
j = 0#误识别初始值
conn = sqlite3.connect('/home/gubo/数据库/路人看库/FaceDatabase.db')
cur = conn.cursor()

facefile ='/home/gubo/WorkSpace/success3/'
piclist = os.listdir(facefile)
# facefile1 ='/home/gubo/WorkSpace/2.blu/Posface/littleface/'
# piclist1 = os.listdir(facefile1)
# def showpic():

for okname in piclist:
    img = Image.open(facefile + okname)
    plt.figure(figsize=(10, 10))
    plt.ion()  # 打开交互模式
    plt.axis('off')  # 不需要坐标轴
    plt.imshow(img)
    plt.pause(3)
    plt.clf()
    plt.close()
    #time.sleep(0.5)
    name = okname.split('.')[0]
    name = name[1:]
    pic = "select md5 from t_FacialFeature where name=" + "'" + str(name) + "'"
    #print(pic)
    cur.execute(pic)
    #print(cur.fetchall())
    md = str(cur.fetchall())
    md = md.split("'")[1]
    print('md5 是' + md)
    a = ''
    cosD = ''
    command = 'adb logcat'
    logcat = os.popen(command,'r',3)

    while True:
        data = logcat.readline()
        #print(data)
        #a = cosD
    #md5 = data[-34:-2]
        # i = 0 ##不在库初始值
        # j = 0 ##
    #print(a)
    #data = "04-03 10:19:58.812 21792 32328 W GLXSS_SDK: │ tag = AiPresenter  | msg = 1----FaceComparisonResult{cosD=67.71814, md5='f82142532961c29a0395502061005c4e'}"

        if "msg = 1" in data:
            #a = cosD
            md5 = data.split("md5='")[-1].split("'}")[0]
            cosD = data.split("cosD=")[-1][0:5]
            #
            print('查询结果：md5是'+ md5)
            print('查询结果：相似度是'+ cosD)
            #i = 0

            if float(cosD) < 80:
                i = i + 1## 不在库加１
                print(i)
                #a = cosD
            #j = 0
            if float(cosD) > 80:

                if md5 != md:
                    print('cosD是' + cosD)
                    print('a是' + a)
                    if cosD == a:
                        print('未识别')

                    else:
                        j = j + 1
                        print(j)## 误识别加１

                    #a = cosD
                    break
                break
            a = cosD
            break

    #print(a)
        #os.system('ps')
        #a = cosD
        #break

        #print('正确')
