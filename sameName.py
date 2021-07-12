# -*- coding: utf-8 -*-
import face_recognition
import face_recognition_models
import cv2
import os
#import cv2
#import BlurDetection
from BlurDetection import BlurDetection
from yaw_module import YawDetecction

facefile = "/home/gubo/WorkSpace/face_b/Posface_b/littleface/copy/"
jobs_image = face_recognition.load_image_file('/home/gubo/WorkSpace/face_a/Posface_a/littleface/重复杨幂/'
                                                      '18203blu184_18203yaw0_18203.jpg')
# XiaoMa_image = face_recognition.load_image_file('/home/gubo/WorkSpace/face_b/Posface_a/littleface/'
#                                                         '重复小马哥/21741blu127_21741yaw-16_21741.jpg')
jobs_enconding = face_recognition.face_encodings(jobs_image)[0]
# XiaoMa_enconding = face_recognition.face_encodings(XiaoMa_image)[0]
#successfile = "/home/gubo/laowang/"
def blur_detction(testImg):
    tmp = BlurDetection('')
    score = tmp.TestBrener(testImg)
    return int(score)
piclist = os.listdir(facefile)
#successlist = os.listdir(successfile)
i = 0
for okname in piclist:
    if okname.endswith('jpg'):
        print(okname)
        img = cv2.imread(facefile + okname)

        unknown_image = face_recognition.load_image_file(facefile + okname)
        sp = img.shape
        print(sp)
        if len(face_recognition.face_encodings(unknown_image)) ==0:
            pass
        else:
            unknown_enconding = face_recognition.face_encodings(unknown_image)[0]
        #print(unknown_enconding)
            results = face_recognition.compare_faces([jobs_enconding], unknown_enconding)
        #labels = ['jobs']
            print(results)

            if results[0]:
                os.system('mv -f' + ' ' + facefile + okname + ' ' + '/home/gubo/WorkSpace/face_a/Posface_a/littleface/1/' + okname)
        i = i + 1
        print('-------' + str(i) + '-------')
            #print(unknown_image)
print(i)