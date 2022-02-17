'''
Created on Jan 19, 2021
@summary: Store Data and send data to printer(Hardware)
@author: git:buildergin
Update on Feb 04, 2022
'''

# #############################################
# imports for the GameMenu functionality
# #############################################


import os
from datetime import datetime
from tkinter.constants import TRUE
import pandas as pd
import numpy as np
from pathlib import Path

# #############################################
# Own Files Import
# #############################################

## Decouple settings, config.py | Developer Changes, developer.py | switching frames, switchFrame.py
from . import config




# Directory to /log
dir = config.ROOT_DIR / 'log/'


# Get the Game Data And Store it in an CSV file
def add_data_to_csv():
    """
        Get Data and Store Data
        :param: Get Data of last finished game and store to CVS file
        :return: CSV file contianing the following {id, date, time, amount, discount}
    """

    id = datetime.today().strftime('%d%m%y-%H%M%S') # Day, month, year, Hour, minut, Seconds
    date = datetime.today().strftime('%d %B %Y') # Wednesday, 03, December, 2021
    time = datetime.today().strftime('%A %H:%M') # Wednesday, 16:31
    AMOUNT_SQUATS = str(config.AMOUNT_SQUATS)
    DISCOUNT = str(config.DISCOUNT_AMOUNT)

    csv_row = []

    # Define Variables to use
    game_data = {
        'id': id,
        'date': date,
        'time': time,
        'game': 'Squat',
        'amount': AMOUNT_SQUATS,
        'discount': DISCOUNT,
    }

    # Link the Tables
    squat_data = {
        'id': game_data['id'],
        'date': game_data['date'],
        'time': game_data['time'],
        'game': game_data['game'],
        'amount': game_data['amount'],
        'discount': game_data['discount'],
    }

    csv_row.append(squat_data)
    print(f'Data ROW: {csv_row}')

    squat_data = pd.DataFrame(csv_row)
    squat_data.to_csv(dir / 'game_log.csv', mode='a', index=False, header=False)
    print('Data has Been stored to CSV file')



# Open CSV file and get Last Player Data
def print_last_row():
    """
        Get Last Row Data
        :param: Get the last row data of csv file
        :return: last row data
    """

    df = pd.read_csv(dir / "game_log.csv")
    last_row = df.iloc[-1].tolist()
    print(f'Last Row: {last_row}')

    return last_row



def main_print():
    """
        Get Data and send to Printer
        :param: Use the above function to get last row. create new file and store information again in a .txt file to Print
        :return: Send last row data to the printer
    """

    # To run above function
    create_save_data_to_csv = add_data_to_csv()
    data = print_last_row()

    # Identifie last row and assign it to an variable
    last_id = f'ID: {data[0]}'
    last_date = f'Date: {data[1]}'
    last_time = f'Finish Time: {data[2]}'
    last_game = f'Type Game: {data[3]}'
    last_amount = f'Amount {data[3]}: {data[4]}'
    last_discount = f'Discount: {data[5]}'


    print(
        f'ID: {last_id}, DATE: {last_date}, TIME: {last_time}, AGAME: {last_game}, AM: {last_amount}, DIS: {last_discount},  '
    )


    # Create .txt file and store last row data there
    file = dir / 'last_user.txt'
    with open(file, 'w') as filetowrite:
        filetowrite.write(
            last_id + '\n' + 
            last_date + '\n' + 
            last_time + '\n' + 
            last_game + '\n' + 
            last_amount + '\n' + 
            last_discount
        )

    # Send File to the printer
    print("Waiting for the printer to start")

    os.startfile(file, 'print') # send .txt file to an printer
