import pygame as pg 
pg.init()

# creating window 
gameWindow=pg.display.set_mode((1200,500))
pg.display.set_caption("My First Game ")

# Game specific variables 
exit_game=False #gamer stops the game by himself
game_over=False #game over  