# import colorgram

# rgb_color= []
# colors = colorgram.extract('maxresdefault.jpg', 20)

# for color in colors:
#     # rgb_color.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)

# print(rgb_color)




import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [ (156, 83, 15), (217, 163, 92), (200, 177, 31),
            (46, 120, 161), (223, 203, 105), (228, 170, 165),
            (202, 93, 71), (196, 148, 160),
            (94, 161, 61), (125, 78, 97),(126, 44, 16),
            (151, 179, 145),(214, 204, 33)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()