# -*-coding=UTF-8-*-
"""
在无参考图下，检测图片质量的方法
"""
import os
import cv2
import numpy as np
np.set_printoptions(threshold=1e6)

from skimage import filters

class BlurDetection:

    def __init__(self, strDir):
        #print("图片检测对象已经创建...")
        self.strDir = strDir


    def _getAllImg(self, strType='jpg'):
        """
        根据目录读取所有的图片
        :param strType: 图片的类型
        :return:  图片列表
        """
        names = []
        for root, dirs, files in os.walk(self.strDir):  # 此处有b[yug  如果调试的数据还放在这里，将会递归的遍历所有文件
            for file in files:
                 if file.endswith('jpg'):
                    names.append(str(file))
        print(names)
        return names

    def _imageToMatrix(self, image):
        """
        根据名称读取图片对象转化矩阵
        :param strName:
        :return: 返回矩阵
        """
        imgMat = np.matrix(image)
        return imgMat
    def _cal(self,image):
        imgMat = self._imageToMatrix(img2gray) / 256.0
        bytes = imgMat.tobytes()
        cbytes = c_ubyte(bytes)
        print(bytes)
        x, y = imgMat.shape
        self.addr(0, 0, x, y, byref(cbytes), x, y)
        score = 0
        for i in range(x - 2):
            for j in range(y - 2):
                score += (imgMat[i + 2, j] - imgMat[i, j]) ** 2
        return score
    def _blurDetection(self,image):

        img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 将图片压缩为单通道的灰度图
        # img2gray = image

        imgMat=self._imageToMatrix(img2gray)
        # print(imgMat)
        # cv2.imshow('1',imgMat)
        # cv2.waitKey(0)
        #imgMat.tofile('imgMat.bin')

        x, y = imgMat.shape
        # x = 135
        # y = 169
        # print(x,y)
        shift =int(x/56)
        # shift=3#yanzhengzhihui
        if shift == 0:
            shift = 1
        # print(shift)
        score1 = 0
        score2 = 0
        tmp=0
        for i in range(0,(x-shift),shift):
            for j in range(0,(y-shift),shift):
        # for i in range(0,(shift*54),shift):
        #     for j in range(0,(shift*54),shift):
                #print(i,j,shift)
                #print(shift)
                # print(imgMat[i+shift,j])
                # print(imgMat[i,j])
                # print(imgMat[i,j+shift])
                # score += (imgMat[i+shift, j] - imgMat[i, j]) ** 2 #hang -
                tmp += 1
                score1 += int(int(imgMat[i + shift, j]) - int(imgMat[i, j])) ** 2
                # print(int(imgMat[i + shift, j]) - int(imgMat[i, j]))
                score2 += int(int(imgMat[i, j + shift]) - int(imgMat[i, j])) ** 2
                # print(int(imgMat[i, j + shift]) - int(imgMat[i, j]))
                # print(score1, score2)

        # print(tmp)
        # print(score1, score2)
        score1= 10000*score1/tmp/65536
        #print(score1)
        #score1 = (("{:0>5d}".format(score1)))
        score2 = 10000*score2/tmp/65536
        # print(score1,score2)
        # cv2.imshow('a', img2gray)
        # cv2.waitKey(0)
        #score2 = (("{:0>5d}".format(score2)))

        #print(score)
        #print()
        #print(tmp)
        #if tmp==0:
            #print(x)

        return score1,score2

    def _lapulaseDetection(self, image):
        """
        :param strdir: 文件所在的目录
        :param name: 文件名称
        :return: 检测模糊后的分数
        """
        # step1: 预处理
        #img2gray, reImg = self.preImgOps(image)
        img2gray = self.preImgOps(image)
        # step2: laplacian算子 获取评分
        resLap = cv2.Laplacian(img2gray, cv2.CV_64F)
        #resLap = cv2.Laplacian(img2gray, cv2.CV_16U)
        score = resLap.var()
        print("Laplacian score of given image is ", str(score))
        # strp3: 绘制图片并保存  不应该写在这里  抽象出来   这是共有的部分
        #newImg = self._drawImgFonts(reImg, str(score))
        #newDir = self.strDir + "/１/"
        # if not os.path.exists(newDir):
        #     pass
            #os.makedirs(newDir)
        #newPath = newDir + image
        # 显示
        #cv2.imwrite(newPath, newImg)  # 保存图片
        #cv2.imshow(image, newImg)
        #cv2.waitKey(0)

        # step3: 返回分数
        return score

    def _SMDDetection(self, imgName):

        # step 1 图像的预处理
        img2gray, reImg = self.preImgOps(imgName)
        f=self._imageToMatrix(img2gray)/255.0
        x, y = f.shape
        score = 0
        for i in range(x - 1):
            for j in range(y - 1):
                score += np.abs(f[i+1,j]-f[i,j])+np.abs(f[i,j]-f[i+1,j])
        # strp3: 绘制图片并保存  不应该写在这里  抽象出来   这是共有的部分
        score=score/100
        newImg = self._drawImgFonts(reImg, str(score))
        newDir = self.strDir + "/_SMDDetection_/"
        if not os.path.exists(newDir):
            os.makedirs(newDir)
        newPath = newDir + imgName
        cv2.imwrite(newPath, newImg)  # 保存图片
        cv2.imshow(imgName, newImg)
        cv2.waitKey(0)
        return score

    def _SMD2Detection(self, imgName):
        """
        灰度方差乘积
        :param imgName:
        :return:
        """
        # step 1 图像的预处理
        img2gray, reImg = self.preImgOps(imgName)
        f=self._imageToMatrix(img2gray)/255.0
        x, y = f.shape
        score = 0
        for i in range(x - 1):
            for j in range(y - 1):
                score += np.abs(f[i+1,j]-f[i,j])*np.abs(f[i,j]-f[i,j+1])
        # strp3: 绘制图片并保存  不应该写在这里  抽象出来   这是共有的部分
        score=score
        newImg = self._drawImgFonts(reImg, str(score))
        newDir = self.strDir + "/_SMD2Detection_/"
        if not os.path.exists(newDir):
            os.makedirs(newDir)
        newPath = newDir + imgName
        cv2.imwrite(newPath, newImg)  # 保存图片
        cv2.imshow(imgName, newImg)
        cv2.waitKey(0)
        return score
    def _Variance(self, imgName):
        """
               灰度方差乘积
               :param imgName:
               :return:
               """
        # step 1 图像的预处理
        img2gray, reImg = self.preImgOps(imgName)
        f = self._imageToMatrix(img2gray)

        # strp3: 绘制图片并保存  不应该写在这里  抽象出来   这是共有的部分
        score = np.var(f)
        newImg = self._drawImgFonts(reImg, str(score))
        newDir = self.strDir + "/_Variance_/"
        if not os.path.exists(newDir):
            os.makedirs(newDir)
        newPath = newDir + imgName
        cv2.imwrite(newPath, newImg)  # 保存图片
        cv2.imshow(imgName, newImg)
        cv2.waitKey(0)
        return score
    def _Vollath(self,imgName):
        """
                       灰度方差乘积
                       :param imgName:
                       :return:
                       """
        # step 1 图像的预处理
        img2gray, reImg = self.preImgOps(imgName)
        f = self._imageToMatrix(img2gray)
        source=0
        x,y=f.shape
        for i in range(x-1):
            for j in range(y):
                source+=f[i,j]*f[i+1,j]
        source=source-x*y*np.mean(f)
        # strp3: 绘制图片并保存  不应该写在这里  抽象出来   这是共有的部分

        newImg = self._drawImgFonts(reImg, str(source))
        newDir = self.strDir + "/_Vollath_/"
        if not os.path.exists(newDir):
            os.makedirs(newDir)
        newPath = newDir + imgName
        cv2.imwrite(newPath, newImg)  # 保存图片
        cv2.imshow(imgName, newImg)
        cv2.waitKey(0)
        return source
    def _Tenengrad(self,imgName):
        """
                       灰度方差乘积
                       :param imgName:
                       :return:
                       """
        # step 1 图像的预处理
        img2gray, reImg = self.preImgOps(imgName)
        #img2gray = self.preImgOps(imgName)
        f = self._imageToMatrix(img2gray)

        a = filters.sobel(f)
        source = np.average(a)
        # x,y = a.shape
        # shift = 1
        # score1 = 0
        # score2 = 0
        # tmp = 0
        # for i in range(0,(x-shift),shift):
        #
        #
        #     for j in range(0,y-shift,shift):
        #         # print(i)
        #         # print(shift)
        #         # print(imgMat[i+shift,j])
        #         # print(imgMat[i,j])
        #         # print(imgMat[i,j+shift])
        #         # score += (imgMat[i+shift, j] - imgMat[i, j]) ** 2 #hang -
        #         score1 += int(int(a[i + shift, j]) - int(a[i, j])) ** 2
        #         score2 += int(int(a[i, j + shift]) - int(a[i, j])) ** 2
        #
        #         tmp = tmp + 1
        #         print(tmp)
        # #score1= 10000*score1/tmp/65536
        # print(score1)
        # #score1 = (("{:0>5d}".format(score1)))
        # #score2 = 10000*score2/tmp/65536
        # print(score2)
        # #cv2.imwrite('/home/gubo/8/buqingchu/' + str(source) + '.png', tmp)

        source=np.sum(a**2)
        print(source)
        source=np.sqrt(source)
        print(source)
        # strp3: 绘制图片并保存  不应该写在这里  抽象出来   这是共有的部分

        #newImg = self._drawImgFonts(reImg, str(source))

        cv2.imshow('', a)
        cv2.waitKey(0)
        return source

    def Test_Tenengrad(self):
        imgList = self._getAllImg(self.strDir)
        for i in range(len(imgList)):
            score = self._Tenengrad(imgList[i])
            print(str(imgList[i]) + " is " + str(score))

    def Test_Vollath(self):
        imgList = self._getAllImg(self.strDir)
        for i in range(len(imgList)):
            score = self._Variance(imgList[i])
            print(str(imgList[i]) + " is " + str(score))


    def TestVariance(self):
        imgList = self._getAllImg(self.strDir)
        for i in range(len(imgList)):
            score = self._Variance(imgList[i])
            print(str(imgList[i]) + " is " + str(score))

    def TestSMD2(self):
        imgList = self._getAllImg(self.strDir)

        for i in range(len(imgList)):
            score = self._SMD2Detection(imgList[i])
            print(str(imgList[i]) + " is " + str(score))
        return
    def TestSMD(self):
        imgList = self._getAllImg(self.strDir)

        for i in range(len(imgList)):
            score = self._SMDDetection(imgList[i])
            print(str(imgList[i]) + " is " + str(score))
        return

    def TestBrener(self,faceImage):
        score = self._blurDetection(faceImage)
        return score
    def TestCal(self,faceImage):
        score = self._cal(faceImage)
        return score

    def preImgOps(self, imgName):
        """
        图像的预处理操作
        :param imgName: 图像的而明朝
        :return: 灰度化和resize之后的图片对象
        """
        # strPath = self.strDir + imgName
        #
        #
        # img = cv2.imread(strPath)  # 读取图片
        img = imgName

        #cv2.moveWindow("", 1000, 100)
        # cv2.imshow("原始图", img)
        # 预处理操作
        reImg = cv2.resize(img, (80, 80), interpolation=cv2.INTER_CUBIC)  #

        img2gray = cv2.cvtColor(reImg, cv2.COLOR_BGR2GRAY)  # 将图片压缩为单通道的灰度图
        return img2gray, reImg
                # img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # return img2gray

    def _drawImgFonts(self, img, strContent):
        """
        绘制图像
        :param img: cv下的图片对象
        :param strContent: 书写的图片内容
        :return:
        """
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontSize = 5
        # 照片 添加的文字    /左上角坐标   字体   字体大小   颜色        字体粗细
        cv2.putText(img, strContent, (0, 200), font, fontSize, (0, 255, 0), 6)

        return img



    def TestDect(self):
        names = self._getAllImg()
        for i in range(len(names)):
            score = self._lapulaseDetection(names[i])
            print(str(names[i]) + " is " + str(score))
        return