import turtle
turtle = turtle.Turtle()
def square():
   
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
for i in range(45):
    square()
    turtle.right(8)
turtle.right(90)
turtle.forward(250)
turtle.exitonclick()      
