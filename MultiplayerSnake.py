import turtle
import time
import random
import winsound

delay = 0.1#snake1 speed
delay2 = 0.1#snake2 speed
score = 0
score2 = 0
high_score = 0

#Screen Setup
wn = turtle.Screen()
wn.title("Snake Game by Chris")
wn.bgcolor("black")#color of screen
wn.setup(width=600, height=600)#size of screen
wn.tracer(0)#turns off screen updates

#Borders
TopB = turtle.Turtle()
TopB.penup()
TopB.shape("square")
TopB.color("blue")
TopB.goto(0,250)
TopB.shapesize(stretch_wid=1, stretch_len = 30)
BottomB = turtle.Turtle()
BottomB.penup()
BottomB.shape("square")
BottomB.color("blue")
BottomB.goto(0,-280)
BottomB.shapesize(stretch_wid=1, stretch_len = 30)
LeftB = turtle.Turtle()
LeftB.penup()
LeftB.shape("square")
LeftB.color("blue")
LeftB.goto(-290,-20)
LeftB.shapesize(stretch_wid=27, stretch_len = 1)
RightB = turtle.Turtle()
RightB.penup()
RightB.shape("square")
RightB.color("blue")
RightB.goto(290,-20)
RightB.shapesize(stretch_wid=27, stretch_len = 1)

#Snake Head1
head = turtle.Turtle()
head.speed #animation speed, 0 is the fastest
head.shape("circle")
head.color("green")
head.penup() #takes away the line that follows
head.goto(-100,0)
head.direction = "stop"

#Snake Head2
head2 = turtle.Turtle()
head2.speed #animation speed, 0 is the fastest
head2.shape("circle")
head2.color("white")
head2.penup() #takes away the line that follows
head2.goto(100,0)
head2.direction = "stop"

#Apples
food = turtle.Turtle()
food.speed #animation speed, 0 is the fastest
food.shape("circle")
food.color("red")
food.penup() #takes away the line that follows
food.goto(0,100)

#Snake Body list
segments = []
segments2 = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)#location of pen.write
pen.write("Snake1 : 0 Snake2 : 0 High Score : 0", align="center", font=("Normal", 24, "underline"))

#Functions
#Snake 1 movement
def go_up():
    if head.direction != "down":#if head direction is not down
        head.direction = "up"#go up
def go_down():
    if head.direction != "up":#cant go up if going down
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
#Snake2 movement
def go_up2():
    if head2.direction != "down":#if head direction is not down
        head2.direction = "up"#go up
def go_down2():
    if head2.direction != "up":#cant go up if going down
        head2.direction = "down"
def go_left2():
    if head2.direction != "right":
        head2.direction = "left"
def go_right2():
    if head2.direction != "left":
        head2.direction = "right"

#Snake1 movement
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)#moves 20 pixels up
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
#Snake2 movement
def move2():
    if head2.direction == "up":
        y = head2.ycor()
        head2.sety(y + 20)#moves 20 pixels up
    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y - 20)
    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x - 20)
    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x + 20)

#Keyboard Bindings
#Snake1 
wn.listen()
wn.onkeypress(go_up, "w")#w = move up
wn.onkeypress(go_down, "s")#s = move down
wn.onkeypress(go_left, "a")#a = move left
wn.onkeypress(go_right, "d")#d = move right
#Snake2
wn.onkeypress(go_up2, "Up")#i = move up
wn.onkeypress(go_down2, "Down")#k = move down
wn.onkeypress(go_left2, "Left")#j = move left
wn.onkeypress(go_right2, "Right")#l = move right

#Main Game Loop
while True:
    wn.update()

    #Check for border collsions
    if head.xcor()>260 or head.xcor()<-260 or head.ycor()>220 or head.ycor()<-260:
        #time.sleep(1)#pauses game with collsion
        head.goto(-100,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)#sends body off screen

        segments.clear()#clear body if collision
    
        score = 0#resets score when snake hits border
        pen.clear()
        pen.write("Snake1 : {} Snake2 : {}  High Score : {}".format(score, score2, high_score), align="center", font=("Normal", 20, "underline"))

        #Reset snake speed
        delay = 0.1
    if head2.xcor()>260 or head2.xcor()<-260 or head2.ycor()>220 or head2.ycor()<-260:
        #time.sleep(1)#pauses game with collsion
        head2.goto(100,0)
        head2.direction = "stop"

        for segment in segments2:
            segment.goto(1000,1000)#sends body off screen

        segments2.clear()#clear body if collision
    
        score2 = 0#resets score when snake hits border
        pen.clear()
        pen.write("Snake1 : {} Snake2 : {}  High Score : {}".format(score, score2, high_score), align="center", font=("Normal", 20, "underline"))

        #Reset snake speed
        delay2 = 0.1

    #Check for food collisons
#Snake1
    if head.distance(food)<20:#if collision
        food.goto(random.randrange(-260,260,20), random.randrange(-260,240,20))#Move apple randomly
        #x = random.randrange(-280,280,20)
        #y = random.randint(-280,280,20)
        #food.goto(x,y)
        
        new_segment = turtle.Turtle()#add segment
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        #Sound
        winsound.PlaySound("appleeat.wav",winsound.SND_ASYNC)

        #Shorten Delay
        delay -=0.01#increases spped of snake with each apple collision

        #Scoring
        score += 10#10 for every apple
        if score > high_score:
            high_score = score#highest score becomes high score
        pen.clear()
        pen.write("Snake1 : {} Snake2 : {} High Score : {}".format(score, score2, high_score), align="center", font=("Normal", 20, "underline"))
    #Snake2
    if head2.distance(food)<20:#if collision
        food.goto(random.randrange(-260,260,20), random.randrange(-260,240,20))#Move apple randomly
        #x = random.randrange(-280,280,20)
        #y = random.randint(-280,280,20)
        #food.goto(x,y)
        
        new_segment = turtle.Turtle()#add segment
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("white")
        new_segment.penup()
        segments2.append(new_segment)

        #Sound
        winsound.PlaySound("appleeat.wav",winsound.SND_ASYNC)

        #Shorten Delay
        delay2 -=0.01#increases spped of snake with each apple collision

        #Scoring
        score2 += 10#10 for every apple
        if score2 > high_score:
            high_score = score2#highest score becomes high score
        pen.clear()
        pen.write("Snake1 : {} Snake2 : {} High Score : {}".format(score, score2, high_score), align="center", font=("Normal", 20, "underline"))

    #Add segments to body in reverse order
#Snake1
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
#Snake2 
    for index in range(len(segments2)-1, 0, -1):
        x = segments2[index-1].xcor()
        y = segments2[index-1].ycor()
        segments2[index].goto(x,y)

    #Move 1st segment to head
#Snake1
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
#Snake2
    if len(segments2) > 0:
        x = head2.xcor()
        y = head2.ycor()
        segments2[0].goto(x,y)

    move()
    move2()

    #Check if head hits body
#Snake1
    for segment in segments:
        if segment.distance(head)<20:
            #time.sleep(1)#pauses game with collsion
            head.goto(-100,0)
            head.direction = "stop"

            score = 0#score resets with body collsion
            pen.clear()
            pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("Normal", 20, "underline"))

            for segment in segments:#every body square in body
                segment.goto(1000,1000)#sends body off screen

            segments.clear#clears body
#Snake2
    for segment in segments2:
        if segment.distance(head2)<20:
            #time.sleep(1)#pauses game with collsion
            head2.goto(100,0)
            head2.direction = "stop"

            score2 = 0#score resets with body collsion
            pen.clear()
            pen.write("Snake1 : {} Snake2 : {} High Score : {}".format(score, score2, high_score), align="center", font=("Normal", 20, "underline"))

            for segment in segments2:#every body square in body
                segment.goto(1000,1000)#sends body off screen

            segments2.clear#clears body

    #Snake1 hits snake 2
    for segment in segments:
        if segment.distance(head2)<20:
            head2.goto(100,0)
            head2.direction = "stop"
            score += score2#snake1 getspoints of snake2
            pen.clear()
            pen.write("Snake1 : {} Snake2 : {} High Score : {}".format(score, score2, high_score), align="center", font=("Normal", 20, "underline"))
    
    for segment in segments2:
        if segment.distance(head)<20:
            head.goto(-100,0)
            head.direction = "stop"
            score2 += score#snake2 gets snake1 points
            pen.clear()
            pen.write("Snake1 : {} Snake2 : {} High Score : {}".format(score, score2, high_score), align="center", font=("Normal", 20, "underline"))

    time.sleep(delay)

wn.mainloop()