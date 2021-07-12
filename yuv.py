import cv2
import numpy
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
    print (dims[0])
    print (dims[1])
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
    facefile = "/home/gubo/1/1/caiji/0000/yuv/"
    piclist = os.listdir(facefile)

    for okname in piclist:
        if okname.endswith('yuv'):

        data=yuv_import(facefile + okname, (height, width), 1, 0)
        YY=data[0][0]


        imgMat = numpy.matrix(YY)
        #print(imgMat)

        face = imgMat[229:229+194,453:453+194]
        cv2.imshow("1",face)
        cv2.waitKey(0)
        x, y = face.shape
        print(x, y)
        shift = int(x / 56)
        if shift == 0:
            shift = 1
        print(shift)
        score1 = 0
        score2 = 0
        temp = 0

        for i in range(0, (x - shift),shift):

            for j in range(0, (y - shift),shift):
                temp += 1

                score1 += int(int(face[i + shift, j]) - int(face[i, j])) ** 2
                score2 += int(int(face[i , j + shift]) - int(face[i, j])) ** 2
        print(temp)
        score1 = 10000*score1/temp/65536
        score2 = 10000 * score2 / temp / 65536
        # score = 300*300*score/65536/temp
        score1 = round(score1, 2)
        score2 = round(score2, 2)
        print(score1,score2)

