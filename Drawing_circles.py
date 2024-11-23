#Drawing  multiple circles using  turtle library

from turtle import Turtle,Screen
import random
turtle=Turtle()

colour=['blue','azure4','brown4','burlywood3','coral2']
turtle.speed('fastest')
def darw_spirograph(size):
    for i in range(360//size):
        turtle.color(random.choice(colour))
        turtle.circle(100)
        turtle.setheading(turtle.heading()+10)
darw_spirograph(5)
screen=Screen()
screen.exitonclick()