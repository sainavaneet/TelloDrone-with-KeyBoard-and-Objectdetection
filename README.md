# TelloDrone-with-KeyBoard-and-Objectdetection

This repo allows you to control a Tello drone using your keyboard and perform object detection using a pre-trained model. The drone movements are controlled using the arrow keys and specific keys for takeoff, landing, and flips. The object detection is performed on the live video feed from the drone's camera.

## Prerequisites

- Python 3.x
- `getter` module
- `djitellopy` library
- `pygame` library
- `cv2` (OpenCV) library
- `cvzone` library

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/sainavaneet/TelloDrone-with-KeyBoard-and-Objectdetection.git
   ```

2. Install the required dependencies:

   ```bash
   pip install getter djitellopy pygame opencv-python cvzone
   ```

## Usage

1. Import the necessary modules and initialize the required components:

   ```python
   import getter as kg
   from djitellopy import tello
   from time import sleep

   kg.init()

   drone = tello.Tello()
   drone.connect()
   ```

2. Define the function to get keyboard input for drone control:

   ```python
   def getKeyboardInput(isFlying):
       # ... implementation ...
       return [lr, fb, ud, yw, isFlying]
   ```

3. Implement the drone control loop:

   ```python
   while True:
       inputs = getKeyboardInput(isFlying)
       isFlying = inputs[4]
       drone.send_rc_control(inputs[0], inputs[1], inputs[2], inputs[3])
       sleep(0.01)
   ```

4. Implement object detection using the Tello drone's camera:

   ```python
   # ... import necessary modules ...

   thres = 0.50
   nmsThres = 0.2

   # ... load class names and pre-trained model ...

   while True:
       # ... get frame from drone's camera ...

       # ... perform object detection ...

       # ... display the detected objects ...

       # ... get keyboard input and control the drone ...

       # ... display the frame ...

   ```


## Videos 

### OBJECT DETECTIOIN
[![OBJECT DETECTION](https://img.youtube.com/vi/FL7ku3DEp7o/0.jpg)](https://youtu.be/FL7ku3DEp7o)

### KEYBOARD CONTROL
[![KEYBOARD CONTROL](https://img.youtube.com/vi/IpdcT8TlTOE/0.jpg)](https://youtu.be/IpdcT8TlTOE)


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.


********
- The Tello SDK provided by DJI Ryze Robotics: [https://github.com/damiafuentes/DJITelloPy](https://github.com/damiafuentes/DJITelloPy)
- Pre-trained object detection model: [https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)
---
