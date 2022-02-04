'''
Created on Feb 02, 2021
@summary: Squat Frame
@author: git:buildergin
Update on Feb 02, 2022
'''


# #############################################
# imports for the GameMenu functionality
# #############################################

import tkinter as tk
from tkinter import Frame, ttk, font, PhotoImage
from tkinter.constants import FLAT
from typing import Text

import cv2
from games.squats import squat


# #############################################
# Own Files Import
# #############################################

## Decouple settings, config.py | Developer Changes, developer.py | switching frames, switchFrame.py
from assets import config, developer, switchFrame


## HERE UNDER START THE FUNCTIONS

def squats(self):

    # Set to fullscreen
    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    self.root.geometry(("%dx%d+0+0" % (screen_width,screen_height)))


    self.cap_frame = ttk.Frame(self.root, style='Frame.TFrame')
    self.cap_frame.pack(padx=10, pady=10, anchor="n", fill="x", expand="YES")

    self.camera_frame = ttk.Label(self.cap_frame)
    self.camera_frame.pack(side='top', padx=0, pady=0, expand="YES")


    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    START_SQUAT_GAME = squat.preprocess(self, cap, self.root, self.camera_frame)