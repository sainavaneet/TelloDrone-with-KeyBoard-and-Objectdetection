import getter as kg
from djitellopy import tello
from time import sleep

kg.init()

drone = tello.Tello()
drone.connect()


def getKeyboardInput(isFlying):
    lr, fb, ud, yw = 0, 0, 0, 0
    speed = 25

    if kg.getKey("SPACE"):
        if isFlying == 0:
            isFlying = 1
            drone.takeoff()
        else:
            isFlying = 0
            drone.land(); sleep(3)

    
    if kg.getKey("t"): drone.takeoff(); isFlying = 1
    if kg.getKey("l"): drone.land(); sleep(3); isFlying = 0
    if kg.getKey("r"): drone.flip("r"); isFlying = 1
    if kg.getKey("f"): drone.flip("l"); isFlying = 1


    
    if kg.getKey("a"):
        lr = -speed
    elif kg.getKey("d"):
        lr = speed

    
    if kg.getKey("s"):
        fb = -speed
    elif kg.getKey("w"):
        fb = speed

    
    if kg.getKey("DOWN"):
        ud = -speed
    elif kg.getKey("UP"):
        ud = speed

    
    if kg.getKey("LEFT"):
        yw = -speed
    elif kg.getKey("RIGHT"):
        yw = speed

    return [lr, fb, ud, yw, isFlying]