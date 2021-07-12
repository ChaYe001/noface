#!/usr/bin/env python3
"""
 Copyright (C) 2018-2019 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from __future__ import print_function
import sys
import os
from argparse import ArgumentParser, SUPPRESS
import cv2
import time
import logging as log

from openvino.inference_engine import IENetwork, IECore
from BlurDetection import BlurDetection
import numpy

def build_argparser():
    parser = ArgumentParser(add_help=False)
    args = parser.add_argument_group('Options')
    args.add_argument('-h', '--help', action='help', default=SUPPRESS, help='Show this help message and exit.')
    args.add_argument("-m", "--model", help="Required. Path to an .xml file with a trained model.",
                      type=str,default='/home/gubo/openvino_models1/face/160/face_detect/v3/deploy.xml')
    args.add_argument("-m_R", "--model_R", help="Required. Path to an .xml file with a trained model.",
                      type=str, default='/home/gubo/openvino_models1/face/160/llvision_model_myriadX/keypoints/keypoints.xml')
    args.add_argument("-i", "--input",
                      help="Required. Path to video file or image. 'cam' for capturing video stream from camera",
                      required=True, type=str)
    args.add_argument("-l", "--cpu_extension",
                      help="Optional. Required for CPU custom layers. Absolute path to a shared library with the "
                           "kernels implementations.", type=str, default=None)
    args.add_argument("-d", "--device",
                      help="Optional. Specify the target device to infer on; CPU, GPU, FPGA, HDDL or MYRIAD is "
                           "acceptable. The demo will look for a suitable plugin for device specified. "
                           "Default value is CPU", default="MYRIAD", type=str)
    args.add_argument("--labels", help="Optional. Path to labels mapping file", default=None, type=str)
    args.add_argument("-pt", "--prob_threshold", help="Optional. Probability threshold for detections filtering",
                      default=0.5, type=float)

    return parser
def blur_detction(testImg):
    tmp = BlurDetection('')
    score1, score2 = tmp._blurDetection(testImg)
    return score1, score2

def calblur(img):
    sp = img.shape
    y = sp[0] * 0.15
    h = sp[0] * 0.70
    x = sp[1] * 0.15

    w = sp[1] * 0.7
    testImg = img[int(y):int(y + h), int(x):int(x + w)]
    score1, score2 = blur_detction(testImg)
    score1 = round(score1, 2)
    score2 = round(score2, 2)
    return score1,score2
        # return getdetectresult()
        # cv2.imwrite(successfile3 + str(score1) + '-' + str(score2) + '-' + okname, testImg)
def startMYIRAD():
    log.basicConfig(format="[ %(levelname)s ] %(message)s", level=log.INFO, stream=sys.stdout)
    # global args

    model_xml = args.model
    modelR_xml = args.model_R
    model_bin = os.path.splitext(model_xml)[0] + ".bin"
    modelR_bin = os.path.splitext(modelR_xml)[0] + ".bin"

    log.info("Creating Inference Engine...")
    ie = IECore()
    if args.cpu_extension and 'CPU' in args.device:
        ie.add_extension(args.cpu_extension, "CPU")
    # Read IR
    log.info("Loading network files:\n\t{}\n\t{}".format(model_xml, model_bin))
    net = IENetwork(model=model_xml, weights=model_bin)
    # net_R = IENetwork(model=modelR_xml, weights=modelR_bin)
    ###cpu可用
    # if "CPU" in args.device:
    #     supported_layers = ie.query_network(net, "CPU")
    #     not_supported_layers = [l for l in net.layers.keys() if l not in supported_layers]
    #     if len(not_supported_layers) != 0:
    #         log.error("Following layers are not supported by the plugin for specified device {}:\n {}".
    #                   format(args.device, ', '.join(not_supported_layers)))
    #         log.error("Please try to specify cpu extensions library path in sample's command line parameters using -l "
    #                   "or --cpu_extension command line argument")
    #         sys.exit(1)

    img_info_input_blob = None
    global feed_dict
    feed_dict = {}
    for blob_name in net.inputs:
        if len(net.inputs[blob_name].shape) == 4:
            global input_blob
            input_blob = blob_name
        elif len(net.inputs[blob_name].shape) == 2:
            img_info_input_blob = blob_name
        else:
            raise RuntimeError("Unsupported {}D input layer '{}'. Only 2D and 4D input layers are supported"
                               .format(len(net.inputs[blob_name].shape), blob_name))

    assert len(net.outputs) == 1, "Demo supports only single output topologies"
    global out_blob
    out_blob = next(iter(net.outputs))
    log.info("Loading IR to the plugin...")
    global exec_net
    exec_net = ie.load_network(network=net, num_requests=2, device_name=args.device)
    # Read and pre-process input image
    global n, c, h, w
    n, c, h, w = net.inputs[input_blob].shape
    if img_info_input_blob:
        feed_dict[img_info_input_blob] = [h, w, 1]
    #
    # img_info_input_blob_R = None
    # global feed_dict_R
    # feed_dict_R = {}
    # for blob_name_R in net_R.inputs:
    #     if len(net_R.inputs[blob_name_R].shape) == 4:
    #         global input_blob_R
    #         input_blob_R = blob_name_R
    #     elif len(net_R.inputs[blob_name_R].shape) == 2:
    #         img_info_input_blob_R = blob_name_R
    #     else:
    #         raise RuntimeError("Unsupported {}D input layer '{}'. Only 2D and 4D input layers are supported"
    #                            .format(len(net_R.inputs[blob_name_R].shape), blob_name_R))
    #
    # assert len(net.outputs) == 1, "Demo supports only single output topologies"
    # global out_blob_R
    # out_blob_R = next(iter(net_R.outputs))
    # log.info("Loading R-IR to the plugin...")
    # global exec_net_R
    # exec_net_R = ie.load_network(network=net_R, num_requests=1, device_name=args.device)
    # # Read and pre-process input image
    # global n_R, c_R, h_R, w_R
    # n_R, c_R, h_R, w_R = net_R.inputs[input_blob_R].shape
    # if img_info_input_blob_R:
    #     feed_dict_R[img_info_input_blob_R] = [h_R, w_R, 1]
def yaw():
    inf_start = time.time()
    global next_frame, frame
    # Main sync point:
    # in the truly Async mode we start the NEXT infer request, while waiting for the CURRENT to complete
    # in the regular mode we start the CURRENT request and immediately wait for it's completion
    if is_async_mode:
        in_frame = cv2.resize(next_frame, (w, h))
        in_frame = in_frame.transpose((2, 0, 1))  # Change data layout from HWC to CHW
        in_frame = in_frame.reshape((n, c, h, w))
        feed_dict[input_blob] = in_frame
        exec_net.start_async(request_id=next_request_id, inputs=feed_dict)
    else:
        in_frame = cv2.resize(frame, (w, h))
        in_frame = in_frame.transpose((2, 0, 1))  # Change data layout from HWC to CHW
        # in_frame = in_frame.reshape((n, c, h, w))
        feed_dict[input_blob] = in_frame
        exec_net.start_async(request_id=cur_request_id, inputs=feed_dict)

    if exec_net.requests[cur_request_id].wait(-1) == 0:
        inf_end = time.time()
        global det_time
        det_time = inf_end - inf_start
        # print("time123: " + str(det_time*1000))
        # Parse detection results of the current request
        global res
        res = exec_net.requests[cur_request_id].outputs[out_blob]
        for obj in res[0][0]:
            # if 0.5< obj[2] <= args.prob_threshold:
            #     # print('facescore:' + str(obj[2]))
            #     global ymin, ymax, xmin, xmax, i, j
            #     xmin = int(obj[3] * initial_w)
            #     ymin = int(obj[4] * initial_h)
            #     xmax = int(obj[5] * initial_w)
            #     ymax = int(obj[6] * initial_h)
            #     # cv2.imwrite('ada.jpg', frame)
            #     # print(xmax,xmin,ymax,ymin)
            #     if xmin < 0:
            #         xmax = xmax - xmin
            #         xmin = 0
            #     if ymin < 0:
            #         ymax = ymax - ymin
            #         ymin = 0
            #
            #
            #
            #         # print('a-' + str(score1) + '-' + str(score2))
            #     class_id = int(obj[1])
            #     # Draw box and label\class_id
            #     color = (min(class_id * 12.5, 255), min(class_id * 7, 255), min(class_id * 5, 255))
            #     cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
            #     det_label = labels_map[class_id] if labels_map else str(class_id)
            #     cv2.putText(frame, det_label + ' ' + str(round(obj[2] * 100, 1)) + ' %', (xmin, ymin - 7),
            #                 cv2.FONT_HERSHEY_COMPLEX, 0.6, color, 1)
            #     cv2.imwrite('/media/gubo/DATADRIVE0/work/face_log1/' + str(xmax - xmin) + '_' + str(obj[2]) + '_' + str(j) + '.jpg',
            #                 frame[ymin:ymax, xmin:xmax])
            #     cv2.imwrite('/media/gubo/DATADRIVE0/work/face_log1/1/' + str(xmax - xmin) + '_' + str(obj[2]) + '_' + str(j) + '.jpg',
            #                 frame)
            #     j += 1
            #     break
            # Draw only objects when probability more than specified threshold
            if obj[2] > args.prob_threshold:
                global ymin, ymax, xmin, xmax,i
                xmin = int(obj[3] * initial_w)
                ymin = int(obj[4] * initial_h)
                xmax = int(obj[5] * initial_w)
                ymax = int(obj[6] * initial_h)
                # cv2.imwrite('ada.jpg', frame)
                # print(xmax,xmin,ymax,ymin)
                if xmin < 0:
                    xmax = xmax - xmin
                    xmin = 0
                if ymin < 0:
                    ymax = ymax - ymin
                    ymin = 0
                wd = xmax - xmin
                hd = ymax - ymin

                xxmin = xmin + int(0.15*wd)
                xxmax = xmax + int(0.15*wd)
                yymin = ymin + int(0.15*wd)
                yymax = ymax + int(0.15*wd)
                calbluframe = frame[yymin:yymax, xxmin:xxmax]
                score1, score2 = calblur(calbluframe)
                score = numpy.var([score1, score2])
                score = round(score, 2)
                # if wd <=60:
                #     score = score1 = score2 = 0
                defi = 1

                if score1 >= defi or score2 >= defi:
                    # print('a-' + str(score1) + '-' + str(score2))
                    class_id = int(obj[1])
                    # Draw box and label\class_id
                    color = (min(class_id * 12.5, 255), min(class_id * 7, 255), min(class_id * 5, 255))
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
                    det_label = labels_map[class_id] if labels_map else str(class_id)
                    cv2.putText(frame, det_label + ' ' + str(round(obj[2] * 100, 1)) + ' %', (xmin, ymin - 7),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, color, 1)
                    cv2.imwrite('/media/gubo/DATADRIVE0/work/face_log/' + str(obj[2]) + '_' + str(xmax - xmin) + '_' + str(i) + '.jpg',
                                frame[ymin:ymax, xmin:xmax])
                    # cv2.imwrite('/media/gubo/DATADRIVE0/work/face_log/1/' + str(xmax - xmin) + '_' + str(i) + '.jpg',
                    #             frame)
                    i += 1
                elif score1 < 0.2 * defi or score2 < 0.2 * defi:
                    # print('b-' + str(score) + '-' + str(score2))
                    # print(obj[2])
                    pass
                    # return getdetectresult()
                    # cv2.imwrite(successfile + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + okname, testImg)
                elif score <= 6:
                    # print('c-' + str(score) + '-' + str(score2))
                    class_id = int(obj[1])
                    # Draw box and label\class_id
                    color = (min(class_id * 12.5, 255), min(class_id * 7, 255), min(class_id * 5, 255))
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
                    det_label = labels_map[class_id] if labels_map else str(class_id)
                    cv2.putText(frame, det_label + ' ' + str(round(obj[2] * 100, 1)) + ' %', (xmin, ymin - 7),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, color, 1)
                    # print(obj[2])
                    # cv2.imwrite(successfile2 + str(score) + '-' + str(score1) + '-' + str(score2) + '-' + okname, testImg)
                else:
                    # print('d-' + str(score) + '-' + str(score2))
                    pass
                ###keypoint计算
                keyframe = frame[ymin:ymax, xmin:xmax]


                # in_frame_R = cv2.resize(keyframe, (w_R, h_R))
                # # print(w_R, h_R)
                # in_frame_R = cv2.cvtColor(in_frame_R, cv2.COLOR_BGR2GRAY)
                # # in_frame_R = in_frame_R.transpose((2, 0, 1))  # Change data layout from HWC to CHW
                # # in_frame_R = in_frame_R.reshape((n_R, c_R, h_R, w_R))
                # feed_dict_R[input_blob_R] = in_frame_R
                # exec_net_R.start_async(request_id=0, inputs=feed_dict_R)
                # if exec_net_R.requests[0].wait(-1) == 0:
                #
                #     res_R = exec_net_R.requests[0].outputs[out_blob_R]
                    # print('===========================================')
                    # print(res_R[0])
                    # print('===========================================')


        # Draw performance stats
        inf_time_message = "Inference time: N\A for async mode" if is_async_mode else \
            "Inference time: {:.3f} ms".format(det_time * 1000)
        render_time_message = "OpenCV rendering time: {:.3f} ms".format(render_time * 1000)
        async_mode_message = "Async mode is on. Processing request {}".format(cur_request_id) if is_async_mode else \
            "Async mode is off. Processing request {}".format(cur_request_id)

        cv2.putText(frame, inf_time_message, (15, 15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (200, 10, 10), 1)
        cv2.putText(frame, render_time_message, (15, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (10, 10, 200), 1)
        cv2.putText(frame, async_mode_message, (10, int(initial_h - 20)), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (10, 10, 200), 1)

    else:
        inf_end = time.time()
        # global det_time
        det_time = inf_end - inf_start
        # print("time123: " + str(det_time*1000))

def getframe():
    if args.labels:
        with open(args.labels, 'r') as f:
            global labels_map
            labels_map = [x.strip() for x in f]
    else:
        labels_map = None
    if args.input == 'cam':
        input_stream = '/media/gubo/DATADRIVE0/work/口罩视频/22.mp4'
        cap = cv2.VideoCapture(input_stream)
        # cap.set(3, 1920)
        # cap.set(4, 1080)
        cap.set(3, 1280)
        cap.set(4, 720)
        global cur_request_id, next_request_id, i, j
        cur_request_id = 0
        next_request_id = 1
        i = 0
        j = 0

        log.info("Starting inference in async mode...")
        global is_async_mode, isModeChanged
        is_async_mode = False
        isModeChanged = False
        global ret, frame, next_frame, render_time
        render_time = 0
        ret, frame = cap.read()
        # ret1, frame1 = cap.read()

        # print("To close the application, press 'CTRL+C' here or switch to the output window and press ESC key")
        # print("To switch between sync/async modes, press TAB key in the output window")
        while cap.isOpened():
            global initial_h, initial_w
            initial_w = 1080
            initial_h = 1920

            # initial_w = 720
            # initial_h = 1280
            if is_async_mode:

                ret, next_frame = cap.read()
                next_frame = cv2.resize(next_frame, (initial_w, initial_h))
            else:
                ret, frame = cap.read()
                frame = cv2.resize(frame, (initial_w, initial_h))
            # if is_async_mode:
            #
            #     ret, next_frame = cap.read()
            #     next_frame = cv2.resize(next_frame, (720, 1280))
            # else:
            #     ret, frame = cap.read()
            #     frame = cv2.resize(frame, (720, 1280))
            if not ret:
                print('break')
                break

            yaw()
            render_start = time.time()
            cv2.imshow("Detection Results", frame)
            # cv2.imshow("da", frame1)

            render_end = time.time()
            render_time = render_end - render_start
            if is_async_mode:
                # i += 1
                cur_request_id, next_request_id = next_request_id, cur_request_id
                frame = next_frame
            # # else:
            # cur_request_id, next_request_id = next_request_id, cur_request_id
            # frame = next_frame

            key = cv2.waitKey(1)
            if key == 27:
                break
            if key == 9:
                is_async_mode ^= False
                isModeChanged = True

                log.info("Switched to {} mode".format("async" if is_async_mode else "sync"))
                # getdetectresult()待测试

        cv2.destroyAllWindows()
    # elif args.input == 'video':
    #     input_stream = '/home/gubo/Downloads/戴口罩.mp4'
    #     cap = cv2.VideoCapture(input_stream)
    #     cap.set(3, 2304)
    #     cap.set(4, 1296)
    #     # cap.set(3, 1280)
    #     # cap.set(4, 720)
    #     global cur_request_id, next_request_id, i, j
    #     cur_request_id = 0
    #     next_request_id = 1
    #     i = 0
    #     j = 0
    #
    #     log.info("Starting inference in async mode...")
    #     global is_async_mode, isModeChanged
    #     is_async_mode = False
    #     isModeChanged = False
    #     global ret, frame, next_frame, render_time
    #     render_time = 0
    #     ret, frame = cap.read()
    #
    #     # print("To close the application, press 'CTRL+C' here or switch to the output window and press ESC key")
    #     # print("To switch between sync/async modes, press TAB key in the output window")
    #     while cap.isOpened():
    #         if is_async_mode:
    #
    #             ret, next_frame = cap.read()
    #         else:
    #             ret, frame = cap.read()
    #         if not ret:
    #             print('break')
    #             break
    #         global initial_h, initial_w
    #         initial_w = cap.get(3)
    #
    #         initial_h = cap.get(4)
    #         yaw()
    #         render_start = time.time()
    #         cv2.imshow("Detection Results", frame)
    #
    #         render_end = time.time()
    #         render_time = render_end - render_start
    #         if is_async_mode:
    #             # i += 1
    #             cur_request_id, next_request_id = next_request_id, cur_request_id
    #             frame = next_frame
    #         # # else:
    #         # cur_request_id, next_request_id = next_request_id, cur_request_id
    #         # frame = next_frame
    #
    #         key = cv2.waitKey(1)
    #         if key == 27:
    #             break
    #         if key == 9:
    #             is_async_mode ^= False
    #             isModeChanged = True
    #
    #             log.info("Switched to {} mode".format("async" if is_async_mode else "sync"))
    #             # getdetectresult()待测试
    #
    #     cv2.destroyAllWindows()

    else:
        input_stream = args.input
        cur_request_id = 0
        next_request_id = 1
        if os.path.isfile(input_stream) == True:

            assert os.path.isfile(args.input), "Specified input file doesn't exist"
            frame = cv2.imread(input_stream)
            # cv2.imshow('231',frame)
            initial_w = frame.shape[1]

            initial_h = frame.shape[2]
            is_async_mode = False
            render_time = 0
            yaw()
        if os.path.isdir(input_stream) == True:
            piclist = os.listdir(input_stream)
            for pic in piclist:
                # print(pic)
                frame = cv2.imread(input_stream + pic)
                frame = cv2.resize(frame, (1280, 720))
                initial_w = frame.shape[1]

                initial_h = frame.shape[2]
                is_async_mode = False
                render_time = 0
                yaw()
            # cv2.imshow("Detection Results", frame)
            # key = cv2.waitKey(0)


            # cv2.destroyAllWindows()


if __name__ == '__main__':


    args = build_argparser().parse_args()
    startMYIRAD()
    getframe()

