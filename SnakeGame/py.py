import pygame;
pygame.init();
Screen_width=900;
Screen_height=600;

# colors
white=(255, 255, 255)
red=(255,0,0)
black=(0,0,0)
gamewindow=pygame.display.set_mode((Screen_width,Screen_height))
# game title
pygame.display.set_caption("Snake Game")
pygame.display.update()
# game specific variables
exit_game=False;
game_over=False;
snake_x=45;
snake_y=55
velocity_x=0;
velocity_y=0
snake_size=10;
fps=30
# Game looop
clock=pygame.time.Clock()
while not exit_game:
    for event in pygame.event.get():
    #    print(event)
       if event.type == pygame.QUIT:
         exit_game = True;
    
       if event.type==pygame.KEYDOWN:
          if event.key== pygame.K_RIGHT:
            #  snake_x+=10;
            velocity_x=10;
            velocity_y=0
          if event.key== pygame.K_LEFT:
            #  snake_x-=10;
            velocity_x=-10;
            velocity_y=0
          if event.key== pygame.K_UP:
            #  snake_y-=10
            velocity_y=-10
            velocity_x=0;

          if event.key== pygame.K_DOWN:
            #  snake_y+=10;
            velocity_y=10
            velocity_x=0;
    snake_x=snake_x+velocity_x;
    snake_y=snake_y+velocity_y;
    gamewindow.fill(white)
    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps);

pygame.quit();
quit();