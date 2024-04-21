import turtle
velocidad_inicial = 2
aceleracion = 0.5
tiempo = 4
velocidad_final = velocidad_inicial + aceleracion * tiempo
print("La velocidad final es: ", velocidad_final)
t = turtle.Turtle()
t.speed(velocidad_inicial)
t.forward(200)
t.speed(velocidad_final)
t.forward(100)
turtle.done()