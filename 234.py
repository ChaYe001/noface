import cv2
import numpy
import os
import codecs
from numpy import *
numpy.set_printoptions(threshold=numpy.inf)
#import Image
screenLevels = 255.0



def yuv_import(filename,dims,numfrm,startfrm):
    fp=open(filename,'rb')
    blk_size = prod(dims) *3/2
    #fp.seek(blk_size*startfrm,0)
    fp.seek(0,0)
    Y=[]
    U=[]
    V=[]
    # print (dims[0])
    # print (dims[1])
    d00=dims[0]//2
    d01=dims[1]//2
    Yt=zeros((dims[0],dims[1]),uint8,'C')
    Ut=zeros((d00,d01),uint8,'C')
    Vt=zeros((d00,d01),uint8,'C')
    for i in range(numfrm):
        for m in range(dims[0]):
            for n in range(dims[1]):
                #print m,n
                Yt[m,n]=ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                Ut[m,n]=ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                Vt[m,n]=ord(fp.read(1))
        Y=Y+[Yt]
        #print(Y)
        U=U+[Ut]
        V=V+[Vt]
    fp.close()
    return (Y,U,V)
if __name__ == '__main__':
    width=1280
    height=720
    facefile = "//home/gubo/樣本/caiji/採集85_yuv樣本/1/"
    successfile = "/home/gubo/11/buqingchu/"
    successfile1 = "/home/gubo/11/qingchu/"
    successfile2 = "/home/gubo/11/0.33/"
    successfile3 = "/home/gubo/11/0/"
    piclist = os.listdir(facefile)
    f = 1
    b = 1
    c = 1
    d = 1
    for okname in piclist:
        if okname.endswith('yuv'):
            #print(facefile + okname)
            a = okname.split('_')
            x = int(a[0])
            #print(x)
            y = int(a[1])
            #print(y)
            w = int(a[2]) - int(a[0])
            h = w
            def_x = int(x) + int(0.15*w)
            def_y = int(y) + int(0.15*h)
            def_w = int(w*0.7)
            def_h = int(h*0.7)

            data=yuv_import(facefile + okname , (height, width), 1, 0)
            YY=data[0][0]


            imgMat = numpy.matrix(YY)
            #print(imgMat)

            face = imgMat[def_y:def_y + def_h,def_x:def_x + def_w]
            face1 = imgMat[y:y+h,x:x+w]

            # cv2.imshow("1",face1)
            # cv2.waitKey(0)
            x1, y1 = face.shape
            #print(x, y)
            shift = int(x1 / 56)
            if shift == 0:
                shift = 1
            #print(shift)
            score1 = 0
            score2 = 0
            temp = 0

            for i in range(0, (x1- shift),shift):

                for j in range(0, (y1 - shift),shift):
                    temp += 1

                    score1 += int(int(face[i + shift, j]) - int(face[i, j])) ** 2
                    score2 += int(int(face[i , j + shift]) - int(face[i, j])) ** 2
            #print(temp)
            score1 = 10000*score1/temp/65536
            score2 = 10000 * score2 / temp / 65536
            # score = 300*300*score/65536/temp
            score1 = round(score1, 2)
            score2 = round(score2, 2)
            score = numpy.var([score1,score2])
            score = round(score,2)
            defi = 30
            ###0.74为
            if score1>=0.33*0.74*defi and score2>=0.19*0.74*defi:
                #print('i: ' + str(i))
                f += 1
                print('a-' +str(score) + '-' + str(score1) + '-' + str(score2) +'-' + a[-1])
                cv2.imwrite(successfile1 + str(score) + '-' + str(score1) + '-' + str(score2) +'-'  + a[-1] + '.jpg', face1)
            elif score1<0.12*0.74*defi or score2<0.12*0.74*defi:

                #print('j: ' + str(j))
                b +=1
                print('b-' + str(score) + '-' + str(score1) + '-' + str(score2) +'-' + a[-1])
                #cv2.imwrite(successfile + str(score) + '-' + str(score1) + '-' + str(score2) +'-'  + a[-1] + '.jpg', face1)
            elif score < 6*0.74*0.74:

                #print('k: ' + str(k))
                c +=1
                print('c-' + str(score) + '-' + str(score1) + '-' + str(score2) +'-' + a[-1])
                cv2.imwrite(successfile2 + str(score) + '-' + str(score1) + '-' + str(score2) +'-' + a[-1] + '.jpg', face1)
            else:
                #print('l: ' + str(l))
                print('d-' + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + a[-1])
                #cv2.imwrite(successfile3 + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + a[-1] + '.jpg', face1)
                d +=1
            print(f+c-2,b+d-2)


