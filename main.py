import turtle as turtle_module
import random
#import colorgram

# colors = colorgram.extract('hirst.jpeg',30)
# rgb_colors =[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple = (r,g,b)
#     rgb_colors.append(new_tuple)
#
# print(rgb_colors
turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(239, 241, 246), (233, 243, 239), (245, 235, 242),  (141, 174, 201), (22, 30, 46), (34, 106, 151), (207, 159, 112), (227, 211, 100), (141, 28, 61), (173, 49, 83), (211, 71, 99), (12, 163, 193), (193, 137, 169), (63, 168, 114), (136, 91, 74), (32, 60, 111), (115, 180, 110), (223, 79, 48), (191, 184, 43), (172, 209, 178), (7, 94, 111), (238, 205, 4), (78, 31, 64), (50, 144, 111), (221, 174, 192), (229, 171, 162), (143, 208, 230), (186, 184, 212), (108, 38, 36)]
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")

number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()