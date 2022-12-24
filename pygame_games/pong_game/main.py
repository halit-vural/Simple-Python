import pygame
import sys

def animate(ball):
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    
    if ball.left <= 0 or ball.right >= screen_width:
        # ball_speed_x *= -1
        reset(ball)

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def reset(ball):
    ball.x = center_x - ball_size//2
    ball.y = center_y - ball_size//2

def handle_player(player, speed):
    global screen_height
    player.y += speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def animate_opponent(opponent, speed, ball):
    if opponent.top < ball.y:
        opponent.top += speed
    if opponent.bottom > ball.y:
        opponent.bottom -= speed
    
    if opponent.top <= 0:
        opponent.top = 0
    
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

#general setup
pygame.init()
clock = pygame.time.Clock()
TICK_COUNT = 30

#setup window
screen_width = 960
screen_height = 600

center_x = screen_width//2
center_y = screen_height//2

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong Game 1.0')

ball_size = 10
ball_x = center_x - ball_size//2
ball_y = center_y - ball_size//2
ball = pygame.Rect(ball_x, ball_y, ball_size, ball_size)

player_width = 5
player_height = 140
player_x = screen_width - player_width*2
player_y = center_y - player_height//2

player = pygame.Rect(player_x, player_y, player_width, player_height)
player_speed = 0

opponent = pygame.Rect(player_width, player_y, player_width, player_height)
opponent_speed = 0

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

move_speed = 7
ball_speed_x = move_speed
ball_speed_y = move_speed


while True:
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed = move_speed

            if event.key == pygame.K_UP:
                player_speed = -move_speed
            
        if event.type == pygame.KEYUP:
            player_speed = 0
            # if event.key == pygame.K_DOWN:
            #     player_speed -= move_speed
            # if event.type == pygame.K_UP:
            #     player_speed = move_speed

    animate(ball)
    handle_player(player, player_speed)
    animate_opponent(opponent, move_speed, ball)

    #visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (center_x,0), (center_x, screen_height))



    pygame.display.flip()
    clock.tick(TICK_COUNT)