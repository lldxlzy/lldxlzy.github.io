from turtle import *
from time import *
def gt(x,y):
    penup()
    goto(x,y)
    pendown()
def clock():
    sL=200
    gt(x-sL//2,y+sL//2)
    pensize(3)
    pencolor("pink")
    for i in range(4):
        time = ctime()
        print(time)


for f in range(4):
    forward(100)
    right(90)
while True:    
    print(ctime())
