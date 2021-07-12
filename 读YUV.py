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
        #print(len(Y))
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
            #print(len(data[0][0][0]))
            YY=data[0][0]
            #print(len(data[0][0]))

            imgMat = numpy.matrix(data[0][0])
            cv2.imshow('aa',imgMat)
            cv2.waitKey(0)
