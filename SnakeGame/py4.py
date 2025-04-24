import pygame
import random
import os
import time

pygame.mixer.init()
pygame.init()

# Screen setup
Screen_width = 900
Screen_height = 600
gamewindow = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red_food = (200, 0, 0)
eye_color = (255, 255, 255)

# Load and scale background
bgimg = pygame.image.load("wp3906260.jpg")
bgimg = pygame.transform.scale(bgimg, (Screen_width, Screen_height)).convert_alpha()

# Fonts and clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# Gradient text renderer
def render_gradient_text(text, font, gradient_colors):
    base = font.render(text, True, (255, 255, 255))
    width, height = base.get_size()
    gradient = pygame.Surface((width, height)).convert_alpha()

    for y in range(height):
        ratio = y / height
        r = int(gradient_colors[0][0] * (1 - ratio) + gradient_colors[1][0] * ratio)
        g = int(gradient_colors[0][1] * (1 - ratio) + gradient_colors[1][1] * ratio)
        b = int(gradient_colors[0][2] * (1 - ratio) + gradient_colors[1][2] * ratio)
        pygame.draw.line(gradient, (r, g, b), (0, y), (width, y))

    base.blit(gradient, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return base

# Snake rendering
def plot_snake(window, snk_list, size):
    head_color = (34, 139, 34)
    tail_color = (144, 238, 144)

    for i, (x, y) in enumerate(snk_list):
        ratio = i / len(snk_list) if len(snk_list) > 1 else 1
        r = int(head_color[0] * (1 - ratio) + tail_color[0] * ratio)
        g = int(head_color[1] * (1 - ratio) + tail_color[1] * ratio)
        b = int(head_color[2] * (1 - ratio) + tail_color[2] * ratio)
        pygame.draw.rect(window, (r, g, b), [x, y, size, size])

        if i == len(snk_list) - 1:
            eye_radius = size // 6
            eye_offset_x = size // 4
            eye_offset_y = size // 4
            pygame.draw.circle(window, eye_color, (x + eye_offset_x, y + eye_offset_y), eye_radius)
            pygame.draw.circle(window, eye_color, (x + size - eye_offset_x, y + eye_offset_y), eye_radius)

# Welcome screen
def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        text = font.render("Welcome to Snake Game", True, black)
        text2 = font.render("Press SPACE to Play", True, black)
        gamewindow.blit(text, (100, 200))
        gamewindow.blit(text2, (100, 250))

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

# Main game loop
def gameloop():
    exit_game = False
    game_over = False
    pause = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 22
    food_x = random.randint(20, int(Screen_width / 2))
    food_y = random.randint(20, int(Screen_height / 2))
    score = 0
    init_velocity = 5
    velocity = init_velocity
    fps = 60
    snk_list = []
    snk_length = 1
    start_time = time.time()

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
            gamewindow.blit(font.render("Game Over! Press ENTER to Restart", True, red_food), (100, 200))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        elif pause:
            pause_text = font.render("Paused - Press R to Resume", True, black)
            gamewindow.blit(pause_text, (200, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    pause = False
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and velocity_x != -velocity:
                        velocity_x = velocity
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT and velocity_x != velocity:
                        velocity_x = -velocity
                        velocity_y = 0
                    elif event.key == pygame.K_UP and velocity_y != velocity:
                        velocity_y = -velocity
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN and velocity_y != -velocity:
                        velocity_y = velocity
                        velocity_x = 0
                    elif event.key == pygame.K_q:
                        score += 10
                    elif event.key == pygame.K_p:
                        pause = True

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 23 and abs(snake_y - food_y) < 23:
                score += 10
                if score > int(hiscore):
                    hiscore = score
                food_x = random.randint(20, int(Screen_width / 2))
                food_y = random.randint(20, int(Screen_height / 2))
                snk_length += 5

                # Increase speed every 50 points
                if score % 50 == 0:
                    velocity += 1

            gamewindow.fill(white)
            gamewindow.blit(bgimg, (0, 0))

            score_text = render_gradient_text(f"Score: {score}", font, [(0, 255, 255), (255, 0, 255)])
            hiscore_text = render_gradient_text(f"Hiscore: {hiscore}", font, [(255, 0, 0), (255, 215, 0)])
            gamewindow.blit(score_text, (5, 5))
            gamewindow.blit(hiscore_text, (5, 45))

            elapsed_time = int(time.time() - start_time)
            time_text = font.render(f"Time: {elapsed_time}s", True, black)
            gamewindow.blit(time_text, (700, 5))

            pygame.draw.circle(gamewindow, red_food, (food_x + snake_size // 2, food_y + snake_size // 2), snake_size // 2)

            head = [snake_x, snake_y]
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1] or snake_x < 0 or snake_x > Screen_width or snake_y < 0 or snake_y > Screen_height:
                game_over = True
                pygame.mixer.music.load('lofi-background-music-309034.mp3')
                pygame.mixer.music.play()

            plot_snake(gamewindow, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
