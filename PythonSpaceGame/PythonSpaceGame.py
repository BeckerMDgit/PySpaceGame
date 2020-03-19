
"""
    Au
    building a space invaders type game in python
"""


import turtle
import os
import math
import random


#   first need to set up screen

screen = turtle.Screen()
screen.bgcolor("black")
screen.bgpic("background.gif")
screen.title("SpaceGame")

#   register icon shapes
turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("laser.gif")

#   next draw a border

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setpos(-300,-300)
border_pen.pensize(4)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.left(90)
border_pen.hideturtle()

#   Set beginning score to 0
score = 0

#   draw the score

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setpos(-280,280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()




#   create player turtle

player = turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setpos(0,-280)
player.setheading(90)

#   create player weapon

laser = turtle.Turtle()
laser.shape("laser.gif")
laser.penup()
laser.speed(0)
laser.setheading(90)
laser.shapesize(0.5,0.5)
laser.hideturtle()

laserspeed = 25

#   define laser state
laserstate = "ready"

#   create enemy
enemy = turtle.Turtle()


#   choose number of enemies
number_of_enemies = 5

#   create an empty list of enemies
enemies = []

#   add enemies to list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setpos(x,y)
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)

enemyspeed = 6

#   now to make the player move
playerspeed = 15

def move_left():
    x = player.xcor()
    x -= playerspeed
    #boundary checking
    if x<-280:                  
        x=-280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    #boundary checking
    if x>280:                   
        x=280
    player.setx(x)

def fire_laser():
    # declare laserstate as a global
    global laserstate
    if laserstate == "ready":
        laserstate = "fire"
        # move the laser to just above the player
        x = player.xcor()
        y = player.ycor()
        laser.setpos(x,y)
        # show laser
        laser.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    
#   keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_laser, "space")


#   main game loop

while True:

    
    # move the laser
    if laserstate == "fire":
        y = laser.ycor()
        y += laserspeed
        laser.sety(y)

    # if bullet reaches top
    if laser.ycor() >280:
        laser.hideturtle()
        laserstate = "ready"

    for enemy in enemies:
        #   move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        #   move the enemy back and down
        if enemy.xcor() > 280:
            # moves all enemies together
            for e in enemies:
                y = e.ycor()
                y -= 20        
                # multiplies enemy speed by -1 to reverse enemy movement
                e.sety(y)
            enemyspeed *= -1        

        if enemy.xcor() < -280:
            # moves all enemies together
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            enemyspeed *= -1

    #   When enemy reaches bottom of screen

    for enemy in enemies:
        if enemy.ycor() < -280:
            enemyspeed *=10
            laser.hideturtle()
            player.hideturtle()
            print("Game Over")
            #   game over message
            gameover_pen = turtle.Turtle()
            gameover_pen.speed(0)
            gameover_pen.color("red")
            gameover_pen.penup()
            gameover_pen.setpos(0,0)
            gameover = "GAME OVER"
            gameover_pen.write(gameover, False, align="center", font=("Arial", 60, "normal"))
            gameover_pen.hideturtle()
            #   ask to play again
            playagain_pen = turtle.Turtle()
            playagain_pen.speed(0)
            playagain_pen.color("yellow")
            playagain_pen.penup()
            playagain_pen.setpos(0,-100)
            playagain = "Play Again? Press Y/N"
            playagain_pen.write(playagain, False, align="center", font=("Arial", 40, "normal"))
            print("Game Over")
            break

            # check for laser hit
        if isCollision(laser,enemy):
            laser.hideturtle()
            laserstate = "ready"
            laser.setpos(0,-400)
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setpos(x,y)
            # update score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(enemy,player):
            laser.hideturtle()
            player.hideturtle()
            #   game over message
            gameover_pen = turtle.Turtle()
            gameover_pen.speed(0)
            gameover_pen.color("red")
            gameover_pen.penup()
            gameover_pen.setpos(0,0)
            gameover = "GAME OVER"
            gameover_pen.write(gameover, False, align="center", font=("Arial", 60, "normal"))
            gameover_pen.hideturtle()

            #   ask to play again
            playagain_pen = turtle.Turtle()
            playagain_pen.speed(0)
            playagain_pen.color("yellow")
            playagain_pen.penup()
            playagain_pen.setpos(0,-100)
            playagain = "Play Again? Press Y/N"
            playagain_pen.write(playagain, False, align="center", font=("Arial", 40, "normal"))
            print("Game Over")
            break

delay = input("Press Enter to Exit")
raise SystemExit()
turtle.done() # game window becomes unresponsive without this command


