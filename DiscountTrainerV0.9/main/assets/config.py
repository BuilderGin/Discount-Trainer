'''
Created on Jan 01, 2022
@summary: Get Config from settings.ini
@author: git:buildergin
Update on Feb 04, 2022
'''

from decouple import config
from pathlib import Path

# Define the base directory for easyer navigation
ROOT_DIR = BASE_DIR = Path(__file__).resolve().parent.parent



"""
    All Config variabels here defined for use later on
    :param: Get config form settings.ini
    :return: Define the config variables inside Settings.ini file
"""


MENU_TITLE = config('MENU_TITLE')

SQUAT_ANGLE1 = config('SQUAT_ANGLE1')
SQUAT_ANGLE2 = config('SQUAT_ANGLE2')

AMOUNT_SQUATS = config('AMOUNT_SQUATS')
DISCOUNT_AMOUNT = config('DISCOUNT_AMOUNT')
SQUAT_COMPLETED_TEXT = config('SQUAT_COMPLETED_TEXT')