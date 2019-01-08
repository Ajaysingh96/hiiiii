#space invader

import turtle
import os
import math
import random
#set up screen
wn =turtle.Screen()
wn.bgcolor("black")
wn.title("space Invaders")
wn.bgpic("giphy.gif")

#register the enemy picture
#turtle.register_shape("inv.gif")
#draw border using pen
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score to 0
score = 0
#draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring ="score: %s" %score
score_pen.write(scorestring,False,align="left",font=("arial",14,"normal"))
score_pen.hideturtle()
#create the player Turtle
player=turtle.Turtle()
player.hideturtle()
player.color("Red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)            #default head direction is -> 360
player.showturtle()
#use arrow keys to move player
playerspeed = 15   #move 15 pixels each time

# create the enemy
'''enemy = turtle.Turtle()
enemy.hideturtle()
enemy.color("green")
enemy.shape("circle")
enemy.penup()  #we dont want enemy to draw anything in background so penup
enemy.speed(0)
enemy.showturtle()
enemy.setposition(-250, 200)
enemyspeed = 2
'''
#create multiple enemies using list
   # choose a number of enemies
number_of_enemies = 5
enemies = []
#add enemies to empty list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("green")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200, 200)
    y = random.randint(100,250)
    enemy.setposition(x, y)

enemyspeed = 2

#create the players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.3, 0.3)
bulletspeed = 20

#define bullet state
#ready - ready to fire
#fire -bullet is firing
bulletstate = "ready"
#move layer left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280 :
        x = - 280
    player.setx(x)         #Set the turtle X coordinate to x
#move player right
def move_right():
    x = player.xcor()  #xcor return turtle x cordinate
    x +=playerspeed
    if x > 280:
        x= 280
    player.setx(x)

def fire_bullet():
    #declare buletstae as global if it needs changed
    global bulletstate  # any change in here reflect in all sowe take global
    # move bullet above players
    if bulletstate == "ready" :
        bulletstate="fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
def iscollision(t1,  t2):
    distance = math.hypot(t1.xcor()-t2.xcor(),t1.ycor()-t2.ycor())
    if distance < 15:
        return True
    else:
        return False

#create keyboard bindings
turtle.listen()  #for onclick methods
turtle.onkey(move_left,"Left")          #onkey(function,"key")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")
# main game loop
while True:
    for enemy in enemies:
        #move the enemyspeed
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

         #move enemy back and down
        if enemy.xcor() > 280:
            #MOVE ALL ENEMIES DOWN when one touches wall
            for e in enemies:
                y = e.ycor()
                y -= 40

                e.sety(y)
            enemyspeed *= -1    # when x cordinatte is greater then 280 ,then decrese by 2*-1= -2 ,eg at 280 enemy speed -2,move back

        if enemy.xcor() < -280:
            #move all enemies downs
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if iscollision(bullet, enemy):
            #reset the bullet
            bullet.hideturtle()
            bullet.setposition(0, -400)
            #reset the enemy
            x=random.randint(-200, 200)
            y = random.randint(100,250)
            enemy.setposition(x, y)
            #update score
            score += 10
            scorestring ="score: %s" %score # %score acts as a place-holder for the string data.either the string can be substituted directly, or from a variable
            score_pen.clear()  #first need to clear then write new score
            score_pen.write(scorestring,False,align="left",font=("arial",14,"normal"))

        if iscollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("game over")
            break
    #move the bulletspeed
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)


    #check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
'''    #check for collison between bullet and enemy
    if iscollision(bullet, enemy):
        #reset the bullet
        bullet.hideturtle()
        bullet.setposition(0, -400)
        #reset the enemy
        enemy.setposition(-200, 250)
    if iscollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("game over")
        break'''

delay=input("press enter to finish")
