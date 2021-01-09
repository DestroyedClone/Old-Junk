from turtle import *
sven_a = Turtle()
sven_b = Turtle()
sven_c = Turtle()
global SVENS
SVENS = [sven_a,sven_b,sven_c]
global SVENS_POS
SVENS_POS = []
global SVEN_RADIUS
SVEN_RADIUS = 25
global GOTO
GOTO = [0,0]

##Setup
for i in range(len(SVENS)):
    SVENS[i].pu()

screen = Screen()

def forward():
    global SVENS
    global SVENS_POS
    SVENS[0].forward(sven_radius)
    for i in range(len(SVENS)):
        sven_tuple = []
        sven_tuple.extend([
        SVENS[i].xcor(),
        SVENS[i].ycor(),
        SVENS[i].heading()]
        )
        if i > 1:
            SVENS[i].towards(SVENS[i-1].pos())
        SVENS_POS.append(sven_tuple)
    
    print(SVENS_POS)
#a^2 + b^2 = c^2
def pyth(x1,y1,x2,y2):
    a = abs(x2-x1)**2
    b = abs(y2-y1)**2
    c = (a+b)**(1/2)
    return c

#https://stackoverflow.com/questions/35530937/how-to-make-a-turtle-object-look-at-where-the-mouse-has-clicked
def turtle_lookat(turtle, lookx, looky):
    val = turtle.towards(lookx,looky) - turtle.heading()
    print(val)
    if val <= 180:
        turtle.left(val)
        #print('left')
    elif val > 180:
        turtle.right(360-val)
        #print('right')


def move_sven(x,y,turtle=SVENS[0]): #rewrite function so that the mouse1 passes to i
    global GOTO
    global SVENS
    global SVEN_RADIUS
    GOTO = [x,y]
    dist = pyth(turtle.xcor(),turtle.ycor(),x,y)
    turtle_lookat(turtle,x,y)
    while dist > SVEN_RADIUS:
        dist = pyth(turtle.xcor(),turtle.ycor(),x,y)
        print(dist)
        turtle_lookat(turtle,x,y)
        turtle.forward(5)
    GOTO = [0,0]
def follow_sven(x,y,z=SVENS):
    for i in range(len(z)):
        

screen.onkey(forward, "w")
#screen.onclick(move_sven)
screen.onclick(move_sven)
screen.listen()
