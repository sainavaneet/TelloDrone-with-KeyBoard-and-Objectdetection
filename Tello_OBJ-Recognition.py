from djitellopy import tello
import cvzone
import cv2
from time import sleep

import getter as kg
import Control as ct
thres = 0.50
nmsThres = 0.2




classNames = []
classFile = 'ss.names'
with open(classFile, 'rt') as f:
    classNames = f.read().split('\n')


print(classNames)
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = "frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

kg.init()

me = tello.Tello()
me.connect()
print(me.get_battery())
isFlying = 0
me.streamoff()
me.streamon()




while True:

    # success, img = cap.read()
    img = me.get_frame_read().frame
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nmsThres) # To remove duplicates / declare accuracy
    try:
        for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cvzone.cornerRect(img, box)
            cv2.putText(img, f'{classNames[classId - 1].upper()} {round(conf * 100, 2)}',
                        (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1, (0, 255, 0), 2)
    except:
        pass

    inputs = ct.getKeyboardInput(isFlying)
    isFlying = inputs[4]
    me.send_rc_control(inputs[0], inputs[1], inputs[2], inputs[3])
    sleep(0.01)

    cv2.imshow("Image", img)
    cv2.waitKey(1)






