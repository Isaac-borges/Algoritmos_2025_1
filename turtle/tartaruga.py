import turtle

def main():
    screen = turtle.Screen()
    screen.setup(400, 400)
    screen.bgpic('space.gif')
    screen.register_shape('soul.gif')
    

    bob = turtle.Turtle()
    bob.shape('soul.gif')
    print(bob)



    turtle.mainloop()

def forward():
  turtle.forward(10)

def backward():
  turtle.backward(10)

def left():
  turtle.left(10)

def right():
  turtle.right(10)


def configurar_turtle(bob: turtle.Turtle):
    pass
    


main()