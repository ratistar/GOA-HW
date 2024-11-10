from turtle import *


#we want to paint a house

#step 1: square

speed(50)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawning a door


forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto (140, 140)
pendown()

left(30)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)

penup()
goto (20, 140)
pendown()

left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)








exitonclick()