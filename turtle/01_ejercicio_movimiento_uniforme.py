import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-300,0)
t.pendown()
for _ in range(600):
    t.forward(3)
  
turtle.done()