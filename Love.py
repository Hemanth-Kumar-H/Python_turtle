import turtle
from turtle import *
def heart(): #Declearing a function
    color("red")
    begin_fill()
    left(50)
    forward(190)
    circle(80, 180)
    left(260)
    circle(80, 180)
    forward(190)
    end_fill()
    turtle.write("     I LOVE YOU",move=True,align="left",font=("Arial",25,"italic"))
    left(50)
    forward(35)
    color("green")
    begin_fill()
    left(50)
    forward(45)
    circle(18, 180)
    left(260)
    circle(18, 180)
    forward(50)
    end_fill()
    done()

#Calling heart function
heart()
