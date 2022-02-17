'''
Created on Nov 24, 2021
@summary: Splash Screen
@author: git:buildergin
Update on Nov 26, 2022
'''

# #############################################
# imports for the splash code functionality
# #############################################
import os
import pathlib
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from tkinter import font
import PIL
from PIL import Image, ImageTk
import time
from time import sleep


""" Developer Changes | assets.developer.py """ 
from assets.developer import GAME_VERSION, CREATOR, UPDATE_DATE, COPYRIGHT_TEXT


## HERE UNDER START THE FUNCTIONS
class splashScreen():     
    def __init__(self):
        '''
        splashScreen constructor
        '''

        self.splash()        
        
        
     
    def splash(self):
        '''
        The splash interface code
        '''
        self.root = tk.Tk()
        #self.root.geometry('540x540+75+75')
      
        self.root.attributes('-alpha', 0.8) 
        self.root.attributes('-topmost', True)
        self.root.update_idletasks()
       
        #root.title('Splash')
        #root.wm_attributes('-fullscreen','true')
        #eliminate the titlebar
        self.root.overrideredirect(1)


        # Main Section
        # self.main_frame = ttk.Frame(self.root)
        # self.main_frame.pack(fill="both", expand="YES")

        self.bg_image = Image.open("static/images/splash/pexels-victor-freitas-841130.jpg")
        self.image = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.root, image=self.image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.image = self.image

        # self.image_label = ttk.Label(self.main_frame, image=self.bg_image)
        # self.image_label.pack()

        self.splash_footer_frame = ttk.Frame(self.root)
        self.splash_footer_frame.pack(padx=15, pady=15, anchor="s", fill="x", expand="YES")

        self.home_Copyright = ttk.Label(self.splash_footer_frame, text=COPYRIGHT_TEXT, font='Salsa 9')
        self.home_Copyright.pack(side="bottom")

        # self.quit_btn = ttk.Button(self.root, text='Squat Trainer', cursor='hand2', command=lambda:self.root.quit())
        # self.quit_btn.pack(padx=5, ipady=5, fill="both", side="left", expand=1)
        #self.root.after(5000, lambda: self.root.destroy()) # Destroy the widget after 30 seconds
        #self.root.mainloop()

        #time.sleep(6)
        #self.root.quit()

        
        
if __name__ == '__main__':
    spl = splashScreen()