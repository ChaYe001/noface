#!/usr/bin/env python3

"""
 Copyright (c) 2018-2019 LLVISION Corporation

"""
from __future__ import print_function
import sys
from mo.utils.versions_checker import check_python_version  # pylint: disable=no-name-in-module
import os
import argparse
from cli_parser import get_placeholder_shapes, get_tuple_values, get_model_name, \
    get_common_cli_options, get_caffe_cli_options, get_tf_cli_options, get_mxnet_cli_options, get_kaldi_cli_options, \
    get_onnx_cli_options, get_mean_scale_dictionary, parse_tuple_pairs
from argparse import ArgumentParser, SUPPRESS
#import  xml.dom.minidom
import json
from collections import OrderedDict


def print_argv(argv: argparse.Namespace, is_caffe: bool, is_tf: bool, is_mxnet: bool, is_kaldi: bool, is_onnx: bool,
               model_name: str):
    print('Model Optimizer arguments:')
    props = OrderedDict()
    props['common_args'] = get_common_cli_options(model_name)
    if is_caffe:
        props['caffe_args'] = get_caffe_cli_options()
    if is_tf:
        props['tf_args'] = get_tf_cli_options()
    if is_mxnet:
        props['mxnet_args'] = get_mxnet_cli_options()
    if is_kaldi:
        props['kaldi_args'] = get_kaldi_cli_options()
    if is_onnx:
        props['onnx_args'] = get_onnx_cli_options()

    framework_specifics_map = {
        'common_args': 'Common parameters:',
        'caffe_args': 'Caffe specific parameters:',
        'tf_args': 'TensorFlow specific parameters:',
        'mxnet_args': 'MXNet specific parameters:',
        'kaldi_args': 'Kaldi specific parameters:',
        'onnx_args': 'ONNX specific parameters:',
    }

    lines = []
    for key in props:
        lines.append(framework_specifics_map[key])
        for (op, desc) in props[key].items():
            if isinstance(desc, list):
                lines.append('\t{}: \t{}'.format(desc[0], desc[1](getattr(argv, op, 'NONE'))))
            else:
                if op is 'k':
                    default_path = os.path.join(os.path.dirname(sys.argv[0]),
                                                'extensions/front/caffe/CustomLayersMapping.xml')
                    if getattr(args, op, 'NONE') == default_path:
                        lines.append('\t{}: \t{}'.format(desc, 'Default'))
                        continue
                lines.append('\t{}: \t{}'.format(desc, getattr(argv, op, 'NONE')))
    lines.append('Model Optimizer version: \t{}'.format(get_version()))
    print('\n'.join(lines))

def SetJson(cli_parser: argparse.ArgumentParser):
    argv = cli_parser.parse_args()
    global setting
    #jsonstr = '{"version":1,"serviceID": 1,"time_slices": 100,	"modelLen":123,"frame_src": 2,	"serviceType": 1,"data_type": "FP16", "frame_src": 2,"preprocessPara":{"RGBMean": {"alpaG": 127,"alpaR": 127,"alpaB": 127},"scale": 127}}'
    jsonstr = '{"serviceType": 1, "modelLen": 123, "time_slices": 100, "frame_src": 2, "serviceID": 1, "data_type": "FP16", "version": 1}'
    setting = json.loads(jsonstr)
    setting = OrderedDict(sorted(setting.items(), key=lambda t: t[0]))
    # setting = []
    setting['data_type'] = argv.data_type
    # if args.serviceType != None:
    #     serviceType = args.serviceType
    #     setting['serviceType'] = int(serviceType)
    if argv.time_slices != None:
        time_slices = argv.time_slices
        setting['time_slices'] = int(time_slices)
    if argv.input != None:
        frame_src = argv.inputfile
        setting['frame_src'] = int(frame_src)
    setting['modelLen'] = int(modelLen)
    kd = setting
    setting = json.dumps(kd, jsonstr)
def getmodellen():
    global fp,text,modelLen
    fp = open(output_file, 'rb+')
    text = fp.read()
    modelLen = fp.tell()
    print('MO model file size = ' + str(modelLen))
    return modelLen
def compl():
    Description_of_JSONLen = 4
    ModelHeaferLen = 1024
    fp.seek(Description_of_JSONLen)
    jsonfile = setting
    jsonstr1 = bytes(jsonfile, encoding="utf-8")
    fp.write(jsonstr1)
    JsonLen = fp.tell()-Description_of_JSONLen
    jsonlen = JsonLen.to_bytes(length=4, byteorder='little')
    fp.seek(0)
    fp.write(jsonlen)
    fp.seek(ModelHeaferLen)
    fp.write(text)
    LLBlobLen = fp.tell()
    print('LLvision Blob file size = ' + str(LLBlobLen))
    fp.close()

def excute(cli_parser: argparse.ArgumentParser):
    argv = cli_parser.parse_args()
    global output_file
    output_dir = argv.output_dir if argv.output_dir != '.' else os.getcwd()
    model_name = "<UNKNOWN_NAME>"
    if argv.model_name:
        model_name = argv.model_name
    elif argv.input_model:
        model_name = get_model_name(argv.input_model)
    elif is_tf and argv.saved_model_dir:
        model_name = "saved_model"
    elif is_tf and argv.input_meta_graph:
        model_name = get_model_name(argv.input_meta_graph)
    elif is_mxnet and argv.input_symbol:
        model_name = get_model_name(argv.input_symbol)
    model_xml = '{}.xml'.format(os.path.join(output_dir,model_name))
    #print(model_xml)
    print('The xml is \033[1;31m' + model_xml + '\033[0m!')
    blob = os.path.splitext(model_xml)[0] + ".blob"
    if argv.output_blob == None:
        output_file = blob
        print('The bolb is \033[1;31m' + output_file + '\033[0m!')
    else:
        output_file = argv.output_blob
        print('The bolb is \033[1;31m' + output_file + '\033[0m!')

    if argv.VPU_NUMBER_OF_SHAVES == None:
        VPU_NUMBER_OF_SHAVES = ''
    else:
        VPU_NUMBER_OF_SHAVES = ' -VPU_NUMBER_OF_SHAVES ' + str(argv.VPU_NUMBER_OF_SHAVES)

    if argv.VPU_NUMBER_OF_CMX_SLICES == None:
        VPU_NUMBER_OF_CMX_SLICES = ''
    else:
        VPU_NUMBER_OF_CMX_SLICES = ' -VPU_NUMBER_OF_CMX_SLICES ' + str(argv.VPU_NUMBER_OF_CMX_SLICES)

    sop = os.system('../inference_engine/lib/intel64/myriad_compile -m '+ model_xml + ' -VPU_PLATFORM VPU_2480 -o ' + output_file  + VPU_NUMBER_OF_SHAVES + VPU_NUMBER_OF_CMX_SLICES)
    #print(sop)
    if sop == 0:
        # 打开xml文档
        #dom = xml.dom.minidom.parse(argv.model)
        #GetXml_values(dom)
        getmodellen()
        SetJson(get_all_cli_parser())
        compl()

if __name__ == "__main__":
    ret_code = check_python_version()
    if ret_code:
        sys.exit(ret_code)

    from mo.main import main
    import cli_parser
    from cli_parser import get_all_cli_parser  # pylint: disable=no-name-in-module

    #args = cli_parser.get_all_cli_parser()

    main(get_all_cli_parser(), None)
    #
    sys.exit(excute(get_all_cli_parser()))
