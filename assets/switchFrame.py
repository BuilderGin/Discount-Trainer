'''
Created on Feb 02, 2022
@summary: Swapping btween screens
@author: git:buildergin
Update on Feb 04, 2022
'''

# #############################################
# Switching to other frame
# #############################################

from . import clearFrame
from windows import about, menu, completed
from games.squats import squat_frame


def to_about(self):
    clear = clearFrame.clear(self)
    clear_btn = clearFrame.destroy_home_btn(self)
    aboutFrame = about.aboutpage(self)


def to_home(self):
    clear = clearFrame.clear(self)
    homeFrame = menu.Main_Window.homepage(self)


def to_squat(self):
    clearall = clearFrame.clearAll(self)
    squatFrame = squat_frame.squats(self)

def to_completed(self):
    clear_cap = clearFrame.clear_capture(self)
    completedFrame = completed.challange_completed(self)