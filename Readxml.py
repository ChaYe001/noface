#coding=utf-8
import  xml.dom.minidom
import json
import os
from collections import OrderedDict
# def loadJsonData():
#     f = open("preprocessPara.json", encoding='utf-8')
#     #global setting
#     setting = json.load(f)
#     return setting

#打开xml文档
dom = xml.dom.minidom.parse('/home/gubo/WorkSpace/open_model_zoo-master/model_downloader/Transportation/object_detection/face/pruned_mobilenet_reduced_ssd_shared_weights/dldt/face-detection-adas-0001.xml')
#dom = xml.dom.minidom.parse('/home/gubo/WorkSpace/NNM/mobilenet_ssd/MobileNetSSD_deploy.xml')
#dom = xml.dom.minidom.parse('/home/gubo/WorkSpace/NNM/squeezenet1.1_FP16/squeezenet1.1.xml')

#获取xml文档元素对象：data_type,mean_values,scale,
def GetXml_values():

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
    mean = Mean.strip('data[()]').split(',')
    print(mean)

    scalelist = root.getElementsByTagName('scale')
    if scalelist == []:
        scalelist = root.getElementsByTagName('scale_values')
    scale = scalelist[0]
    global Scale
    Scale = scale.getAttribute("value")
    Scale = Scale.strip('data[()]').split(',')

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
# #将获取的xml文件数据导入json
# def SetJson():
#
#     f = open("preprocessPara.json", encoding='utf-8')
#     # global setting
#     setting = json.load(f)
#     after = OrderedDict()
#     after = []
#     setting['data_type'] = FP
#
#     #setting['serviceType'] = serviceType
#     #setting['frame_src'] = frame_src
#     setting['preprocessPara']['RGBMean']['alpaR'] = float(mean[0])
#     setting['preprocessPara']['RGBMean']['alpaG'] = float(mean[1])
#     setting['preprocessPara']['RGBMean']['alpaB'] = float(mean[2])
#     setting['preprocessPara']['scale'] = float(Scale)
#     after = setting
#     with open('preprocessPara.json', 'w') as f:
#         setting = json.dump(after, f)

def SetJson():
    jsonstr = '{"version":1,"serviceID": 1,"time_slices": 100,	"modelLen":123,"frame_src": 2,	"serviceType": 1,"data_type": "FP16", "frame_src": 2,"preprocessPara":{"RGBMean": {"alpaG": 127,"alpaR": 127,"alpaB": 127},"scale": 127}}'
    # if not os.path.exists(jsonfile):
    #     a = open(jsonfile, 'w')
    #     a.close()
    # f = open("preprocessPara1.json", encoding='utf-8')
    # global setting
    #jsonfile = json.dumps(jsonstr)
    setting = json.loads(jsonstr)
    setting = OrderedDict(sorted(setting.items(),key=lambda t:t[0]))
    #setting = []
    setting['data_type'] = FP

    #setting['serviceType'] = serviceType
    #setting['frame_src'] = frame_src

    if mean[0] == '':
        mean0 = 0
        mean1 = 0
        mean2 = 0
    else:
        mean0 = mean[0]
        mean1 = mean[1]
        mean2 = mean[2]
    setting['preprocessPara']['RGBMean']['alpaR'] = float(mean0)
    setting['preprocessPara']['RGBMean']['alpaG'] = float(mean1)
    setting['preprocessPara']['RGBMean']['alpaB'] = float(mean2)
    if Scale[0] == '':
        Scale[0] = 1
    setting['preprocessPara']['scale'] = float(Scale[0])
    kd = setting
    setting = json.dumps(kd,jsonstr)
    print(setting)
    # with open(jsonfile, 'w') as f:
    #     setting = json.dump(after, f)

GetXml_values()
#GetJson_values()
SetJson()
