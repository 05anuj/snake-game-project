import pygame
import time
import random
import os

#initializing pygame
pygame.init()

#define colors
white = (255,255,255)  #snake color
black = (0,0,0)   #background color
red = (255,0,0)   #game over color
orange = (255,255,0)  #food color

width, height = 600, 400
# width, height = 200, 100

game_display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Anuj's Snake Game")

clock = pygame.time.Clock()

snake_width = 10
snake_speed = 25

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)

#####

def read_HighScore():
    with open(r"C:\Users\Anuj\Desktop\consistent\project_all\snake game python\highScore.txt", "r+") as f:
        # Read the contents of the file
        data = f.read()
    return data

def write_HighScore(high_score):
    with open(r"C:\Users\Anuj\Desktop\consistent\project_all\snake game python\highScore.txt", "r+") as f:
        # Write some new data to the file
        f.write(str(high_score))
        # with open("my_file.txt", "w") as f:
        #     pass    

####
def print_score(score):
    text = score_font.render("Score: "+ str(score), True, orange)
    game_display.blit(text, [0,0])
    text = score_font.render("High_Score: "+ str(read_HighScore()), True, orange)
    game_display.blit(text, [0,height-30])

def draw_snake(snake_width, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_width, snake_width])

######

def run_game():

    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    
    x_speed = 0
    y_speed = 0

    # snake_pixels = [[x-2*snake_width,y],[x-1*snake_width,y]]
    snake_pixels = []
    snake_length = 1

    food_x = round(random.randrange(0,width-snake_width) / 10.0)*10.0
    food_y = round(random.randrange(0,height-snake_width) / 10.0)*10.0
    


    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over!", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            
            high_score = read_HighScore()
            if snake_length-1 > (int)(high_score):
                high_score = snake_length-1
                write_HighScore(high_score)
            print_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close =False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close =False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_width
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_width
                    y_speed = 0
                if event.key == pygame.K_UP:
                    y_speed = -snake_width
                    x_speed = 0
                if event.key == pygame.K_DOWN:
                    y_speed = snake_width
                    x_speed = 0
        
        if x >= width or x<0 or y >= height or y<0:
            game_close = True
        
        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [food_x,food_y, snake_width, snake_width])

        snake_pixels.append([x,y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x,y]:
                game_close = True

        draw_snake(snake_width, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        # pygame.time.wait(1000)
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0,width-snake_width) / 10.0)*10.0
            food_y = round(random.randrange(0,height-snake_width) / 10.0)*10.0
            # food_x = round(random.randrange(0,width) / 10.0)*10.0
            # food_y = round(random.randrange(0,height) / 10.0)*10.0
            # print(food_x)
            # print(food_y)
            # print("kkk")
            snake_length += 1



        clock.tick(snake_speed)
        # clock.tick(1)
        # time.sleep(1)

    pygame.quit()
    quit()

run_game()

