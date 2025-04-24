import pygame;
import random
import os

"""
if len(snk_list) > snk_length:
    del snk_list[0]  # 🔴 Remove old tail
👆 Yeh line ensure karti hai ki snk_list me hamesha sirf snk_length ke jitne hi coordinates rahein!
  if length==1 ye ensure karta hai ki one elem list mein add hoga and another delete hoga due to  list>len

1️⃣ Pehla move → snk_list = [[45, 55]]
2️⃣ Dusra move → snk_list = [[50, 55], [45, 55]]
3️⃣ Teesra move → snk_list = [[55, 55], [50, 55], [45, 55]]
4️⃣ Chautha move → snk_list = [[60, 55], [55, 55], [50, 55], [45, 55]]
5️⃣ Paanchva move → snk_list = [[65, 55], [60, 55], [55, 55], [50, 55], [45, 55]]
6️⃣ Chhatha move → snk_list = [[70, 55], [65, 55], [60, 55], [55, 55], [50, 55]] (🔥 Purana [45, 55] delete ho gaya!)

matlab ye code ensure karta hai ki jab wo apple khata hai to size grow karta hai and har move pein snkate ka size jitna rectangle plot karta hai and
maximum 6 point list mein add karta hai uss se jyada ku delete karta hain and move ke basis pe chalta hai

snake move coordinate se 5 coordinate tak plot draw karta hai phi ese karte karte rectangle ko draw karta hai jo humko snake
grow karne jesa lagta hai per actually grow nehi karti wo
"""


pygame.mixer.init()
pygame.init();
Screen_width=900;
Screen_height=600;




# colors
white=(255, 255, 255)
red=(255,0,0)
black=(0,0,0)
gamewindow=pygame.display.set_mode((Screen_width,Screen_height))
bgimg=pygame.image.load("wp3906260.jpg")
bgimg=pygame.transform.scale(bgimg,(Screen_width,Screen_height)).convert_alpha()
# game title
pygame.display.set_caption("Snake Game")
pygame.display.update()


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

def plot_snake (gamewindow, color, snk_list,snake_size) :
    #    print(snk_list)
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game=False;
    while not exit_game:
        gamewindow.fill(white)
        text_screen("welcome to snakeGame",black,100,200)  
        text_screen("press Enter to Play",black,100,250)  
        for event in pygame.event.get():
          if event.type==pygame.QUIT:
             exit_game=True
          if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_SPACE:
                pygame.mixer.music.load('gardens-stylish-chill-303261.mp3')
                       
                    #    lofi-background-music-309034
                pygame.mixer.music.play()
                gameloop()
        pygame.display.update()
        clock.tick(fps)

def gameloop():
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
        if (not os.path.exists("hiscore.txt")):
           with open("hiscore.txt","w") as f:
              f.write("0");
        with open ("hiscore.txt","r") as f:
            hiscore=f.read();
            
        while not exit_game:
            if game_over:
                with open ("hiscore.txt","w") as f:
                   f.write(str(hiscore))
                gamewindow.fill(white)

                text_screen("Game Over press Enter To continue",red,int(100),int(200))
                for event in pygame.event.get():
                 #    print(event)
                   if event.type == pygame.QUIT:
                     exit_game = True;
                   if event.type==pygame.KEYDOWN:
                      if event.key==pygame.K_RETURN:
                           gameloop()
                   
            else:
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
                    if event.key==pygame.K_q:
                       score+=10;
                snake_x=snake_x+velocity_x;
                snake_y=snake_y+velocity_y;
                if abs(snake_x-food_x)<23 and abs(snake_y-food_y)<23:
                  if(score>int(hiscore)):
                     hiscore=score;
                  score+=10;
                #    print(score)
                
                  food_x=random.randint(20,int(Screen_width/2))
                  food_y=random.randint(20,int(Screen_height/2))
                  snk_length+=5;
                gamewindow.fill(white)
                gamewindow.blit(bgimg,(0,0))
                text_screen("Score: "+str(score)+"Hiscore: "+str(hiscore),red,5,5),
                pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
                head=[]
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)
                # print(snk_list)
                if len(snk_list)>snk_length:
                  del snk_list[0]
                if head in snk_list[:-1]:
                   game_over=True 
                   pygame.mixer.music.load('lofi-background-music-309034.mp3')
                   pygame.mixer.music.play()
                # pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
                if(snake_x<0 or snake_x>Screen_width or snake_y<0 or snake_y>Screen_height):
                    game_over=True;
                    pygame.mixer.music.load('lofi-background-music-309034.mp3')
                    pygame.mixer.music.play()
                plot_snake(gamewindow,black,snk_list,snake_size)
            pygame.display.update()
            clock.tick(fps);

        pygame.quit();
        quit();

welcome()
# gameloop();