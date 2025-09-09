import turtle

def draw_circle(x,y,r):
    c_x, c_y = x, y

    turtle.penup()
    turtle.goto(c_x, c_y)
    turtle.stamp()
    turtle.pendown()

    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.circle(r)



turtle.shape("turtle")
draw_circle(0,0,50)
draw_circle(200,200,100)
draw_circle(100,-100,50)

turtle.exitonclick()
