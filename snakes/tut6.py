import pygame as pg 
pg.init()

# creating window 
gameWindow=pg.display.set_mode((1200,500))
pg.display.set_caption("My First Game ")

# Game specific variables 
exit_game=False #gamer stops the game by himself
game_over=False #game over

# creating a game loop 
while not exit_game:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            exit_game=True 
        
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_RIGHT:
                print('You have pressed right arrow key')
                
pg.quit()
quit()