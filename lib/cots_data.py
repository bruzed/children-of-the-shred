#Simple data loader module.

#Loads data files from the "data" directory shipped with a game.

#Enhancing this to handle caching etc. is left as an exercise for the reader.

import os, sys

import pygame
from pygame.locals import *


data_py = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.normpath(os.path.join(data_py, '..', 'data'))

def load_bg(name):
	print name
	bgname = os.path.join(data_dir, os.path.join( "backgrounds", * name))
	print bgname
	bgimage = pygame.image.load(bgname)
	bgimage = bgimage.convert_alpha()
	return bgimage, bgimage.get_rect()

def load_image(name):
    fullname = os.path.join(data_dir, name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image, image.get_rect()


def filepath(filename):
    #Determine the path to a file in the data directory.

    return os.path.join(data_dir, filename)

def load(filename, mode='rb'):
    #Open a file in the data directory.

    #"mode" is passed as the second arg to open().
    
    return open(os.path.join(data_dir, filename), mode)