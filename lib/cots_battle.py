#! /usr/bin/env python

import random, os.path
from cots_data import filepath
#open sound control
import osc

#basic pygame modules
import pygame
from pygame.locals import *

#see if we can load more than standard BMP
if not pygame.image.get_extended():
	raise SystemExit, "Sorry, extended image module required"

#game constants
SCREENRECT	 = Rect(0, 0, 800, 600)
SCORE		  = 0
SCORE2		  = 0
TIMELEFT          = 180
lordObjectNumber = 0  #this variable changes the x position of the zombie lord
slayerObjectNumber = 0  #this variable changes the x position of the zombie slayer
xposSpace = 1 #distance between notes played
xposIncrementor = 100 #this is the amount of x space for the zombies and slayers
last = 0 #previous time holder
playerTurn = 0 #my turn variable
yourCharacter = ""
slayerHits = 0
lordHits = 0
font_filename = 'anything.ttf'
doGameOver = 0 #change when the game is over

def load_image(file):
	"loads an image, prepares it for play"
	file = os.path.join('data', file)
	try:
		surface = pygame.image.load(file)
	except pygame.error:
		raise SystemExit, 'Could not load image "%s" %s'%(file, pygame.get_error())
	return surface.convert_alpha()

def load_images(*files):
	imgs = []
	for file in files:
		imgs.append(load_image(file))
	return imgs

class dummysound:
	def play(self): pass

def load_sound(file):
	if not pygame.mixer: return dummysound()
	file = os.path.join('data', file)
	try:
		sound = pygame.mixer.Sound(file)
		return sound
	except pygame.error:
		print 'Warning, unable to load,', file
	return dummysound()

# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change it's current position and state.

# zombie sprites


class ZombieA(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
        points = 600
        location = 600
	global lordObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50

class ZombieAs(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
        points = 600
        location = 600
	global lordObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50
                
class ZombieB(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
	location = 600
        global lordObjectNumber	

	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50

class ZombieC(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
	location = 600
	global lordObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50
                
class ZombieCs(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
	location = 600
	global lordObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50

class ZombieD(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
	location = 600
	global lordObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50
 
class ZombieDs(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
	location = 600
	global lordObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50
                
class ZombieE(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
	location = 600
	global lordObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50
                
class ZombieF(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
        location = 600
	global lordObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50

class ZombieFs(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
        location = 600
	global lordObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50
                
class ZombieG(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
        location = 600
	global lordObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50
                
class ZombieGs(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
        location = 600
	points = 600
	global lordObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(lordObjectNumber, 0)
		self.frame = 0

	def update(self):
                global SCORE2
		self.rect.move_ip(0, 1)
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE2 = SCORE2 - 50


#slayer sprites
		
class SlayerA(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
        location = 600
	points = 600
	global slayerObjectNumber
	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50
                        
class SlayerAs(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
        location = 600
	points = 600
	global slayerObjectNumber
	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50

class SlayerB(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
        location = 600
	points = 600
	global slayerObjectNumber
	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50

class SlayerC(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
	location = 600
	global slayerObjectNumber	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50

class SlayerCs(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
        location = 600
	global slayerObjectNumber
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50

class SlayerD(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
	location = 600
	global slayerObjectNumber
	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50

class SlayerDs(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
	location = 600
	global slayerObjectNumber
	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50

class SlayerE(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
        location = 600
	global slayerObjectNumber
	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50

class SlayerF(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
        location = 600
	global slayerObjectNumber
	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50

class SlayerFs(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
        location = 600
	global slayerObjectNumber
	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50

class SlayerG(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
        location = 600
	global slayerObjectNumber
	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50

class SlayerGs(pygame.sprite.Sprite):
	speed = 13
	animcycle = 12
	images = []
	points = 600
        location = 600
	global slayerObjectNumber
	
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(slayerObjectNumber, 550)
		self.frame = 0

	def update(self):
                global SCORE
		self.rect.move_ip(0, -1)		
		self.frame = self.frame + 1
		self.image = self.images[self.frame/self.animcycle%4]
                self.location = self.location - 1
                if self.location == 600:
                        self.points = self.location
                elif self.location == 550:
                        self.points = self.location
                elif self.location == 500:
                        self.points = self.location
                elif self.location == 450:
                        self.points = self.location
                elif self.location == 350:
                        self.points = self.location
                elif self.location == 300:
                        self.points = self.location
                elif self.location == 250:
                        self.points = self.location
                elif self.location == 200:
                        self.points = self.location
                elif self.location == 150:
                        self.points = self.location
                elif self.location == 100:
                        self.points = self.location
                elif self.location == 50:
                        self.points = self.location
                if self.location == 0:
                        SCORE = SCORE - 50

class Explosion(pygame.sprite.Sprite):
	defaultlife = 12
	animcycle = 3
	images = []
	def __init__(self, actor):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect(center=actor.rect.center)
		self.life = self.defaultlife

	def update(self):
		self.life = self.life - 1
		self.image = self.images[self.life/self.animcycle%2]
		if self.life <= 0: self.kill()

class slayerMessage(pygame.sprite.Sprite):
        global yourCharacter
        
        encouragingPhrases = ["You Rock!", "Way to Slay!",  "Look Out Buffy!"]
        tauntingPhrases = ["mmm... Brains!", "Rock Harder!"]
        messageLife = 45
        
        if yourCharacter == "lord":
                phrases = tauntingPhrases
                color = Color('red')
        else:
                phrases = encouragingPhrases
                color = Color('white')
                position = 0
                
	def __init__(self):           
		pygame.sprite.Sprite.__init__(self, self.containers)
                self.font = pygame.font.Font( filepath(font_filename), 60)
		self.image =  self.font.render(self.phrases[random.randint(0, len(self.phrases) - 1)], 0, self.color)
         	self.rect = self.image.get_rect(center=SCREENRECT.center)

	def update(self):
                if self.messageLife == 0:
                        self.kill()
                self.messageLife = self.messageLife - 1
                self.rect.move_ip(random.randint(-2,2), random.randint(-2,2))

class lordMessage(pygame.sprite.Sprite):
        global yourCharacter
        tauntingPhrases = ["Eat more brains!", "Rock Harder!"]
        encouragingPhrases = ["You Rock!", "mmm... Brains!",  "Braaaains!", "Delicious!"]
        messageLife = 45
        
        if yourCharacter == "lord":
                phrases = encouragingPhrases
                color = Color('white')
        else:
                phrases = tauntingPhrases
                color = Color('red')
        position = 0
        
	def __init__(self):           
		pygame.sprite.Sprite.__init__(self, self.containers)
                self.font = pygame.font.Font( filepath(font_filename), 60)
		self.image =  self.font.render(self.phrases[random.randint(0, len(self.phrases) - 1)], 0, self.color)
		self.rect = self.image.get_rect(center=SCREENRECT.center)
		
	def update(self):
                if self.messageLife == 0:
                        self.kill()
                self.messageLife = self.messageLife - 1
                self.rect.move_ip(random.randint(-2,2), random.randint(-2,2))

class timeLeft(pygame.sprite.Sprite):
        def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.Font( filepath(font_filename), 50)
		self.font.set_bold(0)
		self.color = Color('white')
		self.update()
		self.rect = self.image.get_rect(midtop=SCREENRECT.midtop)
		self.rect.move_ip(0,10)
        def update(self):
                msg = "%d" % TIMELEFT
                self.image = self.font.render(msg, 0, self.color)

class switchTurn(pygame.sprite.Sprite):
        def __init__(self):
                global playerTurn
                if playerTurn == 1:
                        msg = "Zombie Lord, Go!"
                else:
                        msg = "Zombie Slayer, Go!"
                pygame.sprite.Sprite.__init__(self, self.containers)
                self.font = pygame.font.Font( filepath(font_filename), 80)
                self.color = Color('white')
                self.image = self.font.render(msg, 0, self.color)
                self.rect = self.image.get_rect(center=SCREENRECT.center)
        def update(self):
        	
        	self.rect.move_ip(0,5)
                
class Score(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.Font(None, 20)
		self.font.set_italic(0)
		self.color = Color('white')
		self.lastscore = -1
		self.update()
		self.rect = self.image.get_rect().move(10, 10)

	def update(self):
		if SCORE != self.lastscore:
			self.lastscore = SCORE
			msg = "Zombie Lord Score: %d" % SCORE
			self.image = self.font.render(msg, 0, self.color)

class Score2(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.Font(None, 20)
		self.font.set_italic(0)
		self.color = Color('white')
		self.lastscore = -1
		self.update()
		self.rect = self.image.get_rect().move(550, 10)

	def update(self):
		if SCORE2 != self.lastscore:
			self.lastscore = SCORE2
			msg = "Zombie Slayer Score: %d" % SCORE2
			self.image = self.font.render(msg, 0, self.color)

def gameOver():
	winstyle = 0  # |FULLSCREEN
	bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
	screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
	#create the background, tile the bgd image
	gameOverScreen = load_image('gameover.gif')
	background = pygame.Surface(SCREENRECT.size)
	for x in range(0, SCREENRECT.width, gameOverScreen.get_width()):
		background.blit(gameOverScreen, (x, 0))
	screen.blit(background, (0,0))
	pygame.display.flip()
	pygame.time.wait(2000)
	osc.dontListen()
	return
                
#translate incoming frequencies from instrument

def getNote(freq):
	if (84.0 > freq > 80.0) | (166.0 > freq > 163.0) | (331.0 > freq > 325.0) | (661.0 > freq > 658) | (1320.0 > freq > 1317.0):
		return "E"
	
	elif (89.0 > freq > 86.5) | (176.0 > freq > 173.0) | (351.0 > freq > 348.0) | (700.0 > freq > 697.0) | (1398.0 > freq > 1395.0):
		return "F"
	
	elif (94.0 > freq > 91.5) | (186.5 > freq > 183.5) | (371.0 > freq > 369.0) | (741.0 > freq > 738.0) | (1481.0 > freq > 1478.0):
		return "F#"
	
	elif (99.5 > freq > 97.5) | (197.5 > freq > 194.5) | (393.5 > freq > 390.5) | (785.5 > freq > 782.5):
		return "G"

	elif (105.5 > freq > 103.0) | (209.0 > freq > 206.0) | (417.0 > freq > 414.0) | (832.0 > freq > 829.0):
		return "G#"

	elif (111.0 > freq > 109.5) | (221.0 > freq > 219.0) | (441.0 > freq > 439.0) | (881.0 > freq > 879.0):
		return "A"

	elif (118.0 > freq > 115.5) | (234.0 > freq > 232.0) | (467.0 > freq > 465.0) | (933.5 > freq > 931.0):
		return "A#"

	elif (84.0 > freq > 61.0) | (125.5 > freq > 122.5) | (247.5 > freq > 245.5) | (495.0 > freq > 492.0) | (988.5 > freq > 986.5):
		return "B"

	elif (132.5 > freq > 129.5) | (263.0 > freq > 260.0) | (524.0 > freq > 522.0) | (1047.5 > freq > 1045.0):
		return "C"

	elif (140.0 > freq > 137.5) | (279.0 > freq > 276.0) | (525.0 > freq > 522.0) | (1110.0 > freq > 1108.0):
		return "C#"

	elif (148.0 > freq > 145.5) | (295.0 > freq > 293.0) | (589.0 > freq > 586.0) | (1175.5 > freq > 1173.0):
		return "D"

	elif (157.0 > freq > 154.5) | (312.5 > freq > 310.0) | (623.5 > freq > 621.0) | (1245.5 > freq > 1243.5):
		return "D#"

	else:
		return "junk"

#runs when a note is played by you
def maxYourNote(*msg):
	global last
	global xposSpace
	global playerTurn
        global slayerHits
        global lordHits

	"""print 'last=', last
	now = pygame.time.get_ticks()
	print 'now=', now
	if (now > last):
		timeDifference = now - last
		timeDiffSecs = timeDifference/1000
		print 'timeDifference=', timeDifference
		print 'timeDiffSecs=', timeDiffSecs
		if timeDiffSecs !=0:
			xposSpace = timeDiffSecs
		else:
			xposSpace = 1
		last = now"""
	note = getNote(msg[0][2])
	print 'playerTurn', playerTurn
	
        
	if note != "junk" and playerTurn != 1:
		printYourNote(note)
		global lordObjectNumber
                global slayerObjectNumber
		global xposIncrementor

		#print 'lordObjectNumber', lordObjectNumber
		if note == "A":
                        if yourCharacter == "lord":
                                ZombieA()
			else:
                                SlayerA()
		elif note == "A#":
                        if yourCharacter == "lord":
                                ZombieAs()
                        else:
                                SlayerAs()
		elif note == "B":
                        if yourCharacter == "lord":
                                ZombieB()
                        else:
                                SlayerB()
		elif note == "C":
                        if yourCharacter == "lord":
        			ZombieC()
        		else:
                                SlayerC()
		elif note == "C#":
                        if yourCharacter == "lord":
        			ZombieCs()
        		else:
                                SlayerCs()
		elif note == "D":
                        if yourCharacter == "lord":
                                ZombieD()
			else:
                                SlayerD()
		elif note == "D#":
                        if yourCharacter == "lord":
                                ZombieDs()
			else:
                                SlayerDs()
		elif note == "E":
                        if yourCharacter == "lord":
                                ZombieE()
			else:
                                SlayerE()
		elif note == "F":
                        if yourCharacter == "lord":
        			ZombieF()
        		else:
                                SlayerF()
		elif note == "F#":
                        if yourCharacter == "lord":
        			ZombieFs()
        		else:
                                SlayerFs()
		elif note == "G":
                        if yourCharacter == "lord":
                                ZombieG()
                        else:
                                SlayerG()
		elif note == "G#":
                        if yourCharacter == "lord":
                                ZombieGs()
			else:
                                SlayerGs()
		else:
			print "must be something else"
        	if yourCharacter == "lord":
                        if lordHits%10 == 1:
                                lordMessage()
                        if lordObjectNumber <= 600:
                                lordObjectNumber += (xposIncrementor * xposSpace)
                                print 'objectNumber', lordObjectNumber
                        else: 
                        	lordObjectNumber = 0
                                playerTurn = 1
                                switchTurn()
                                
                else:

                        if slayerHits%10 == 1:
                                slayerMessage()
                        if slayerObjectNumber <= 600:
                                slayerObjectNumber += (xposIncrementor * xposSpace)
                                print 'objectNumber', slayerObjectNumber
                        else: 
                                slayerObjectNumber = 0
                                playerTurn = 1
                                switchTurn()
                                
	else:
		print "electricity!"
#runs when a note is played by your opponent
def maxOppNote(*msg):
	global playerTurn
	global xposIncrementor
	note = getNote(msg[0][2])
	if note != "junk" and playerTurn != 0:
		printOppNote(note)
		global slayerObjectNumber
		global lordObjectNumber
		if note == "A":
                        if yourCharacter != "lord":
                                ZombieA()
			else:
                                SlayerA()
		elif note == "A#":
                        if yourCharacter != "lord":
                                ZombieAs()
                        else:
                                SlayerAs()
		elif note == "B":
                        if yourCharacter != "lord":
                                ZombieB()
                        else:
                                SlayerB()
		elif note == "C":
                        if yourCharacter != "lord":
        			ZombieC()
        		else:
                                SlayerC()
		elif note == "C#":
                        if yourCharacter != "lord":
        			ZombieCs()
        		else:
                                SlayerCs()
		elif note == "D":
                        if yourCharacter != "lord":
                                ZombieD()
			else:
                                SlayerD()
		elif note == "D#":
                        if yourCharacter != "lord":
                                ZombieDs()
			else:
                                SlayerDs()
		elif note == "E":
                        if yourCharacter != "lord":
                                ZombieE()
			else:
                                SlayerE()
		elif note == "F":
                        if yourCharacter != "lord":
        			ZombieF()
        		else:
                                SlayerF()
		elif note == "F#":
                        if yourCharacter != "lord":
        			ZombieFs()
        		else:
                                SlayerFs()
		elif note == "G":
                        if yourCharacter != "lord":
                                ZombieG()
                        else:
                                SlayerG()
		elif note == "G#":
                        if yourCharacter != "lord":
                                ZombieGs()
			else:
                                SlayerGs()
		else:
			print "must be something else"

		if yourCharacter != "lord":
#taunts
#                        if lordHits%15 == 1:
#                                lordMessage()

                        if lordObjectNumber <= 600:
                		lordObjectNumber += (xposIncrementor * xposSpace)
                                print 'objectNumber', lordObjectNumber
                        else: 
        			lordObjectNumber = 0
                                playerTurn = 0
                                switchTurn()

                else:
#taunts
#                        if slayerHits%15 == 1:
#                                slayerMessage()
                        if slayerObjectNumber <= 600:
                                slayerObjectNumber += (xposIncrementor * xposSpace)
                                print 'objectNumber', slayerObjectNumber
                        else: 
        			slayerObjectNumber = 0
                                playerTurn = 0
                                switchTurn()


	else:
		print "opponent electricity!"

def printYourNote(note):
	print "you played:", note

def printOppNote(note):
	print "your opponent played:", note

def main(winstyle = 0, characterChoice = ""):
	if pygame.mixer:
		pygame.mixer.music.fadeout(1000)
		
        global yourCharacter
        global playerTurn
        global slayerHits
        global lordHits
	# Initialize pygame
	pygame.init()
	#initialize open sound control
	osc.init()
	print "playing as", characterChoice
	yourCharacter = characterChoice
	if yourCharacter == "lord":
                playerTurn = 0
        else:
                playerTurn = 1
        #bind functions to osc addresses
	inSocket = osc.createListener('127.0.0.1', 7800)
	osc.bind(maxYourNote, "/max/you")
	osc.bind(maxOppNote, "/max/opponent")
	
	if pygame.mixer and not pygame.mixer.get_init():
		print 'Warning, no sound'
		pygame.mixer = None

	# Set the display mode
	winstyle = 0  # |FULLSCREEN
	bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
	screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

	#Load images, assign to sprite classes
	#(do this before the classes are used, after screen setup)
	img = load_image('player1.gif')
	img = load_image('boom.png')
	Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
	ZombieA.images = load_images('zombie-a1.png', 'zombie-a2.png', 'zombie-a3.png', 'zombie-a4.png')
	ZombieAs.images = load_images('zombie-a#1.png', 'zombie-a#2.png', 'zombie-a#3.png', 'zombie-a#4.png')
	ZombieB.images = load_images('zombie-b1.png', 'zombie-b2.png', 'zombie-b3.png', 'zombie-b4.png')
	ZombieC.images = load_images('zombie-c1.png', 'zombie-c2.png', 'zombie-c3.png', 'zombie-c4.png')
	ZombieCs.images = load_images('zombie-c#1.png', 'zombie-c#2.png', 'zombie-c#3.png', 'zombie-c#4.png')
	ZombieD.images = load_images('zombie-d1.png', 'zombie-d2.png', 'zombie-d3.png', 'zombie-d4.png')
	ZombieDs.images = load_images('zombie-d#1.png', 'zombie-d#2.png', 'zombie-d#3.png', 'zombie-d#4.png')
	ZombieE.images = load_images('zombie-e1.png', 'zombie-e2.png', 'zombie-e3.png', 'zombie-e4.png')
	ZombieF.images = load_images('zombie-f1.png', 'zombie-f2.png', 'zombie-f3.png', 'zombie-f4.png')
	ZombieFs.images = load_images('zombie-f#1.png', 'zombie-f#2.png', 'zombie-f#3.png', 'zombie-f#4.png')
	ZombieG.images = load_images('zombie-g1.png', 'zombie-g2.png', 'zombie-g3.png', 'zombie-g4.png')
	ZombieGs.images = load_images('zombie-g#1.png', 'zombie-g#2.png', 'zombie-g#3.png', 'zombie-g#4.png')
		
	SlayerA.images = load_images('slayer-a1.png', 'slayer-a2.png', 'slayer-a3.png', 'slayer-a4.png')
	SlayerAs.images = load_images('slayer-a#1.png', 'slayer-a#2.png', 'slayer-a#3.png', 'slayer-a#4.png')
	SlayerB.images = load_images('slayer-b1.png', 'slayer-b2.png', 'slayer-b3.png', 'slayer-b4.png')
	SlayerC.images = load_images('slayer-c1.png', 'slayer-c2.png', 'slayer-c3.png', 'slayer-c4.png')
	SlayerCs.images = load_images('slayer-c#1.png', 'slayer-c#2.png', 'slayer-c#3.png', 'slayer-c#4.png')
	SlayerD.images = load_images('slayer-d1.png', 'slayer-d2.png', 'slayer-d3.png', 'slayer-d4.png')
	SlayerDs.images = load_images('slayer-d#1.png', 'slayer-d#2.png', 'slayer-d#3.png', 'slayer-d#4.png')
	SlayerE.images = load_images('slayer-e1.png', 'slayer-e2.png', 'slayer-e3.png', 'slayer-e4.png')
	SlayerF.images = load_images('slayer-f1.png', 'slayer-f2.png', 'slayer-f3.png', 'slayer-f4.png')
	SlayerFs.images = load_images('slayer-f#1.png', 'slayer-f#2.png', 'slayer-f#3.png', 'slayer-f#4.png')
	SlayerG.images = load_images('slayer-g1.png', 'slayer-g2.png', 'slayer-g3.png', 'slayer-g4.png')
	SlayerGs.images = load_images('slayer-g#1.png', 'slayer-g#2.png', 'slayer-g#3.png', 'slayer-g#4.png')

	#decorate the game window
	icon = pygame.transform.scale(ZombieA.images[0], (50, 100))
	pygame.display.set_icon(icon)
	pygame.display.set_caption('Children of the Shred')
	pygame.mouse.set_visible(0)

	#create the background, tile the bgd image
	bgdtile = load_image('bg2.gif')
	background = pygame.Surface(SCREENRECT.size)
	for x in range(0, SCREENRECT.width, bgdtile.get_width()):
		background.blit(bgdtile, (x, 0))
	screen.blit(background, (0,0))
	pygame.display.flip()

	#load the sound effects
	boom_sound = load_sound('boom.wav')

#background music
	#if pygame.mixer:
	#	music = os.path.join('data', 'house_lo.wav')
	#	pygame.mixer.music.load(music)
	#	pygame.mixer.music.play(-1)

	# Initialize Game Groups
	zombiesA = pygame.sprite.Group()
	zombiesAs = pygame.sprite.Group()
	zombiesB = pygame.sprite.Group()
	zombiesC = pygame.sprite.Group()
	zombiesCs = pygame.sprite.Group()
	zombiesD = pygame.sprite.Group()
	zombiesDs = pygame.sprite.Group()
	zombiesE = pygame.sprite.Group()
	zombiesF = pygame.sprite.Group()
	zombiesFs = pygame.sprite.Group()
	zombiesG = pygame.sprite.Group()
	zombiesGs = pygame.sprite.Group()
		
	slayersA = pygame.sprite.Group()
	slayersAs = pygame.sprite.Group()
	slayersB = pygame.sprite.Group()
	slayersC = pygame.sprite.Group()
	slayersCs = pygame.sprite.Group()
	slayersD = pygame.sprite.Group()
	slayersDs = pygame.sprite.Group()
	slayersE = pygame.sprite.Group()
        slayersF = pygame.sprite.Group()
        slayersFs = pygame.sprite.Group()
        slayersG = pygame.sprite.Group()
        slayersGs = pygame.sprite.Group()
        slayerMessages = pygame.sprite.Group()
        lordMessages = pygame.sprite.Group()
        switchTurns = pygame.sprite.Group()
        gameOvers = pygame.sprite.Group()
	all = pygame.sprite.RenderUpdates()

	#assign default groups to each sprite class
	ZombieA.containers = zombiesA, all
	ZombieAs.containers = zombiesAs, all
	ZombieB.containers = zombiesB, all
	ZombieC.containers = zombiesC, all
	ZombieCs.containers = zombiesCs, all
	ZombieD.containers = zombiesD, all
	ZombieDs.containers = zombiesDs, all
	ZombieE.containers = zombiesE, all
	ZombieF.containers = zombiesF, all
	ZombieFs.containers = zombiesFs, all
	ZombieG.containers = zombiesG, all
	ZombieGs.containers = zombiesGs, all
	SlayerA.containers = slayersA, all
        SlayerAs.containers = slayersAs, all
        SlayerB.containers = slayersB, all
        SlayerC.containers = slayersC, all
        SlayerCs.containers = slayersCs, all
        SlayerD.containers = slayersD, all
        SlayerDs.containers = slayersDs, all
        SlayerE.containers = slayersE, all
        SlayerF.containers = slayersF, all
        SlayerFs.containers = slayersFs, all
        SlayerG.containers = slayersG, all
        SlayerGs.containers = slayersGs, all
        
        switchTurn.containers = switchTurns, all
        gameOver.containers = gameOvers, all
	slayerMessage.containers = slayerMessages, all
        lordMessage.containers = lordMessages, all
	Explosion.containers = all
	Score.containers = all
        timeLeft.containers = all
        
	#Create Some Starting Values
	global score
	global score2
	kills = 0
	clock = pygame.time.Clock()

	#initialize our starting sprites
	global SCORE
	global SCORE2
	global TIMELEFT
	if pygame.font:
		all.add(Score())
		all.add(Score2())
		all.add(timeLeft())
        ticks = pygame.time.get_ticks()
        killtime = 0
        switchTurn()

#makes the game run forever.  this can run a timer as well for timed battles.
	while killtime < 180000:
                
		osc.getOSC(inSocket)
                killtime = pygame.time.get_ticks() - ticks
                TIMELEFT = 180 - (killtime / 1000)
		#get input
		for event in pygame.event.get():
			if event.type == QUIT or \
				(event.type == KEYDOWN and event.key == K_ESCAPE):
					osc.dontListen()
					return
		keystate = pygame.key.get_pressed()

		# clear/erase the last drawn sprites
		all.clear(screen, background)

		#update all the sprites
		all.update()

		# Detect collisions
		#for alien in pygame.sprite.spritecollide(player, aliens, 1):
		#	boom_sound.play()
		#	Explosion(alien)
		#	Explosion(player)
		#	SCORE = SCORE + 1
			#player.kill()
		for zombiea in pygame.sprite.groupcollide(slayersA, zombiesA, 1, 1).keys():
			boom_sound.play()
			Explosion(zombiea)
			if zombiea.points > (800 - zombiea.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1
			SCORE = SCORE + zombiea.points
                        SCORE2 = SCORE2 + 800 - zombiea.points
                        
		for zombieas in pygame.sprite.groupcollide(slayersAs, zombiesAs, 1, 1).keys():
			boom_sound.play()
			Explosion(zombieas)
			if zombieas.points > (800 - zombieas.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1
			SCORE = SCORE + zombieas.points
                        SCORE2 = SCORE2 + 600 - zombieas.points

		for zombieb in pygame.sprite.groupcollide(slayersB, zombiesB, 1, 1).keys():
			boom_sound.play()
			Explosion(zombieb)
			if zombieb.points > (800 - zombieb.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1
			
			SCORE = SCORE + zombieb.points
                        SCORE2 = SCORE2 + 600 - zombieb.points

		for zombiec in pygame.sprite.groupcollide(slayersC, zombiesC, 1, 1).keys():
			boom_sound.play()
			Explosion(zombiec)
			if zombiec.points > (800 - zombiec.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1

			SCORE = SCORE + zombiec.points
			SCORE2 = SCORE2 + 600 - zombiec.points


		for zombiecs in pygame.sprite.groupcollide(slayersCs, zombiesCs, 1, 1).keys():
			boom_sound.play()
			Explosion(zombiecs)
			if zombiecs.points > (800 - zombiecs.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1

			SCORE = SCORE + zombiecs.points
			SCORE2 = SCORE2 + 600 - zombiecs.points


		for zombied in pygame.sprite.groupcollide(slayersD, zombiesD, 1, 1).keys():
			boom_sound.play()
			Explosion(zombied)
			if zombied.points > (800 - zombied.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1

			SCORE = SCORE + zombied.points
                        SCORE2 = SCORE2 + 600 - zombied.points
                        
		for zombieds in pygame.sprite.groupcollide(slayersDs, zombiesDs, 1, 1).keys():
			boom_sound.play()
			Explosion(zombieds)
			if zombieds.points > (800 - zombieds.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1

			SCORE = SCORE + zombieds.points
			SCORE2 = SCORE2 + 600 - zombieds.points
			
		for zombiee in pygame.sprite.groupcollide(slayersE, zombiesE, 1, 1).keys():
			boom_sound.play()
			Explosion(zombiee)
			if zombiee.points > (800 - zombiee.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1

			SCORE = SCORE + zombiee.points
			SCORE2 = SCORE2 + 600 - zombiee.points

		for zombief in pygame.sprite.groupcollide(slayersF, zombiesF, 1, 1).keys():
			boom_sound.play()
			Explosion(zombief)
			if zombief.points > (800 - zombief.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1

			SCORE = SCORE + zombief.points
			SCORE2 = SCORE2 + 600 - zombief.points

		for zombiefs in pygame.sprite.groupcollide(slayersFs, zombiesFs, 1, 1).keys():
			boom_sound.play()
			Explosion(zombiefs)
			if zombiefs.points > (800 - zombiefs.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1

			SCORE = SCORE + zombiefs.points
                        SCORE2 = SCORE2 + 600 - zombiefs.points
                        
		for zombieg in pygame.sprite.groupcollide(slayersG, zombiesG, 1, 1).keys():
			boom_sound.play()
			Explosion(zombieg)
			if zombieg.points > (800 - zombieg.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1

			SCORE = SCORE + zombieg.points
			SCORE2 = SCORE2 + 600 - zombieg.points

		for zombiegs in pygame.sprite.groupcollide(slayersGs, zombiesGs, 1, 1).keys():
			boom_sound.play()
			Explosion(zombiegs)
			if zombiegs.points > (800 - zombiegs.points):
                                lordHits = lordHits + 1
                        else:
                                slayerHits = slayerHits + 1

			SCORE = SCORE + zombiegs.points
			SCORE2 = SCORE2 + 600 - zombiegs.points
                
		#game timer
		#turntimer = pygame.time.get_ticks()
		#print turntimer
	
		#draw the scene
		dirty = all.draw(screen)
		pygame.display.update(dirty)

		#cap the framerate
		clock.tick(40)
		
#end of game
	gameOver()
#without that function, it will go back to the main menu
	if pygame.mixer:
		pygame.mixer.music.fadeout(1000)
	pygame.time.wait(1000)
	
	if pygame.mixer:
		pygame.mixer.music.play(-1)



#call the "main" function if running this script
if __name__ == '__main__': main()

