import pygame;
import random
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
snake_size=22;
fps=60
food_x=random.randint(20,int(Screen_width/2))
food_y=random.randint(20,int(Screen_height/2))
score=0;
init_velocity=5

snk_list=[]
snk_length=1;
# Game looop
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
   screen_text=font.render(text,True,color);
   gamewindow.blit(screen_text,(x,y))

def plot_snake (gamewindowc, color, snk_list,snake_size) :
#    print(snk_list)
   for x,y in snk_list:
    
       pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])
    
while not exit_game:
    for event in pygame.event.get():
    #    print(event)
       if event.type == pygame.QUIT:
         exit_game = True;
    
       if event.type==pygame.KEYDOWN:
          if event.key== pygame.K_RIGHT:
            #  snake_x+=10;
            velocity_x=init_velocity;
            velocity_y=0
          if event.key== pygame.K_LEFT:
            #  snake_x-=10;
            velocity_x=-init_velocity;
            velocity_y=0
          if event.key== pygame.K_UP:
            #  snake_y-=10
            velocity_y=-init_velocity
            velocity_x=0;

          if event.key== pygame.K_DOWN:
            #  snake_y+=10;
            velocity_y=init_velocity
            velocity_x=0;
    snake_x=snake_x+velocity_x;
    snake_y=snake_y+velocity_y;
    if abs(snake_x-food_x)<23 and abs(snake_y-food_y)<23:
       score+=1;
    #    print(score)
      
       food_x=random.randint(20,int(Screen_width/2))
       food_y=random.randint(20,int(Screen_height/2))
       snk_length+=5;
    gamewindow.fill(white)
    text_screen("Score: "+str(score*10),red,5,5),
    pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    if len(snk_list)>snk_length:
       del snk_list[0]
    # pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
    plot_snake(gamewindow,black,snk_list,snake_size)
    pygame.display.update()
    clock.tick(fps);

pygame.quit();
quit();