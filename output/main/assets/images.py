import tkinter as tk
from tkinter import Frame, ttk, font, PhotoImage
from tkinter.constants import FLAT
from typing import Text

import os
import random
from PIL import Image, ImageTk
#import config
from . import config

rootdir = config.BASE_DIR
IMAGE_ROOT = rootdir / 'static/images/'



# h 1080 * 60%      648         1296
# w 1920 * 16%      307         614

def squat_image_root():
    SQUAT_ROOT = rootdir / 'static/images/squats/'
    random_image = get_random_image(SQUAT_ROOT)
    return f'{SQUAT_ROOT / random_image}' 


def bicep_image_root():
    BICEP_ROOT = rootdir / 'static/images/biceps/'
    random_image = get_random_image(BICEP_ROOT)
    return f'{BICEP_ROOT / random_image}' 


def get_random_image(directory):
    image_list = images_list(directory)  # return all items ends with .jpg
    random_image = image_list[random.randint(0, int(len(image_list)-1))]  # get random item
    
    return random_image



def images_list(directory):
    images = []        
    for image in os.listdir(directory):
        if image.endswith(".jpg"):
            images.append(image)

    return images




# def resize_image():
#     random_image = get_random_image(IMAGE_ROOT / 'squats/')
#     image_directory = IMAGE_ROOT / random_image

#     screen_width = 1920
#     screen_height = 1080 
#     # screen_width = self.root.winfo_screenwidth()
#     # screen_height = self.root.winfo_screenheight()

#     image = PhotoImage(file=image_directory)

#     resized_image = image.resize(screen_width, screen_height)

#     print(f'w:{resized_image.width} ,h:{resized_image.height}')

#     return resize_image
