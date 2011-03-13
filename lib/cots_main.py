#Game main module.
#Contains the entry point used by the run_game.py script.
#Feel free to put all your game code here, or in other modules in this "lib" directory.

from cots_data import load_image, filepath, load_bg
import pygame
from pygame.locals import *
import cots_battle
import os

#networking libraries
#import socket,select,os,sys
#from Net import *

#set server ip address
#host = "localhost"
#port = 6000
#client_connection = socket.socket()
#client_connection.connect((host,port))
#variables
screenWidth = 800
screenHeight = 600
whoami = "zombie"

backgrounds = ['splash.gif' ]
background2 = ['splash.gif' ]
icon_filename = 'game_icon.png'
font_filename = 'anything.ttf'

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

#begin screen 1
def main():
	pygame.init()
	
	if pygame.mixer and not pygame.mixer.get_init():
		print 'Warning, no sound'
		pygame.mixer = None
	
	if pygame.mixer:
		music = os.path.join('data', 'thriller.wav')
		pygame.mixer.music.load(music)
		pygame.mixer.music.play(-1)
	
	running = 1
	screen = pygame.display.set_mode( (screenWidth, screenHeight) )
	pygame.display.set_caption( "Children of the Shred" )
	
	background, a = load_bg( backgrounds )
	icon, a = load_image( icon_filename )
	pygame.display.set_icon(icon)
    
	font = pygame.font.Font( filepath(font_filename), 40)
	fontColor = ( 215, 26, 26 )
	fontColor1 = ( 255, 255, 255 )
	backgroundColor = None #( 0, 0, 0)
	menuPosition = ( 50, 220 ) # 800x600

	Fullscreen = False
	menuItemSelected = 0
	showMenu = True

	key = { "fullscreen":K_f, "quit":K_q, "left":K_LEFT, "right":K_RIGHT, "up":K_UP, "down":K_DOWN, "fire":K_SPACE, "select":K_RETURN }
	menu = [
			{ "title": "Play", "action":"playGame"  }, \
#			{ "title": "Instructions", "action":"instructions" }, \
			{ "title": "Quit", "action":"get outta here" } \
			]

	while True:
		event = pygame.event.wait()
		if event.type == QUIT or ( event.type == KEYDOWN and ( event.key == key['quit'] ) ) :
			exit()
		
		if event.type == KEYDOWN:
			
			if event.key == key['up']:
				
				if menuItemSelected > 0 :
					menuItemSelected -= 1
					print menu[menuItemSelected]['action']
				
			elif event.key == key['down']:
				#print "it's here"
					
				if menuItemSelected < len(menu) - 1 :
					menuItemSelected += 1
					print menu[menuItemSelected]['action']
				
			elif event.key in [ key['fire'], key['select'] ] :
				print "Action: %i" % menuItemSelected
                #print "Action: %i" % menuItemSelected
				#print menu[menuItemSelected]['action']
                
                ############### Play Game ##############
				if menuItemSelected == 0:
					#from game import main
					#main()
					print "play the damn game"
					screen2()
				
				############## Show instructions ############
				elif menuItemSelected == 1:
					#presentation(phrase, pygame.font.Font( filepath(font_filename), 100), screen)
					print "show instructions"
				
				############ Show credits ##############
				elif menuItemSelected == 2:
					print "show credits"
					exit()
				
				############ Quit the game ############
				#elif menuItemSelected == 3:
					#exit()

		if showMenu:

			screen.blit(background, (0, 0))
			x, y = menuPosition
			menuItem = 0
			
			for item in menu:

				# menu[menuItem]['area'] = 0

				y += icon.get_height()
				if menuItem != menuItemSelected :
					text = font.render( item['title'], True, fontColor )
					screen.blit( text, ( x + icon.get_width() + 10, y + ( icon.get_height() - text.get_height() ) / 2 ))
				else :
					#font.set_bold(True)
					text = font.render( item['title'], True, fontColor1 )
					font.set_bold(False)
					screen.blit( icon, ( x, y ))
					screen.blit( text, ( x + icon.get_width() + 10, y + ( icon.get_height() - text.get_height() ) / 2 ))
				y += 10
				menuItem += 1
				pygame.display.update()

#begin screen 2
def screen2():
        global whoami
	print "this is screen 2"
	pygame.init()
	running = 1
	screen = pygame.display.set_mode( (screenWidth, screenHeight) )
	pygame.display.set_caption( "Children of the Shred" )
	
	background, a = load_bg( background2 )
	icon, a = load_image( icon_filename )
	pygame.display.set_icon(icon)
    
	font = pygame.font.Font( filepath(font_filename), 40)
	fontColor = ( 215, 26, 26 )
	fontColor1 = ( 255, 255, 255 )
	backgroundColor = None #( 0, 0, 0)
	menuPosition = ( 50, 220 ) # 800x600

	Fullscreen = False
	menuItemSelected = 0
	showMenu = True

	key = { "fullscreen":K_f, "quit":K_q, "left":K_LEFT, "right":K_RIGHT, "up":K_UP, "down":K_DOWN, "fire":K_SPACE, "select":K_RETURN }
	menu = [

                        { "title": "Zombie Slayer", "action":"slayer"  }, \
                        { "title": "Zombie Lord", "action":"lord"  }, \
#                        { "title": "Wait for a Game", "action":"decide" }
#			{ "title": "Battle", "action":"battle"  }, \
#			{ "title": "Pick a side", "action":"pick a side" }, \
#			{ "title": "Pick a location", "action":"location" }
			]

	while True:
		event = pygame.event.wait()
		if event.type == QUIT or ( event.type == KEYDOWN and ( event.key == key['quit'] ) ) :
			exit()
		
		if event.type == KEYDOWN:
			
			if event.key == key['up']:
				
				if menuItemSelected > 0 :
					menuItemSelected -= 1
					print menu[menuItemSelected]['action']
				
			elif event.key == key['down']:
				#print "it's here"
					
				if menuItemSelected < len(menu) - 1 :
					menuItemSelected += 1
					print menu[menuItemSelected]['action']
				
			elif event.key in [ key['fire'], key['select'] ] :
				print "Action: %i" % menuItemSelected
                
                                ############### Be the Slayer ##############
				if menuItemSelected == 0:
					#from game import main
					#print "battle"
					from cots_battle import main
                                        #SendData(client_connection,"meslayer")
                                        print "currently", whoami
                                        whoami = "slayer"
                                        print "now you are", whoami
					main(0, whoami)
				
				############## Be the Lord ############
				elif menuItemSelected == 1:
                                        from cots_battle import main
					#presentation(phrase, pygame.font.Font( filepath(font_filename), 100), screen)
					#print "choose a side"
                                        #SendData(client_connection,"melord")
                                        print "currently", whoami
                                        whoami = "lord"
                                        print "now you are", whoami
					#pickSide()
                                        main(0, whoami)
				
			#elif event.mouse
			elif event.key == K_ESCAPE:
				global main
				main()

		if showMenu:

			screen.blit(background, (0, 0))
			x, y = menuPosition
			menuItem = 0
			
			for item in menu:

				# menu[menuItem]['area'] = 0

				y += icon.get_height()
				if menuItem != menuItemSelected :
					text = font.render( item['title'], True, fontColor )
					screen.blit( text, ( x + icon.get_width() + 10, y + ( icon.get_height() - text.get_height() ) / 2 ))
				else :
					#font.set_bold(True)
					text = font.render( item['title'], True, fontColor1 )
					font.set_bold(False)
					screen.blit( icon, ( x, y ))
					screen.blit( text, ( x + icon.get_width() + 10, y + ( icon.get_height() - text.get_height() ) / 2 ))
				y += 10
				menuItem += 1
				pygame.display.update()
				
main()
