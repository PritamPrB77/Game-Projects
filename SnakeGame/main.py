import pygame
x=pygame.init();
print(x)
# creating window
gamewindow=pygame.display.set_mode((800,600))
pygame.display.set_caption("My Game")
# game specific variables
exit_game=False;
game_over=False;
# creating a game loop
while exit_game==False:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         exit_game = True;
      if event.type==pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
             print("Right Key Pressed")

pygame.quit();
quit();
