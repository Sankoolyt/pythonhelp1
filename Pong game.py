# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:24:50 2024
@author: 2004s
"""
import pygame as pgm, sys, random
## general setup of the game
pgm.init()  ## initiates all modules and is required to run any game
clock = pgm.time.Clock()
fps = 90
# window setup
width = 1280
height = 960
scr = pgm.display.set_mode((width,height)) # returns a display surface object
## for object oriented programming
## draws all the shapes and there can only be a single one
pgm.display.set_caption('Ping pang pong')

## creating empty rectangles
meth = height/2
centre = width/2
ball = pgm.Rect(centre -15, meth-15, 30,30)

player1 = pgm.Rect(width - 20, meth-30,10,140)
player2 = pgm.Rect(10, meth- 30,10,140)

bg = pgm.Color('grey12')
## player scores
player1, player2 = 0, 0
ballx = 7 * random.choice((1,-1))
bally = 7 * random.choice((1,-1))
player_speed = 0
opp_speed = 16
def ball_movement():
    global ballx, bally  # Access the global variables

    ball.x += ballx
    ball.y += bally

    ## bouncing ball off top and bottom walls
    if ball.top <= 0 or ball.bottom >= height:
        bally *= -1  # Reverse vertical direction

    ## bouncing ball off left and right walls
    if ball.left <= 0 or ball.right >= width:
        ball_restart()

    ## ball collision with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ballx *= -1  # Reverse horizontal direction on collision
def ball_restart():
    global ballx, bally
    ball.center = (centre, meth)
    bally *= random.choice((1,-1))
    ballx *= random.choice((1,-1))

def player_an():
    player1.y += player_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= height:
        player1.bottom = height
        
def opponent_intel():
    if player2.top < ball.y:
        player2.top += opp_speed
    if player2.bottom > ball.y:
        player2.bottom -= opp_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= height:
        player2.bottom = height

while True:
    ##imput
    for event in pgm.event.get():
        if event.type == pgm.QUIT:
            pgm.quit()
            sys.exit
        if event.type == pgm.KEYDOWN:
            if event.key == pgm.K_DOWN:
                player_speed += 7
            if event.key == pgm.K_UP:
                player_speed -= 7

        if event.type == pgm.KEYUP:
            if event.key == pgm.K_DOWN:
                player_speed -= 7
            if event.key == pgm.K_UP:
                player_speed += 7
    player_an()
    opponent_intel()
    ball_movement()
        ## for every event it checks user imput, if the user clicks the x 
        #the game reliably closes
    ##visuals.
    scr.fill(bg)
    pgm.draw.rect(scr,(200,200,200),player1)
    pgm.draw.rect(scr,(200,200,200),player2)
    pgm.draw.ellipse(scr,(200,200,200),ball)
    pgm.draw.aaline(scr, (200,200,200),
                    (centre,0), (centre, height))
    pgm.display.flip()
    clock.tick(fps)
