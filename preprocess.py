#! /usr/bin/env python3

# Copyright(c) 2018 Llvision Corporation.


# from mvnc import mvncapi as mvnc
import numpy
import cv2
import sys

IMAGE_FULL_PATH = '/home/gubo/WorkSpace/red.jpeg'


def preprocess_image(src):
    # scale the image (outputFormatData)
    NETWORK_WIDTH = 112
    NETWORK_HEIGHT = 112
    img = cv2.resize(src, (NETWORK_WIDTH, NETWORK_HEIGHT))
    img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    # adjust values to range between -1.0 and + 1.0

    ilsvrc_mean = [128,128,128]
    # img = img.astype(numpy.float32)
    img[:, :, 0] = (img[:, :, 0] - ilsvrc_mean[0])
    img[:, :, 1] = (img[:, :, 1] - ilsvrc_mean[1])
    img[:, :, 2] = (img[:, :, 2] - ilsvrc_mean[2])
    stdValve = 128
    img = img / stdValve
    print(img[:, :, 0])
    print(img[:, :, 2])
    # img = img[:, :, ::-1]    #convert to RGB
    # return img
    img.astype(numpy.float16).tofile("manypersonfp16.bin")
    cv2.imshow("red", img)
    cv2.waitKey(0)


def main():
    infer_image = cv2.imread(IMAGE_FULL_PATH)

    preprocess_image(infer_image)


if __name__ == "__main__":
    sys.exit(main())

