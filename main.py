import turtle
import random

def rand_color():
     hex_digits = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
     len = 16
     color_string = "#"
     for i in range(6):
         color_string += str(random.choice(hex_digits))
     return(color_string)

from turtle import Turtle, Screen
tim = Turtle()
for i in range(0, 360):
    color=rand_color()
    tim.shape("turtle")
    tim.color(color)
    tim.speed("fastest")
    tim.circle(100)
    tim.setheading(i)
    if i % 89 == 0:
        tim.circle(100)

# sides = 3
# side_len = 100
# tim.fillcolor("red")
# def rand_move():
#     turns = [0, 90, 180, 270, 360]
#     move = random.randrange(0,50)
#     color = rand_color()
#     tim.color(color)
#     tim.pensize(20)
#     tim.right(random.choice(turns))
#     tim.forward(move)
#     tim.speed("fastest")
#

#
#
#
# def make_shape(sides, len, color):
#     angle = 360 / sides
#     for a in range(sides):
#         #print(angle)
#         tim.color(color)
#         tim.pendown()
#         tim.forward(len)
#         tim.right(angle)
# while 1==1:
#     rand_move()
#
# # for x in range(90):
# #     offset = (-1*(side_len/2))
# #     tim.penup()
# #     tim.setx(offset)
# #     tim.sety(150)
# #     color = rand_color()
# #
# #     #make_shape(sides,side_len,color)
# #     sides += 1
# #     # side_len += 10
# #
# # # tim.forward(side_len)
#
#
#
#
#
#
#
#
screen = Screen()
screen.exitonclick()