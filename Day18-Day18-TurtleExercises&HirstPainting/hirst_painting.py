import turtle
import random
import colorgram
from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
rgb_colors = []
colors = colorgram.extract('hirst_image.jpg', 30)

# colors grabbed via below function
grabbed_colors = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188),
                  (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
                  (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8),
                  (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
                  (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]


def grab_colors(color_list):
    for color in color_list:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)


def hirst_drawing(color_list):
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)

    num_of_dots = 100

    for dot_count in range(1, num_of_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


# grab_colors(colors)

hirst_drawing(grabbed_colors)

screen = Screen()
screen.exitonclick()
