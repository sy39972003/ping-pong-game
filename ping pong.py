import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Ping Pong!")

#code for creating ball and bars
back = pygame.Surface((640,480))
background = back.convert()
background.fill((0,0,0))

bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((0,0,255))
bar2 = bar.convert()
bar2.fill((255,0,0))

circ_sur = pygame.Surface((15,15))
ball = pygame.draw.circle(circ_sur,(0,255,0),(15/2,15/2),15/2)
ball = circ_sur.convert()
ball.set_colorkey((0,0,0))

# initializations
bar1_x, bar2_x = 10. , 620.
bar1_y, bar2_y = 215. , 215.
ball_x, ball_y = 307.5, 232.5
bar1_move, bar2_move = 0. , 0.
speed_x, speed_y, speed_ball = 240., 240., 240.
bar1_score, bar2_score = 0,0

#soundObj = pygame.mixer.Sound('beeps.wav')

#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial",30)

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                bar1_move = -ai_speed
            elif event.key == K_UP:
                bar2_move = -ai_speed
            elif event.key == K_s:
                bar1_move = ai_speed
            elif event.key == K_DOWN:
                bar2_move = ai_speed
        elif event.type == KEYUP:
            if event.key == K_w:
                bar1_move = 0.
            elif event.key == K_UP:
                bar2_move = 0.
            elif event.key == K_s:
                bar1_move = 0.
            elif event.key == K_DOWN:
                bar2_move = 0.
                
    score1 = font.render(str(bar1_score), True,(0,0,255))
    score2 = font.render(str(bar2_score), True,(255,0,0))

    screen.blit(background,(0,0))
    frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
    middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
    screen.blit(bar1,(bar1_x,bar1_y))
    screen.blit(bar2,(bar2_x,bar2_y))
    screen.blit(ball,(ball_x,ball_y))
    screen.blit(score1,(250.,210.))
    screen.blit(score2,(380.,210.))

    bar1_y += bar1_move
    bar2_y += bar2_move
    
# movement of the ball
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0
    
    ball_x += speed_x * time_sec
    ball_y += speed_y * time_sec
    ai_speed = speed_ball * time_sec
    
#code about the ball colliding with the bars
    if ball_x <= bar1_x + 10.:
        if ball_y >= bar1_y - 7.5 and ball_y <= bar1_y + 42.5:
            ball_x = 20.
            speed_x = -speed_x
    if ball_x >= bar2_x - 15.:
        if ball_y >= bar2_y - 7.5 and ball_y <= bar2_y + 42.5:
            ball_x = 605.
            speed_x = -speed_x
    if ball_x < 5.:
        #soundObj.play()
        #import time
        #time.sleep(1) # wait and let the sound play for 1 second
        #soundObj.stop()
        bar2_score += 1
        ball_x, ball_y = 320., 232.5
        bar1_y,bar_2_y = 215., 215.
    elif ball_x > 620.:
        #soundObj.play()
        #import time
        #time.sleep(1) # wait and let the sound play for 1 second
        #soundObj.stop()
        bar1_score += 1
        ball_x, ball_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
    if ball_y <= 10.:
        speed_y = -speed_y
        ball_y = 10.
    elif ball_y >= 457.5:
        speed_y = -speed_y
        ball_y = 457.5
        
    pygame.display.update()
