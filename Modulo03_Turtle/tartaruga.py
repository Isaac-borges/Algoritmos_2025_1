import turtle

def main() : 
    bob = turtle.Turtle()
    configurarTurtle(bob)

    #Desenhar quadrado
    comprimento = 200
    circulo(bob, comprimento)

    turtle.mainloop()




def configurarTurtle(bob: turtle.Turtle) :
    bob.shape('square')


#  def quadrado(bob: turtle.Turtle, comprimento: float) :
#      bob.fd(comprimento)
#      bob.lt(90)
#      bob.fd(comprimento)
#      bob.lt(90)
#      bob.fd(comprimento)
#      bob.lt(90)
#      bob.fd(comprimento)

def triangulo(bob: turtle.Turtle, comprimento: float) :
    bob.fd(comprimento)
    bob.lt(120)
    bob.fd(comprimento)
    bob.lt(120)
    bob.fd(comprimento)

def circulo(bob: turtle.Turtle, comprimento: float) :
    bob.circle()





main()