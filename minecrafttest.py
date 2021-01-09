from turtle import *
greg = Turtle()
screen = Screen()
grid = Turtle()
gridrange = [5,5]
gridmult = 25
screen.delay(0)
grid.speed(5)

global mousex
mousex = 0
global mousey
mousey = 0
def getmpos(x,y):
    global mousex
    global mousey
    mousex = x
    mousey = y
    #print(x,y)

def whole(val):
    return int(val)

def fract(val):
    shit = str(val)
    shitindex = shit.find('.')
    part_a = shit[shitindex+1:]
    part_a_fl = float(part_a)
    part_a_len = len(part_a)
    return part_a_fl*10**-part_a_len

def drawsquare(a,b):
    grid.clear()
    grid.pu()
    grid.goto(a[0],a[1])
    grid.pd()
    grid.goto(a[0],b[1])
    grid.goto(b[0],b[1])
    grid.goto(b[0],a[1])
    grid.goto(a[0],a[1])

def figure(x,y):
    part1 = [whole(mousex),whole(mousey)]
    print("\npart1:",part1)
    part2 = [part1[0]/gridmult,part1[1]/gridmult]
    print("part2:",part2)
    part3 = [whole(part2[0]),whole(part2[1])]
    print("part3:",part3)
    part4 = [fract(part2[0]),fract(part2[1])]
    print("part4:",part4)
    drawsquare(part3,[part3[0]+gridmult,part3[1]+gridmult])

def shit(x,y):
    getmpos(x,y)
    figure(x,y)


screen.onclick(shit)
#screen.onkey(printmpos, "Up")
screen.listen()
