import pygame

#Parametres de la fenetre
nombre_sprite_cote = 15
nbcol= 15
nblig = 15
startlig = 1 
startcol = 3 
wall = '*' 
numberoftools=3
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite

#Personnalisation de la fenetre
titre_fenetre = "Mac Gyver"
image_icone = "images/MacGyver.png"

#Listes des images du jeu
image_wall = "images/wall.png"
image_gardien = "images/Gardien.png"
image_mac = "images/MacGyver.png"
image_tool = "images/seringue.png"
image_floor = "images/floor.png"
UP = pygame.K_UP
DOWN = pygame.K_DOWN
RIGHT = pygame.K_RIGHT
LEFT = pygame.K_LEFT
KEYDOWN= pygame.KEYDOWN
