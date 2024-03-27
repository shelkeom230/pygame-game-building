import pygame as pg 

pg.init()

# colors 
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)
blue=(0,0,255)

screen_width=900
screen_height=600

# Game title 
pg.display.set_caption('snakes with omkar')
gameWindow=pg.display.set_mode((screen_width,screen_height))
pg.display.update()

exit_game=False 
game_over=False 
snake_x=45
snake_y=55
snake_size=20

# game loop 
while not exit_game:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            exit_game=True 
    
    gameWindow.fill(white)
    pg.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pg.display.update()

pg.quit()
quit()