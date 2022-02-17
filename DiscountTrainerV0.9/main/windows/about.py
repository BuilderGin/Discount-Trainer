'''
Created on Nov 21, 2021
@summary: AboutGame screen
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

import webbrowser


# #############################################
# Own Files Import
# #############################################

## Decouple settings, config.py | Developer Changes, developer.py | switching frames, switchFrame.py
from assets import config, developer, switchFrame



## HERE UNDER START THE FUNCTIONS

def aboutpage(self):
    """
    Created About Window
    :param: Created frames needed 
    :return: About Window
    """
    # Header Section
    self.about_title_label = ttk.Label(self.header_frame, text='About The Game', style='middle_txt.TLabel')
    self.about_title_label.pack(side="top")

    # Container Section
    self.about_title_label1 = ttk.Label(self.container_frame, text=(f'CREATED BY {developer.CREATOR}'), style='small_txt.TLabel')
    self.about_title_label1.pack(side="top", expand="YES")

    self.about_game_version = ttk.Label(self.container_frame, text=(f'CURRENT GAME VERSION {developer.GAME_VERSION}'), style='small_txt.TLabel')
    self.about_game_version.pack(side="top", expand="YES")

    self.about_update_date = ttk.Label(self.container_frame, text=(f'LAST DATE IT HAS BEEN EDITED {developer.UPDATE_DATE}'), style='small_txt.TLabel')
    self.about_update_date.pack(side="top", expand="YES")

    self.about_copyright = ttk.Label(self.container_frame, text=(developer.COPYRIGHT_TEXT), style='small_txt.TLabel')
    self.about_copyright.pack(side="top", expand="YES")


    # Footer Section
    self.new_versions = ttk.Label(self.footer_frame, text='I will update the game from time to time, do you want a newer version? Just check my Github page.', style='small_txt.TLabel')
    self.new_versions.pack(side="top", expand="YES")
    
    self.new_versions1 = ttk.Label(self.footer_frame, text='Check if the game version is higher than previus before download & installing.', style='small_txt.TLabel')
    self.new_versions1.pack(side="top", expand="YES")

    self.about_back_btn = tk.PhotoImage(file='static/icon/back_btn.png')
    self.about_back_to_menu = ttk.Button(self.footer_frame, image=self.about_back_btn, cursor='hand2', command=lambda: switchFrame.to_home(self))
    self.about_back_to_menu.pack(side="left")

    self.about_gitlink_btn = tk.PhotoImage(file='static/icon/github_link.png')
    self.about_gitlink = ttk.Button(self.footer_frame, image=self.about_gitlink_btn, cursor='hand2', command=lambda: webbrowser.open_new(developer.GITHUB_LINK))
    self.about_gitlink.pack(side="right")

