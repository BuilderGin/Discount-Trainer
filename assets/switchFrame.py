'''
Created on Feb 02, 2022
@summary: Swapping btween screens
@author: git:buildergin
Update on Feb 04, 2022
'''

# #############################################
# Switching to other frame
# #############################################

from . import clearFrame, sound
from windows import about, menu, completed
from games.squats import squat_frame


def to_about(self):
    """
    Clear frames, go to about window
    :param: clear frame, go about
    :return: clean about window
    """
    clear = clearFrame.clear(self)
    clear_btn = clearFrame.destroy_home_btn(self)
    aboutFrame = about.aboutpage(self)
    pause_music = sound.pause_music()


def to_home(self):
    """
    Clear frames, go to home window
    :param: clear frame, go home
    :return: clean home window
    """
    clear = clearFrame.clear(self)
    homeFrame = menu.Main_Window.homepage(self)
    start_music = sound.music_root()


def to_squat(self):
    """
    clear all frames, go squat game
    :param: clear all frames go Squat Game
    :return: Clean frames, Go Squat window + game
    """
    clearall = clearFrame.clearAll(self)
    squatFrame = squat_frame.squats(self)


def to_completed(self):
    """
    Clear frames, go to completed window
    :param: clear frame, go completed window
    :return: clean completed window
    """
    clear_cap = clearFrame.clear_capture(self)
    completedFrame = completed.challange_completed(self)
    stop_music = sound.stop_music()
    completed_sound = sound.completed_sound()
