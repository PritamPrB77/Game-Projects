import pygame
import random
import os

pygame.mixer.init()
pygame.init()

Screen_width = 900
Screen_height = 600

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

gamewindow = pygame.display.set_mode((Screen_width, Screen_height))
bgimg = pygame.image.load("wp3906260.jpg")
bgimg = pygame.transform.scale(bgimg, (Screen_width, Screen_height)).convert_alpha()

# Game title
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, (x, y))

def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        text_screen("Welcome to Snake Game", black, 100, 200)
        text_screen("Press SPACE to Play", black, 100, 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('gardens-stylish-chill-303261.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        
        pygame.display.update()
        clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 22
    fps = 60
    food_x = random.randint(20, int(Screen_width / 2))
    food_y = random.randint(20, int(Screen_height / 2))
    score = 0
    init_velocity = 5
    snk_list = []
    snk_length = 1

    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gamewindow.fill(white)
            text_screen("Game Over! Press ENTER to Restart", red, 100, 200)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    # the code ensure that it cant move 180 degree in both top bottom or left or right
                    # and velocity_x != -init_velocity:  it ensure if you presss up then direct you cant press down and if you press doen then 
                    # you cant press up+
                    if event.key == pygame.K_RIGHT and velocity_x != -init_velocity:
                        velocity_x = init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT and velocity_x != init_velocity:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_UP and velocity_y != init_velocity:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN and velocity_y != -init_velocity:
                        velocity_y = init_velocity
                        velocity_x = 0
                    elif event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 23 and abs(snake_y - food_y) < 23:
                if score > int(hiscore):
                    hiscore = score
                score += 10
                food_x = random.randint(20, int(Screen_width / 2))
                food_y = random.randint(20, int(Screen_height / 2))
                snk_length += 5

            gamewindow.fill(white)
            gamewindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + " Hiscore: " + str(hiscore), red, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
            
            head = [snake_x, snake_y]
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('lofi-background-music-309034.mp3')
                pygame.mixer.music.play()
            
            if snake_x < 0 or snake_x > Screen_width or snake_y < 0 or snake_y > Screen_height:
                game_over = True
                pygame.mixer.music.load('lofi-background-music-309034.mp3')
                pygame.mixer.music.play()
            
            plot_snake(gamewindow, black, snk_list, snake_size)
        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()