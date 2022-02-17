import pygame
from . import config
import time
import os
import random
from mutagen.mp3 import MP3

rootdir = config.BASE_DIR
SOUND_ROOT = rootdir / "static/sound/"
BG_ROOT = SOUND_ROOT / 'background/'
ENDING_ROOT = SOUND_ROOT / 'ending/'

pygame.mixer.init()


# Background root music
def music_root():
    """
    Root Of playing a music on the background
    :param: get item from folder and play
    :return: Playing music on background
    """
    random_music = get_random_music(BG_ROOT)    # Get Random Music from the Folder 'background/'
    music_dir = BG_ROOT / random_music          # Define the directory of music
    play_random_music = load_play(music_dir)    # Load & Play the music

    song = MP3(music_dir)                       
    songLength = song.info.length               # Read length of song
    print(f'Playing: {random_music[:-4]}, Time_sec: {int(songLength)}')

    return music_dir, random_music


def completed_sound():
    """
    Root Of playing completion sound
    :param: get item from folder and play
    :return: Playing music when completed challange
    """
    random_sound = get_random_music(ENDING_ROOT)    # Get Random Music from the Folder 'ending/'
    sound_dir = ENDING_ROOT / random_sound          # Define the directory of music
    play_random_sound = load_play(sound_dir)        # Load & Play the music

    song = MP3(sound_dir)
    songLength = song.info.length                   # Read length of song
    print(f'Playing: {random_sound[:-4]}, Time_sec: {int(songLength)}')

    return sound_dir, random_sound


# Random Int for the gathr list of music
def get_random_music(directory):
    """
    Get Random music from directory
    :param: get random item from folder
    :return: random item
    """
    music_list = list_music(directory)  # return all items ends with .mp3
    random_music = music_list[random.randint(0, int(len(music_list)-1))]  # get random item
    # random_music = random.choice(music_list)  ## This code get also random item in a string format, That use more memmory
    
    return random_music


# Load and play music
def load_play(directory):
    """
    Load the music and play it
    :param: Load & Play music
    :return: Load & Play Music
    """
    pygame.mixer.music.load(directory)  # Load Music
    play = pygame.mixer.music.play()    # Play Music
    volume = pygame.mixer.music.set_volume(0.3)
    pygame.mixer.fadeout(1000)


# Get List of music
def list_music(directory):   
    """
    Get all items in directory
    :param: look into a folder and give all items in a list format
    :return: list of all items
    """
    files = []        
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            files.append(file)
    
    return files


# Stopping the music
def stop_music():
    pygame.mixer.music.stop()

# Pausing the music
def pause_music():
    pygame.mixer.music.pause()

# Unpausing the Music
def unpause_music():
    pygame.mixer.music.unpause()
