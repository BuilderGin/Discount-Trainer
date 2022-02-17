'''
Created on Feb 03, 2021
@summary: Challange Completed Screen
@author: git:buildergin
Update on Feb 04, 2022
'''


# #############################################
# imports for the GameMenu functionality
# #############################################

from ast import Lambda
from calendar import c
from distutils import command
import tkinter as tk
from tkinter import Frame, ttk, font, PhotoImage
from tkinter.constants import FLAT
from typing import Text

import time

# #############################################
# Own Files Import
# #############################################

## Decouple settings, config.py | Developer Changes, developer.py | switching frames, switchFrame.py
from assets import config, developer, switchFrame




## HERE UNDER START THE FUNCTIONS

def challange_completed(self):

    """
    Created completed Window
    :param: Window Will be shown, when a game is completed
    :return: Completed Window
    """

    #Set to fullscreen
    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    self.root.geometry(("%dx%d+0+0" % (screen_width,screen_height)))

    # HEADER
    self.header_frame = ttk.Frame(self.root, style='Frame.TFrame')
    self.header_frame.pack(padx=15, pady=35, anchor="n", fill="x", expand="YES")


    # CONTAINER
    self.container_frame = ttk.Frame(self.root, style='Frame.TFrame')
    self.container_frame.pack(padx=15, pady=10, anchor="n", fill="x", expand="YES")

    self.congrats = ttk.Label(self.container_frame, text=(config.SQUAT_COMPLETED_TEXT), style='big_txt.TLabel')
    self.congrats.pack(side="top", expand="YES")

    self.bon = ttk.Label(self.container_frame, text=(developer.PRINT_TIME), style='middle_txt.TLabel')
    self.bon.pack(side="top", expand="YES")


    # FOOTER
    self.footer_frame = ttk.Frame(self.root, style='Frame.TFrame')
    self.footer_frame.pack(padx=15, pady=15, anchor="s", fill="x", expand="YES")



    self.go_menu_btn = ttk.Button(self.footer_frame, text='Go to menu', cursor='hand2', style='Train.TButton', command=lambda:switchFrame.to_home(self))
    self.go_menu_btn.pack(padx=5, ipady=5, fill="both", expand=1)
