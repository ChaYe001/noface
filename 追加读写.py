import numpy
fp = open('/home/gubo/wang.bin','rb+')
text = fp.read()
text = text.hex()
text = float(text)
jsonlen = text.to_bytes(length=4, byteorder='little')
fp.write(jsonlen)
fp.close()

print(text)
modelLen = fp.tell()
print('MO model file size = ' + str(modelLen))
# fp.seek(4)
# #jsonfile = '{"version":1,"serviceID":1,"time_slices": 100,	"modelLen":123,"frame_src": 2,	"serviceType": 1,"data_type": "FP16","frame_src": 2,"preprocessPara":{"RGBMean": {alpaG": 127.5,"alpaR": 127.5,"alpaB": 127.5},"scale": 127.5}}'
# jsonfile = 'm'
# jsonstr = bytes(jsonfile, encoding = "utf-8")
#
# fp.write(jsonstr)

# JsonLen = fp.tell()
# print(JsonLen)
# JsonLen = "{:0>4d}".format(JsonLen)
# JsonLen = int(JsonLen)
# print(type(JsonLen))
# jsonlen = bytes(JsonLen, encoding = "u32")
ererybinLen = 4
Description_of_JSONLen = 28
#ModelHeaferLen = 1024
fp.seek(Description_of_JSONLen)
#jsonfile = setting
fp.seek(0)
MobileNetSSD_deployparambinLen = 6548
mobileNetSSD_deployparambinLen = MobileNetSSD_deployparambinLen.to_bytes(length=4, byteorder='little')
fp.write(mobileNetSSD_deployparambinLen)
print('MobileNetSSD_deploy.param.bin size = ' + str(MobileNetSSD_deployparambinLen))

#fp.seek(ererybinLen)
MobileNetSSD_deploybinLen = 9434020
mobileNetSSD_deploybinLen = MobileNetSSD_deploybinLen.to_bytes(length=4, byteorder='little')
fp.write(mobileNetSSD_deploybinLen)
print('MobileNetSSD_deploy.bin size = ' + str(MobileNetSSD_deploybinLen))

#fp.seek(ererybinLen*2)
FaceYawparambinLen = 5456
faceYawparambinLen = FaceYawparambinLen.to_bytes(length=4, byteorder='little')
fp.write(faceYawparambinLen)
print('FaceYaw.param.bin size = ' + str(FaceYawparambinLen))

#fp.seek(ererybinLen*3)
FaceYawbinLen = 959912
faceYawbinLen = FaceYawbinLen.to_bytes(length=4, byteorder='little')
fp.write(faceYawbinLen)
print('faceYaw.bin size = ' + str(FaceYawbinLen))

#fp.seek(ererybinLen*4)
paramstdbinLen = 496
ParamstdbinLen = paramstdbinLen.to_bytes(length=4, byteorder='little')
fp.write(ParamstdbinLen)
print('param-std.bin size = ' + str(paramstdbinLen))

#fp.seek(ererybinLen*5)
FaceKpsparambinLen = 1168
faceKpsparambinLen =  FaceKpsparambinLen.to_bytes(length=4, byteorder='little')
fp.write( faceKpsparambinLen)
print(' FaceKps.param.bin size = ' +  str(FaceKpsparambinLen))

#fp.seek(ererybinLen*6)
FaceKpsbinLen = 1006360
faceKpsbinLen = FaceKpsbinLen.to_bytes(length=4, byteorder='little')
fp.write(faceKpsbinLen)
print('FaceKps.bin size = ' + str(FaceKpsbinLen))

#fp.seek(Description_of_JSONLen)
fp.write(text)
LLBlobLen = fp.tell()
print('LLvision Blob file size = ' + str(LLBlobLen))
fp.close()
# jsonlen = JsonLen.to_bytes(length=4, byteorder='little')
# # jsonlen = JsonLen.to_bytes(length=4,　byteorder='little')
# fp.seek(0)
# fp.write(jsonlen)
# fp.seek(1024)
# fp.write(text)
# print(fp.tell())

# fp.close()
