'''
Created on Nov 24, 2021
@summary: Squat functionalitys to display on screen
@author: git:buildergin
Update on Feb 04, 2022
'''




# #############################################
# imports for the GameMenu functionality
# #############################################

from numpy.lib.function_base import angle 
from . import PostModule as pm
import numpy as np
import time
import imutils
import cv2
from tkinter import *
from PIL import Image, ImageTk


# #############################################
# Own Files Import
# #############################################\

## Decouple settings, config.py | switching frames, switchFrame.py | print results, printResults.py
from assets import config, switchFrame, printResults

from windows import completed


# from .print_script import print_discount

detector = pm.poseDetector()



def preprocess(self, cap, root, camera_frame):

    mauve_pink, mauve_blue, mauve_light = (72,32,122), (174,104,24), (235,215,198)

    # Get Full resolution of divice       
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    fullscreen = int(screen_width*0.95), int(screen_height*0.95) # Width #height

    # Define squat angels form settings.ini
    SQUAT_ANGLE1 = config.SQUAT_ANGLE1
    SQUAT_ANGLE2 = config.SQUAT_ANGLE2

    # Define the counter amount
    left_count, right_count = float(config.AMOUNT_SQUATS), float(config.AMOUNT_SQUATS)
    
    # Direction left & right
    left_dir, right_dir = 0, 0
    pTime = 0

    

    #============================================================================#

    while(cap.isOpened()):
        success, image = cap.read()
        if success == False: break

        # Crop Frame and define the angle
        cropped_frame = crop_frame(image, fullscreen)

        human_pose = detector.findPose(cropped_frame, False) # False Full Body Lines
        lmList = detector.findPosition(human_pose, False)

        if len(lmList) != 0:

            # LEFT LEGG
            Left_Leg = 27, 25, 23
            left_angle = detector.findAngle(human_pose, Left_Leg[0], Left_Leg[1], Left_Leg[2])
            left_bar = np.interp(left_angle, ((int(SQUAT_ANGLE1),int(SQUAT_ANGLE2))), (160,400))
            left_per = np.interp(left_angle, (int(SQUAT_ANGLE1),int(SQUAT_ANGLE2)), (100,0))
            
            # RIGHT LEGG
            Right_Leg = 28, 26, 24
            right_angle = detector.findAngle(human_pose, Right_Leg[0], Right_Leg[1], Right_Leg[2])
            right_bar = np.interp(right_angle, ((int(SQUAT_ANGLE1),int(SQUAT_ANGLE2))), (160,400))
            right_per = np.interp(right_angle, (int(SQUAT_ANGLE1),int(SQUAT_ANGLE2)), (100,0))


            # Check for the Squats
            # Left Legg
            if left_per == 100:
                if left_dir == 0:
                    left_count = left_count - 0.5
                    left_dir = 1
            if left_per == 0:
                if left_dir == 1:
                    left_count -= 0.5
                    left_dir = 0

            # Right Legg
            if right_per == 100:
                if right_dir == 0:
                    right_count = right_count - 0.5
                    right_dir = 1
            if right_per == 0:
                if right_dir == 1:
                    right_count -= 0.5
                    right_dir = 0


            ## COUNTER
            if left_count < 0.6:
                left_count = 0
            if right_count < 0.6:
                right_count = 0


            ## DISPLAY AVERAGE BAR / PER ON DISPLAY
            avg_bar = (round(left_bar,2) + round(right_bar,2)) / 2
            avg_per = (round(left_per,2) + round(right_per,2)) / 2

            # DRAW Bar Box Right
            cv2.rectangle(human_pose, (125,int(avg_bar)),(85,400),mauve_light, cv2.FILLED)
            cv2.rectangle(human_pose, (85,160),(125,400),mauve_pink, 3)
            cv2.putText(human_pose, f'{int(avg_per)}%', (85, 425), cv2.FONT_HERSHEY_PLAIN, 1, mauve_pink, 2)

            
            # DISPLAY AVERAGE COUNTER
            count_list = [left_count, right_count]
            highest_count = max(count_list)
            cv2.putText(human_pose, f'Nog {str(int(highest_count))} squats', (75, 150), cv2.FONT_HERSHEY_PLAIN, 3, mauve_pink, 3)

            # FPS:
            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime
            cv2.putText(human_pose, f'FPS: {str(int(fps))}', (10,30), cv2.FONT_HERSHEY_PLAIN, 2, mauve_pink, 2)


            # Make sound if counter reach ...
            if highest_count == 0: 
                print("Challange Completed...")

                cap.release()
                cv2.destroyAllWindows()

                # Challange Completed Window
                results = printResults.main_print()
                completed = switchFrame.to_completed(self)

            
        #cv2.imshow('Squats Counter', img)
        img = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(image=Image.fromarray(img))
        camera_frame['image'] = img
        root.update()
        
    cap.release()
    cv2.destroyAllWindows()




# Crop Frame
def crop_frame(frame, fullscreen):
    """
    To Resize capture to portrait mode
    :param: portrait size webcam
    :return: Resize webcam to fullscreen and resize again to protrait and return it
    """

    # Resize to fullscreen Image
    resized_frame = cv2.resize(frame, (fullscreen[0], fullscreen[1]))
    #mirror_flip = cv2.flip(resized_frame, 1)

    # Crop Image to Portrait mode
    w1 = int(fullscreen[0]/4)
    w2 = int(fullscreen[0]/4*3)
    cropped_img = resized_frame[0:int(fullscreen[1]), w1:w2]

    return cropped_img
