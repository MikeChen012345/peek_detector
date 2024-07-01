"""
Acknowledgement:
This program is based on the tutorial at 
https://www.geeksforgeeks.org/python-smile-detection-using-opencv/?ref=lbp
"""

import cv2
import numpy as np
import argparse
from turnoff import screen_off, screen_on

# ----------------- Configuration -----------------
# The time to wait before turning off the screen. If the value is too low, 
# the screen will turn off too much and can trigger more false alarm. 
# If the value is too high, the screen will not turn off when someone leaves the screen or
# others are peeking at the screen.
timeout = 20 

# Whether the user can press the q key to quit the program. 
# Side effect: a small window will appear when the program is running.
q_quit = False 
# ----------------- Configuration -----------------

off = False # Variable to keep track of the screen state
no_face_time = 0 # The time since the last face was detected
multi_face_time = 0 # The time since the last multiple faces were detected

vc = cv2.VideoCapture(0) # Open the camera. # 0 represents the default camera (usually the built-in webcam)


if __name__ == "__main__" :
    # Read the command line arguments
    parser = argparse.ArgumentParser(description='Detect peeking')
    parser.add_argument('-q', '--q_quit', action='store_true', help='Allow the user to press q to quit the program. Side effect: a small window will appear when the program is running.')
    parser.add_argument('-t', '--timeout', type=int, help='The time to wait before turning off the screen')
    args = parser.parse_args()
    timeout = args.timeout if args.timeout else timeout
    q_quit = args.q_quit if args.q_quit else q_quit

    if q_quit:
        # Create a blank image to display in the window
        blank_image = np.zeros((1, 1, 1), np.uint8)

    video_capture = cv2.VideoCapture(0) 
    while video_capture.isOpened(): 
        if q_quit:
            # Display the blank image
            cv2.imshow('', blank_image)

        # Captures video_capture frame by frame 
        _, frame = video_capture.read()  
    
        # To capture image in monochrome                     
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) == 0: # Turn off the screen if no face is detected
            print("No face detected")
            no_face_time += 1
            if not off and no_face_time > timeout: # Turn off the screen if no face is detected for <timeout> frames
                no_face_time = 0
                screen_off()
                off = True

        if len(faces) > 1: # Turn off the screen if multiple faces are detected
            print("Multiple faces detected")
            multi_face_time += 1
            if not off and multi_face_time > timeout:
                multi_face_time = 0
                screen_off()
                off = True
        
        if len(faces) == 1: # Turn on the screen if only one face is detected
            print("One face detected")
            no_face_time = 0
            multi_face_time = 0
            if off:
                screen_on()
                off = False
                print("Screen on")

        if q_quit:
            # for unknown reason, pyautogui.press('q') does not work
            # The control breaks once q key is pressed    
            # 20 is to wait for 20ms. 0xff is used to mask off the upper bits of the key code.                   
            if cv2.waitKey(20) & 0xff == ord('q'):                
                break
    
    # Release the capture once all the processing is done. 
    video_capture.release()                                  
    cv2.destroyAllWindows() 
