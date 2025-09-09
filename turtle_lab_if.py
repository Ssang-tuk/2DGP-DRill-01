import turtle

while True:
    shape = input('Enter shape: ')
    if shape == 'circle':
        turtle.circle(50)
    elif shape == 'triangle':
        turtle.forward(50); turtle.left(50)
        turtle.forward(50); turtle.left(50)
        turtle.forward(50)
    elif shape == 'quit':
        break
