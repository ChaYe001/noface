#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:GuBo_LLvision
import os, sys

input_yuv_image_file = '/home/gubo/Downloads/jpg/yuv/'

piclist = os.listdir(input_yuv_image_file)
for pic in piclist:
    picname = pic.split('.')[0]
    picpath = os.path.join(input_yuv_image_file, pic)
    inputname = (picname + '.yuv')
    outname = (picname + '.jpg')
    ff = os.system('ffmpeg -s 1920x1080 -pix_fmt yuv420p -i ' + input_yuv_image_file + inputname + ' ' + input_yuv_image_file + outname)
ff.run()