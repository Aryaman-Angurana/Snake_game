# Snake Game


# Modules needed in the project
import turtle
import random
import time


# Score in the game
game_over = False
score = 0


# Setting the Screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(800, 700)


# Drawing the boundary of the game
t1 = turtle.Turtle()
t1.speed(0)
t1.color("grey")
t1.hideturtle()
t1.pensize(10)

t1.penup()
t1.goto(295, 295)
t1.pendown()
t1.goto(-295, 295)
t1.goto(-295, -295)
t1.goto(295, -295)
t1.goto(295, 295)

t1.pensize(20)
t1.penup()
t1.goto(0, 300)
t1.pendown()
t1.write("Snake Game ",align = "center", font= ('MV Boli', 35, 'italic'))


# Printing the Score
t2 = turtle.Turtle()
t2.penup()
t2.color("grey")
t2.hideturtle()
t2.speed(0)
t2.goto(0,-340)
t2.pendown()
t2.write("Score: {}".format(score),align = "center", font= ('MV Boli', 24, 'normal'))


# Head of the Snake
head = turtle.Turtle()
head.color("red")
head.shape('square')
head.penup()     

sleep1 = 0.2

direction = ["right"]         # starting direction of the snake


# Fruit
fruit = turtle.Turtle()
fruit.color('red')
fruit.shape('circle')
fruit.penup()
fruit.speed(0)

x = random.randint(-270, 290)//20
x *= 20
y = random.randint(-270, 290)//20
y *= 20
fruit.goto(x,y)

matrix = [] # list of all the positions on the playable screen
for i in range(-280,300,20):
    for j in range(-280,300,20):
        matrix += [[i,j]]

fruit_collide = False # boolean to check if snake has eaten the fruit


# Body of the snake
body = []
head_movements = [[0, 0], [-20, 0]]


# Functions to move the snake and check for the collisions with walls and fruit

def move_up():
    global direction
    if (direction[-1] != "down" ):
        direction += ["up"]


def move_down():
    global direction
    if (direction[-1] != "up" ):
        direction += ["down"]


def move_left():
    global direction
    if (direction[-1] != "right" ):
        direction += ["left"]


def move_right():
    global direction
    if (direction[-1] != "left" ):
        direction += ["right"]


def check_for_fruit_collision():
    global fruit_collide
    global score
    global sleep1

    fruit_collide = False
    
    # checking if the head of the snake is at the position of the fruit
    if (head.xcor() == fruit.xcor() and head.ycor() == fruit.ycor()):
        # displacing the fruit to a new place where the bosy of the snake is not present
        fruit_matrix2 = []
        for i in matrix:
            if i not in head_movements[ : -1] + [[head.xcor(), head.ycor()]]:
                fruit_matrix2 += [i]
        j = random.randint(0,1000)
        l = len(fruit_matrix2)
        j = j % l
        fruit.goto(fruit_matrix2[j][0], fruit_matrix2[j][1])
        
        score += 1
        t2.speed(0)
        t2.clear()
        t2.write("Score: {}".format(score),align = "center", font= ('MV Boli', 24, 'normal'))
        
        fruit_collide = True

        # increasing the speed the snake
        if sleep1 > 0.05:
            sleep1 -= 0.005
        elif sleep1 > 0.03:
            sleep1 -= 0.001
        elif sleep1 > 0:
            sleep1 -= 0.0002


def check_for_wall_collision():
    global game_over
    if (head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290 ):
        game_over = True


def check_for_body_collision():
    global game_over
    if [head.xcor(), head.ycor()] in head_movements[ : -2]:
        game_over = True


def move():
    global direction
    if (direction[0] == "up"):
        head.sety(head.ycor() + 20)
    elif (direction[0] == "down"):
        head.sety(head.ycor() - 20)
    elif (direction[0] == "left"):
        head.setx(head.xcor() - 20)
    elif (direction[0] == "right"):
        head.setx(head.xcor() + 20)

    if len(direction) > 1:
        direction = direction[1:]
    
    check_for_fruit_collision()
    check_for_wall_collision()
    check_for_body_collision()
    body_move()


def body_move():
    global fruit_collide
    global body
    global head_movements

    if fruit_collide:
        new_part = turtle.Turtle()
        new_part.color('white')
        new_part.shape("square")
        new_part.speed(0)
        new_part.shapesize(0.8)
        new_part.penup()
        
        body += [new_part]
        
        head_movements = [[head.xcor(), head.ycor()]] + head_movements
        
        j = 0
        for i in body:
            i.setx(head_movements[j + 1][0])
            i.sety(head_movements[j + 1][1])
            j += 1
    else:
        head_movements = [[head.xcor(), head.ycor()]] + head_movements[ : -1]
        
        j = 0
        for i in body:
            i.setx(head_movements[j + 1][0])
            i.sety(head_movements[j + 1][1])
            j += 1


# Commands
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.listen()
wn.delay(0)


# Main loop
while True:
    if(game_over):
        t3 = turtle.Turtle()
        t3.color('grey')
        t3.speed(0)
        t3.write("GAME OVER", align='center', font = ('Calibri', 40, 'bold'))
        t3.hideturtle()
        wn.mainloop()
        break
    else:
        move()
        time.sleep(sleep1)

