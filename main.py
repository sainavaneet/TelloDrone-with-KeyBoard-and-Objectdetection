import getter as kg
import Control as ct
from djitellopy import tello
from time import sleep
import cv2 as cv
import numpy as np

kg.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())
isFlying = 0


while True:
    inputs = ct.getKeyboardInput(isFlying)
    isFlying = inputs[4]
    drone.send_rc_control(inputs[0], inputs[1], inputs[2], inputs[3])
    sleep(0.01)
