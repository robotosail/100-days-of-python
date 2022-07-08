# import colorgram
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()

# extracting the colors from the image using colorgram
# colors = colorgram.extract("image.jpg", 100)
# rgb_colors = []

# # looping through each color
# for color in colors:
#     # getting the red blue and green colors
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.g
#     # putting them in a tuple
#     new_colors = (r, g, b)
#     # appending the tuple to the list
#     rgb_colors.append(new_colors)

# print(rgb_colors)

# change color mode
turtle.colormode(255)
color_list = [(214, 157, 157), (33, 105, 105), (238, 215, 215), (153, 75, 75), (125, 168, 168), (209, 134, 134), (156, 60, 60), (22, 39, 39), (212, 85, 85), (176, 162, 162), (200, 85, 85), (135, 184, 184), (56, 119, 119),
              (25, 46, 46), (228, 167, 167), (64, 46, 46), (87, 157, 157), (9, 99, 99), (34, 166, 166), (40, 60, 60), (228, 175, 175), (179, 189, 189), (95, 126, 126), (68, 34, 34), (105, 42, 42), (170, 205, 205), (113, 43, 43), (156, 206, 206), (78, 69, 69), (3, 90, 90)]

# putting the pen up so it doesn't leave trails
t.penup()
# hides the turtle
t.hideturtle()
# moving the turtle or the pen
t.seth(225)
t.fd(300)
t.seth(0)
num_of_dots = 100

# making it draw 10 dots per rows and columns


for dot_count in range(1, num_of_dots + 1):
    # drawing a dot with a size of 20 and random color
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.seth(0)


screen.exitonclick()

# class Paint:
#     def __init__(self, num_of_dots):
#         self.num_of_dots = num_of_dots

#     def paint(self, count):
#         self.counts = count
#         for self.count in range(self.counts):
#             for self.dot_count in range(self.num_of_dots):
#                 # drawing a dot with a size of 20 and random color
#                 t.dot(20, random.choice(color_list))
#                 t.forward(50)
#             t.setheading(90)
#             t.forward(50)
#             t.setheading(180)
#             t.forward(500)
#             t.seth(0)
# dots = Paint(num_of_dots)
# dots.paint(10)
