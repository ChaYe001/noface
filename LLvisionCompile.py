#!/usr/bin/env python3
"""
 Copyright (C) 2018-2019 LLVISION Corporation
 """

from __future__ import print_function
import sys
import os
from argparse import ArgumentParser, SUPPRESS
import time
#import logging as log



def build_argparser():
    parser = ArgumentParser(add_help=False)
    args = parser.add_argument_group('Options')
    args.add_argument('-h', '--help',action='help', default=SUPPRESS, help='Show this help message and exit.')
    args.add_argument("-m", "--model",help="Required. Path to an .xml file with a trained model.",
                      required=True, type=str)
    args.add_argument("-i", "--input", help="Optional. file from camera frame or image,Supported = 1,2",default=2)

    args.add_argument("-s","--serviceType", help="Optional. serviceType is common or private,Supported = 1,2",default=2)
    args.add_argument("-pp","--plugin", help="Optional. Path to a plugin folder", type=str, default=None)
    args.add_argument("-o","--output", help="Optional. Path to the output file.default=<model_xml_file>.blob", type=str )
    #args.add_argument("-c", help="Optional. Path to the configuration file.", type=str, default="config")
    args.add_argument("-VPU_NUMBER_OF_SHAVES","--VPU_NUMBER_OF_SHAVES", help="Optional. Specifies number of shaves.Should be set with VPU_NUMBER_OF_CMX_SLICES")
    args.add_argument("-VPU_NUMBER_OF_CMX_SLICES","--VPU_NUMBER_OF_CMX_SLICES", help="Optional. Specifies number of CMX slices.Should be set with VPU_NUMBER_OF_SHAVES")


    return parser

import  xml.dom.minidom
import json
from collections import OrderedDict
def loadJsonData():
    f = open("preprocessPara.json", encoding='utf-8')
    #global setting
    setting = json.load(f)
    return setting



#获取xml文档元素对象：data_type,mean_values,scale,
def GetXml_values(dom):

    root = dom.documentElement

    data_typelist = root.getElementsByTagName('data_type')
    data_type = data_typelist[0]
    global FP
    FP = data_type.getAttribute("value")
    print(FP)

    mean_scale_valueslist = root.getElementsByTagName('mean_scale_values')
    mean_scale_values = mean_scale_valueslist[0]
    global Mean_scale
    Mean_scale = mean_scale_values.getAttribute("value")
    print(Mean_scale)

    mean_valueslist = root.getElementsByTagName('mean_values')
    mean_value = mean_valueslist[0]
    Mean = mean_value.getAttribute("value")
    global mean
    mean = Mean.strip('[]').split(',')
    print(mean)

    scalelist = root.getElementsByTagName('scale')
    scale = scalelist[0]
    global Scale
    Scale = scale.getAttribute("value")
    print(Scale)

#获取json模板数据
def GetJson_values():

    serviceTypeLoad = loadJsonData()['serviceType']
    print('serviceType: ' + str(serviceTypeLoad))
    frame_srcLoad = loadJsonData()['frame_src']
    print('frame_src: ' + str(frame_srcLoad))
    data_typeLoad = loadJsonData()['data_type']
    print('data_type: ' + str(data_typeLoad))

    alpaRLoad = loadJsonData()['preprocessPara']['RGBMean']['alpaR']
    print('alpaR: ' + str(alpaRLoad))
    alpaGLoad = loadJsonData()['preprocessPara']['RGBMean']['alpaG']
    print('alpaG: ' + str(alpaGLoad))
    alpaBLoad = loadJsonData()['preprocessPara']['RGBMean']['alpaB']
    print('alpaB: ' + str(alpaBLoad))
    scaleLoad = loadJsonData()['preprocessPara']['scale']
    print('scale: ' + str(scaleLoad))
#将获取的xml文件数据导入json
def SetJson():

    f = open("preprocessPara.json", encoding='utf-8')
    # global setting
    setting = json.load(f)
    after = OrderedDict()
    after = []
    setting['data_type'] = FP

    #setting['serviceType'] = serviceType
    #setting['frame_src'] = frame_src
    setting['preprocessPara']['RGBMean']['alpaR'] = float(mean[0])
    setting['preprocessPara']['RGBMean']['alpaG'] = float(mean[1])
    setting['preprocessPara']['RGBMean']['alpaB'] = float(mean[2])
    setting['preprocessPara']['scale'] = float(Scale)
    after = setting
    with open('preprocessPara.json', 'w') as f:
        setting = json.dump(after, f)



def main():

    #log.basicConfig(format="[ %(levelname)s ] %(message)s", level=log.INFO, stream=sys.stdout)
    args = build_argparser().parse_args()
    model_xml = args.model
    print('The xml is \033[1;31m' + model_xml + '\033[0m!')
    model_bin = os.path.splitext(model_xml)[0] + ".bin"
    blob = os.path.splitext(model_xml)[0] + ".blob"
    # print(blob)
    if args.output == None:
        output_file = blob
        print('The bolb is \033[1;31m' + output_file + '\033[0m!')

    else:
        output_file = args.output
        print('The bolb is \033[1;31m' + output_file + '\033[0m!')
    # 打开xml文档
    dom = xml.dom.minidom.parse(args.model)
    GetXml_values(dom)
    GetJson_values()
    SetJson()
    os.system('./myriad_compile -m '+ model_xml + ' -VPU_PLATFORM VPU_2480 -o ' +output_file )
    os.system('./paraModelConvert preprocessPara.json '+ output_file)

if __name__ == '__main__':
    sys.exit(main() or 0)
