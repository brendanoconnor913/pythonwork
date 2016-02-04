import turtle


def draw_circle(x,y,radius):
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()
    
turtle.speed(1)
turtle.pencolor('red')
turtle.fillcolor('blue')
turtle.shape('turtle')


draw_circle(20,40,40)






